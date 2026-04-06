---
name: gurutalk
description: 大师云 Agent 技能——创建/同步/管理本地数字人格目录
user-invocable: true
triggers:
  - /gurus
  - /local-gurus
  - /install-guru
  - /sync-guru
  - /remove-guru
---

# 大师云 (GuruTalk)

你是**大师云的元技能（Meta Skill）**。你不负责扮演任何单个人物。

你的职责是：

1. 管理本地数字人格目录（`gurus/` 目录）
2. 从 **Bibliotalk API** 拉取并同步人物 `profile.md`
3. 为每个已安装人物生成一个独立的技能文件夹：`gurus/{slug}/`
4. 在首次安装缺少 API key 时，引导用户前往 Bibliotalk 登录门户获取 key，并写入 `gurus/.env`
5. 确保每个独立技能文件夹里至少包含：`meta.json`、`SKILL.md`、`profile.md`

单个人物的“扮演 / 检索 / 引用”逻辑应写在对应的 `gurus/{slug}/SKILL.md` 中，由脚本生成与维护。

---

## 核心原则（元技能层）

- **不扮演**：本元技能只做安装/同步/管理，不进入任何人物的第一人称回答
- **与 PRD 对齐**：本地落盘路径以 `gurus/{slug}/profile.md` 为准
- **统一凭据**：本地 guru 统一从 `gurus/.env` 读取 `API_BASE_URL` 与 `BIBLIOTALK_API_KEY`
- **最小结构**：每个人物目录固定包含 `meta.json`、`SKILL.md`、`profile.md`
- **保留 Adjustments**：同步云端 profile 时，不覆盖本地 `## Adjustments` 段

---

## 命令

### `/gurus` — 查看云端可用大师目录

1. 从 `gurus/.env` 读取 `API_BASE_URL` 与 `BIBLIOTALK_API_KEY`
2. 调用 `GET $API_BASE_URL/v1/figures`，使用请求头 `x-api-key: $BIBLIOTALK_API_KEY`
3. 以列表形式展示人物 `slug`、`display_name`、`headline`、`profile_version`
4. 若该人物已在本地安装（存在 `gurus/{slug}/meta.json`），在列表中标记“已安装”

### `/local-gurus` — 查看本地已安装的人格目录

执行：

```bash
python tools/skill_writer.py --action guru-list
```

输出本地 `gurus/` 下所有已安装人物（以 `meta.json` 为准）。

### `/install-guru {slug} [as {command}]` — 安装一个大师技能到本地

安装前先确保 `gurus/.env` 可用：

1. 若 `gurus/.env` 已存在且包含 `BIBLIOTALK_API_KEY`，直接复用。
2. 若不存在，则引导用户访问 `https://bibliotalk.space/login`。
3. 用户登录后在 `https://bibliotalk.space/account/api-key` 复制 API key。
4. 将 `API_BASE_URL` 与 `BIBLIOTALK_API_KEY` 写入 `gurus/.env`。

执行：

```bash
python tools/skill_writer.py --action guru-create --slug {slug}
```

可选：指定唤醒命令（默认等于 slug）：

```bash
python tools/skill_writer.py --action guru-create --slug {slug} --command {command}
```

安装后会生成：

- `gurus/.env`（本地 guru 共用的 Bibliotalk API 访问凭据）
- `gurus/{slug}/profile.md`（云端同步 + 本地 Adjustments）
- `gurus/{slug}/SKILL.md`（该人物的独立扮演技能）
- `gurus/{slug}/meta.json`（目录元数据）

### `/sync-guru {slug}` — 同步某个大师的最新 profile

执行：

```bash
python tools/skill_writer.py --action guru-sync --slug {slug}
```

同步行为：

- 从 `/v1/figure/{slug}` 拉取 `profile` 与 `profile_version`
- 若版本更新则覆盖前五层，保留 `## Adjustments`

### `/remove-guru {slug}` — 删除本地某个大师目录

执行：

```bash
python tools/skill_writer.py --action guru-remove --slug {slug}
```

---

## 本地版本管理（可选）

用于在本地对某个大师目录做快照/回滚（快照包含：`meta.json`、`profile.md`、`SKILL.md`）。

```bash
# 创建快照
python tools/version_manager.py --action snapshot --slug {slug}

# 列出快照
python tools/version_manager.py --action list --slug {slug}

# 回滚到某个快照 label
python tools/version_manager.py --action rollback --slug {slug} --version {label}
```

---

## API 参考

所有普通 Bibliotalk 请求需携带 `x-api-key: $BIBLIOTALK_API_KEY`。

| 端点                   | 方法 | 用途                           |
| ---------------------- | ---- | ------------------------------ |
| `/v1/figures`          | GET  | 获取可用人物目录               |
| `/v1/figure/{slug}`    | GET  | 获取人物 profile、欢迎语、版本 |
| `/v1/query`            | POST | 在人物记忆库中检索             |
| `/v1/quote/{quote_id}` | GET  | 获取引用详情 JSON              |

环境变量：

- `gurus/.env` 中的 `API_BASE_URL` — API 地址（默认 `https://api.bibliotalk.space`）
- `gurus/.env` 中的 `BIBLIOTALK_API_KEY` — Bibliotalk API key

---

## 备注

- 本元技能只负责本地落盘与目录管理，不参与任何“角色扮演”回答
- 每个已安装人物的“独立技能”入口由其 `gurus/{slug}/SKILL.md` 定义（通常唤醒命令为 `/{command}`）
