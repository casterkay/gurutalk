#!/usr/bin/env python3
"""scripts/skill_writer.py

一个小型脚手架工具，用于在本仓库内创建/同步 GuruTalk 人物 Skill（`gurus/`）。

用途：
- 从 Bibliotalk API 拉取人物 profile，落盘到 `gurus/{slug}/profile.md`
- 生成可唤醒的 `gurus/{slug}/SKILL.md`

目录结构（最小）：
- `gurus/{slug}/meta.json`
- `gurus/{slug}/SKILL.md`
- `gurus/{slug}/profile.md`

环境变量：
- `API_BASE_URL` (可选，默认 https://api.bibliotalk.space)
- `BIBLIOTALK_API_KEY` (必需)
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

DEFAULT_API_BASE_URL = "https://api.bibliotalk.space"

# Agent skills directory mapping
AGENT_SKILLS_DIRS = {
    "claude": "~/.claude/skills",
    "openclaw": "~/.openclaw/workspace/skills",
}

# Default base directory for gurus (will be resolved based on agent type)
DEFAULT_AGENT = "claude"
DEFAULT_GURU_BASE_DIR = None  # Will be set to AGENT_SKILLS_DIR[agent]/gurus


GURU_SKILL_MD_TEMPLATE = """\
---
name: {command}
description: {display_name}{headline_part}
user-invocable: true
---

# {display_name}

> 本技能由大师云元技能生成与维护。资料来源：Bibliotalk 公有语料库检索与引用。

---

## Profile

{{{{include profile.md}}}}

---

## 运行规则

在发起任何 Bibliotalk 请求前：

1. 优先从当前环境读取 `API_BASE_URL` 与 `BIBLIOTALK_API_KEY`。
2. `API_BASE_URL` 缺失时默认使用 `https://api.bibliotalk.space`。
3. 若仍缺少 `BIBLIOTALK_API_KEY`，不要继续调用 Bibliotalk。先让用户访问 `https://bibliotalk.space/login` 登录并复制 API key。
4. 若宿主环境是 OpenClaw，可执行 `printf "Enter BIBLIOTALK_API_KEY: "; read -s key; echo; mkdir -p ~/.openclaw; printf 'BIBLIOTALK_API_KEY=%s\n' "$key" >> ~/.openclaw/.env`。
5. 若宿主环境是 Claude Code，可执行 `printf "Enter BIBLIOTALK_API_KEY: "; read -s key; echo; tmp=$(mktemp); jq --arg key "$key" '.env.BIBLIOTALK_API_KEY=$key' ~/.claude/settings.json > "$tmp" && mv "$tmp" ~/.claude/settings.json`。
6. 初始化完成后继续处理请求，并在调用 Bibliotalk 时使用请求头 `x-api-key: $BIBLIOTALK_API_KEY`。

收到任何消息时：

1. 你扮演 **{display_name}**。保持其思维方式、表达风格与 Personality 特质。
2. 先检索后回答：调用 `POST /v1/query`，其中 `figure` 必须是 `{slug}`。
3. 关键判断必须引用 `kind=\"chunk\"` 的结果，并在句末标注 `[n]`。
4. `kind=\"memory\"` 只能用于补充上下文，不得作为可溯源引用。
5. 若检索结果不足，明确降级："关于这个问题，我目前缺少足够材料支撑。" 不要编造。
6. 语言对齐：用户用什么语言，你就用什么语言。

引用格式：

---
[1]: [来源标题, 定位](https://bibliotalk.space/q/{{quote_id}})
"""


def _get_agent_skills_dir(agent: str) -> Path:
    """Get the skills directory for the specified agent type."""
    if agent not in AGENT_SKILLS_DIRS:
        raise RuntimeError(f"Unknown agent type: {agent}. Supported: {list(AGENT_SKILLS_DIRS.keys())}")
    return Path(AGENT_SKILLS_DIRS[agent]).expanduser()


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _request_json(
    url: str,
    *,
    headers: dict[str, str],
    method: str = "GET",
    body: Optional[dict[str, Any]] = None,
) -> Any:
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        headers={
            **headers,
            "User-Agent": "GuruTalk-SkillWriter/1.0 (+https://github.com/gurutalk)",
        },
        data=data,
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8")
        except Exception:
            body = ""
        raise RuntimeError(f"HTTP {e.code} fetching {url}: {body or e.reason}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error fetching {url}: {e.reason}") from e

def _read_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    env_data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env_data[key.strip()] = value.strip().strip('"').strip("'")
    return env_data



def _apply_runtime_env(env_data: dict[str, str]) -> dict[str, str]:
    for key, value in env_data.items():
        if value:
            os.environ[key] = value
    return env_data


def ensure_guru_api_env(base_dir: Path) -> dict[str, str]:
    env_file = base_dir / ".env"
    env_data = _read_env_file(env_file)

    api_url = (
        os.environ.get("API_BASE_URL")
        or env_data.get("API_BASE_URL")
        or DEFAULT_API_BASE_URL
    ).rstrip("/")

    api_token = (
        os.environ.get("BIBLIOTALK_API_KEY")
        or env_data.get("BIBLIOTALK_API_KEY")
        or ""
    ).strip()
    if not api_token:
        raise RuntimeError(
            "Missing BIBLIOTALK_API_KEY. Sign in at https://bibliotalk.space/login, copy your API key, then save it to your agent environment before retrying."
        )

    return _apply_runtime_env(
        {
            "API_BASE_URL": api_url,
            "BIBLIOTALK_API_KEY": api_token,
        }
    )


def _get_api_url() -> str:
    return os.environ.get("API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")


def _get_api_token() -> str:
    token = os.environ.get("BIBLIOTALK_API_KEY", "").strip()
    if not token:
        raise RuntimeError("Missing env BIBLIOTALK_API_KEY")
    return token


def fetch_figure_detail(slug: str) -> dict:
    api_url = _get_api_url()
    token = _get_api_token()
    quoted = urllib.parse.quote(slug, safe="")
    return _request_json(
        f"{api_url}/v1/figure/{quoted}",
        headers={
            "x-api-key": token,
            "Accept": "application/json",
        },
    )


def fetch_figures_index() -> list[dict]:
    api_url = _get_api_url()
    token = _get_api_token()
    data = _request_json(
        f"{api_url}/v1/figures",
        headers={
            "x-api-key": token,
            "Accept": "application/json",
        },
    )
    if isinstance(data, list):
        return data
    return []


def _extract_adjustments(profile_md: str) -> str:
    marker = "\n## Adjustments\n"
    if marker not in profile_md:
        return "（用户个人修订，由 Agent 在对话中记录）\n"
    after = profile_md.split(marker, 1)[1]
    after = after.lstrip("\n")
    return after if after.strip() else "（用户个人修订，由 Agent 在对话中记录）\n"


def _default_adjustments() -> str:
    return "（用户个人修订，由 Agent 在对话中记录）\n"


def build_profile_md(detail: dict, *, adjustments: Optional[str] = None) -> str:
    display_name = str(detail.get("display_name", detail.get("slug", "Unknown")))
    slug = str(detail.get("slug", ""))
    profile_version = str(detail.get("profile_version", ""))
    profile = detail.get("profile") or {}

    def s(key: str) -> str:
        v = profile.get(key, "")
        return str(v) if isinstance(v, str) else ""

    adjustments_block = adjustments if adjustments is not None else _default_adjustments()

    return (
        f"# {display_name}\n\n"
        f"- slug: {slug}\n"
        f"- profile_version: {profile_version}\n\n"
        "## Identity\n"
        f"{s('identity')}\n\n"
        "## Mental Models\n"
        f"{s('mental_models')}\n\n"
        "## Expression Styles\n"
        f"{s('expr_styles')}\n\n"
        "## Personality\n"
        f"{s('personality')}\n\n"
        "## Timeline\n"
        f"{s('timeline')}\n\n"
        "## Adjustments\n"
        f"{adjustments_block.rstrip()}\n"
    )


def build_guru_meta(
    *,
    slug: str,
    command: str,
    detail: dict,
    headline: Optional[str],
    adjustments: Optional[str] = None,
    created_at: Optional[str] = None,
) -> dict:
    now = _utc_now_iso()
    return {
        "kind": "guru",
        "slug": slug,
        "command": command,
        "display_name": detail.get("display_name"),
        "greeting": detail.get("greeting"),
        "headline": headline,
        "profile_version": detail.get("profile_version"),
        "adjustments": adjustments if (adjustments is not None and str(adjustments).strip()) else _default_adjustments(),
        "created_at": created_at or now,
        "updated_at": now,
        "synced_at": now,
        "source": {
            "type": "bibliotalk",
            "api_url": _get_api_url(),
        },
    }


def build_guru_skill_md(*, slug: str, command: str, display_name: str, headline: Optional[str]) -> str:
    headline_part = f" · {headline}" if headline else ""
    return GURU_SKILL_MD_TEMPLATE.format(
        slug=slug,
        command=command,
        display_name=display_name,
        headline_part=headline_part,
    )


def guru_create(
    base_dir: Path,
    *,
    slug: str,
    command: Optional[str] = None,
    force: bool = False,
) -> Path:
    skill_dir = base_dir / slug
    if skill_dir.exists() and not force:
        raise RuntimeError(f"Guru directory already exists: {skill_dir} (use --force to overwrite)")

    ensure_guru_api_env(base_dir)
    skill_dir.mkdir(parents=True, exist_ok=True)

    detail = fetch_figure_detail(slug)

    headline: Optional[str] = None
    try:
        for f in fetch_figures_index():
            if isinstance(f, dict) and f.get("slug") == slug:
                headline = f.get("headline")
                break
    except Exception:
        headline = None

    final_command = (command or slug).strip().lstrip("/")
    if not final_command:
        final_command = slug

    existing_meta_path = skill_dir / "meta.json"
    created_at: Optional[str] = None
    existing_adjustments: Optional[str] = None
    if existing_meta_path.exists():
        try:
            existing_meta = _read_json(existing_meta_path)
            created_at = existing_meta.get("created_at")
            existing_adjustments = existing_meta.get("adjustments")
        except Exception:
            created_at = None
            existing_adjustments = None

    # Migrate adjustments from existing profile.md if meta.json doesn't have it
    profile_path = skill_dir / "profile.md"
    if not (isinstance(existing_adjustments, str) and existing_adjustments.strip()) and profile_path.exists():
        try:
            existing_adjustments = _extract_adjustments(profile_path.read_text(encoding="utf-8"))
        except Exception:
            existing_adjustments = None

    meta = build_guru_meta(
        slug=slug,
        command=final_command,
        detail=detail,
        headline=headline,
        adjustments=str(existing_adjustments) if isinstance(existing_adjustments, str) else None,
        created_at=created_at,
    )
    _write_json(skill_dir / "meta.json", meta)

    # profile.md (append local adjustments from meta.json)
    profile_md = build_profile_md(detail, adjustments=str(meta.get("adjustments") or _default_adjustments()))
    profile_path.write_text(profile_md, encoding="utf-8")

    # SKILL.md
    display_name = str(detail.get("display_name", slug))
    skill_md = build_guru_skill_md(
        slug=slug,
        command=final_command,
        display_name=display_name,
        headline=headline,
    )
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    return skill_dir


def guru_sync(base_dir: Path, *, slug: str) -> str:
    ensure_guru_api_env(base_dir)
    skill_dir = base_dir / slug
    if not skill_dir.exists():
        raise RuntimeError(f"Guru directory does not exist: {skill_dir}")

    meta_path = skill_dir / "meta.json"
    meta: dict = _read_json(meta_path) if meta_path.exists() else {"slug": slug}
    command = str(meta.get("command") or slug).strip().lstrip("/") or slug

    existing_adjustments: Optional[str] = meta.get("adjustments")

    detail = fetch_figure_detail(slug)
    next_version = str(detail.get("profile_version", ""))
    prev_version = str(meta.get("profile_version", ""))

    profile_path = skill_dir / "profile.md"
    if not (isinstance(existing_adjustments, str) and existing_adjustments.strip()) and profile_path.exists():
        try:
            existing_adjustments = _extract_adjustments(profile_path.read_text(encoding="utf-8"))
        except Exception:
            existing_adjustments = None

    # headline best-effort
    headline: Optional[str] = meta.get("headline")
    try:
        for f in fetch_figures_index():
            if isinstance(f, dict) and f.get("slug") == slug:
                headline = f.get("headline")
                break
    except Exception:
        headline = headline

    # Always refresh meta timestamps; refresh profile only if version changed
    meta = build_guru_meta(
        slug=slug,
        command=command,
        detail=detail,
        headline=headline,
        adjustments=str(existing_adjustments) if isinstance(existing_adjustments, str) else None,
        created_at=meta.get("created_at"),
    )
    _write_json(meta_path, meta)

    # Only overwrite the first five layers when backend version is newer.
    # Always ensure profile.md exists; local Adjustments come from meta.json.
    if not profile_path.exists() or not (next_version and prev_version and next_version <= prev_version):
        profile_md = build_profile_md(detail, adjustments=str(meta.get("adjustments") or _default_adjustments()))
        profile_path.write_text(profile_md, encoding="utf-8")

    display_name = str(detail.get("display_name", slug))
    skill_md = build_guru_skill_md(
        slug=slug,
        command=command,
        display_name=display_name,
        headline=headline,
    )
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    return next_version or prev_version


def guru_list(base_dir: Path) -> list[dict]:
    gurus: list[dict] = []
    if not base_dir.exists():
        return gurus

    for d in sorted(base_dir.iterdir()):
        if not d.is_dir():
            continue
        meta_path = d / "meta.json"
        if not meta_path.exists():
            continue
        try:
            meta = _read_json(meta_path)
        except Exception:
            continue
        if meta.get("kind") != "guru":
            continue
        gurus.append(
            {
                "slug": meta.get("slug", d.name),
                "command": meta.get("command", d.name),
                "display_name": meta.get("display_name", d.name),
                "profile_version": meta.get("profile_version", ""),
                "updated_at": meta.get("updated_at", ""),
            }
        )
    return gurus


def guru_remove(base_dir: Path, *, slug: str) -> None:
    skill_dir = base_dir / slug
    if not skill_dir.exists():
        raise RuntimeError(f"Guru directory does not exist: {skill_dir}")
    shutil.rmtree(skill_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="GuruTalk Skill Writer")
    parser.add_argument(
        "--action",
        required=True,
        choices=[
            "guru-create",
            "guru-sync",
            "guru-list",
            "guru-remove",
        ],
    )
    parser.add_argument("--slug", help="人物 slug（guru）")
    parser.add_argument("--command", help="人物技能唤醒命令（guru，可选，默认等于 slug）")
    parser.add_argument(
        "--agent",
        default=DEFAULT_AGENT,
        choices=list(AGENT_SKILLS_DIRS.keys()),
        help=f"Agent 类型（默认: {DEFAULT_AGENT}）",
    )
    parser.add_argument(
        "--base-dir",
        default=None,
        help="根目录（默认: {agent_skills_dir}）",
    )
    parser.add_argument("--force", action="store_true", help="覆盖已存在目录（仅 guru-create）")

    args = parser.parse_args()

    # Resolve base_dir based on agent type
    if args.base_dir:
        base_dir = Path(args.base_dir).expanduser()
    else:
        base_dir = _get_agent_skills_dir(args.agent)

    if args.action == "guru-list":
        gurus = guru_list(base_dir)
        if not gurus:
            print("暂无已安装的大师 Skill")
        else:
            print(f"已安装 {len(gurus)} 个大师 Skill：\n")
            for g in gurus:
                updated = g["updated_at"][:10] if g.get("updated_at") else "未知"
                pv = g.get("profile_version") or ""
                print(f"  [{g['slug']}]  /{g['command']}  {g['display_name']}  {pv}")
                print(f"    更新: {updated}")
                print()
        return

    if args.action == "guru-create":
        if not args.slug:
            print("错误：guru-create 需要 --slug", file=sys.stderr)
            sys.exit(1)
        try:
            skill_dir = guru_create(
                base_dir,
                slug=args.slug,
                command=args.command,
                force=bool(args.force),
            )
        except Exception as e:
            print(f"错误：{e}", file=sys.stderr)
            sys.exit(1)
        meta = _read_json(skill_dir / "meta.json")
        print(f"✅ 大师 Skill 已创建：{skill_dir}")
        print(f"   触发词：/{meta.get('command', args.slug)}")
        return

    if args.action == "guru-sync":
        if not args.slug:
            print("错误：guru-sync 需要 --slug", file=sys.stderr)
            sys.exit(1)
        try:
            version = guru_sync(base_dir, slug=args.slug)
        except Exception as e:
            print(f"错误：{e}", file=sys.stderr)
            sys.exit(1)
        print(f"✅ 已同步 {args.slug}：profile_version={version}")
        return

    if args.action == "guru-remove":
        if not args.slug:
            print("错误：guru-remove 需要 --slug", file=sys.stderr)
            sys.exit(1)
        try:
            guru_remove(base_dir, slug=args.slug)
        except Exception as e:
            print(f"错误：{e}", file=sys.stderr)
            sys.exit(1)
        print(f"✅ 已删除：{base_dir / args.slug}")
        return

    print(f"错误：未知 action={args.action}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
