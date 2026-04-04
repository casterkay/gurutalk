## Documentation Index

- [Ingesting context to supermemory](https://supermemory.ai/docs/add-memories.md): Add text, files, and URLs to Supermemory
- [Configure connection](https://supermemory.ai/docs/api-reference/connections/configure-connection.md): Configure resources for a connection (supported providers: GitHub for now)
- [Create connection](https://supermemory.ai/docs/api-reference/connections/create-connection.md): Initialize connection and get authorization URL
- [Delete connection](https://supermemory.ai/docs/api-reference/connections/delete-connection.md): Delete connection for a specific provider and container tags
- [Delete connection by ID](https://supermemory.ai/docs/api-reference/connections/delete-connection-by-id.md): Delete a specific connection by ID
- [Fetch resources](https://supermemory.ai/docs/api-reference/connections/fetch-resources.md): Fetch resources for a connection (supported providers: GitHub for now)
- [Get connection (by id)](https://supermemory.ai/docs/api-reference/connections/get-connection-by-id.md): Get connection details with id
- [Get connection (by provider)](https://supermemory.ai/docs/api-reference/connections/get-connection-by-provider.md): Get connection details with provider and container tags
- [List connections](https://supermemory.ai/docs/api-reference/connections/list-connections.md): List all connections
- [List documents](https://supermemory.ai/docs/api-reference/connections/list-documents.md): List documents indexed for a provider and container tags
- [Sync connection](https://supermemory.ai/docs/api-reference/connections/sync-connection.md): Initiate a manual sync of connections
- [Delete container tag](https://supermemory.ai/docs/api-reference/container-tags/delete-container-tag.md): Delete a container tag and all its documents and memories. Only organization owners and admins can perform this action.
- [Get container tag settings](https://supermemory.ai/docs/api-reference/container-tags/get-container-tag-settings.md): Get settings for a container tag
- [Merge container tags](https://supermemory.ai/docs/api-reference/container-tags/merge-container-tags.md): Merge multiple container tags into a target tag. All documents from the source tags will be updated to reference the target tag, and the source tags will be deleted after successful merge.
- [Update container tag settings](https://supermemory.ai/docs/api-reference/container-tags/update-container-tag-settings.md): Update settings for a container tag
- [Ingest or update conversation](https://supermemory.ai/docs/api-reference/conversations/ingest-or-update-conversation.md): Ingest or update a conversation
- [Get graph bounds](https://supermemory.ai/docs/api-reference/graph/get-graph-bounds.md): Get the bounding box of all documents with spatial coordinates
- [Get graph statistics](https://supermemory.ai/docs/api-reference/graph/get-graph-statistics.md): Get summary statistics for the graph
- [Get graph viewport data](https://supermemory.ai/docs/api-reference/graph/get-graph-viewport-data.md): Fetch documents (with memories) and memory edges within a viewport
- [Add document](https://supermemory.ai/docs/api-reference/manage-documents/add-document.md): Add a document with any content type (text, url, file, etc.) and metadata
- [Batch add documents](https://supermemory.ai/docs/api-reference/manage-documents/batch-add-documents.md): Add multiple documents in a single request. Each document can have any content type (text, url, file, etc.) and metadata
- [Bulk delete documents](https://supermemory.ai/docs/api-reference/manage-documents/bulk-delete-documents.md): Bulk delete documents by IDs or container tags
- [Delete document by ID or customId](https://supermemory.ai/docs/api-reference/manage-documents/delete-document-by-id-or-customid.md): Delete a document by ID or customId
- [Get document](https://supermemory.ai/docs/api-reference/manage-documents/get-document.md): Get a document by ID
- [Get document chunks](https://supermemory.ai/docs/api-reference/manage-documents/get-document-chunks.md): Get all chunks for a document, ordered by position
- [Get processing documents](https://supermemory.ai/docs/api-reference/manage-documents/get-processing-documents.md): Get documents that are currently being processed
- [List documents](https://supermemory.ai/docs/api-reference/manage-documents/list-documents.md): Retrieves a paginated list of documents with their metadata and workflow status
- [Update document](https://supermemory.ai/docs/api-reference/manage-documents/update-document.md): Update a document with any content type (text, url, file, etc.) and metadata
- [Upload a file](https://supermemory.ai/docs/api-reference/manage-documents/upload-a-file.md): Upload a file to be processed
- [List memory entries with history](https://supermemory.ai/docs/api-reference/memories-v4/list-memory-entries-with-history.md): List all latest memory entries from specified container tags with their update history and source documents
- [Create memories directly](https://supermemory.ai/docs/api-reference/memories/create-memories-directly.md): Create memories directly, bypassing the document ingestion workflow. Generates embeddings and makes them immediately searchable.
- [Forget a memory](https://supermemory.ai/docs/api-reference/memories/forget-a-memory.md): Forget (soft delete) a memory entry. The memory is marked as forgotten but not permanently deleted.
- [Update a memory (creates new version)](https://supermemory.ai/docs/api-reference/memories/update-a-memory-creates-new-version.md): Update a memory by creating a new version. The original memory is preserved with isLatest=false.
- [Get settings](https://supermemory.ai/docs/api-reference/organization-settings/get-settings.md): Get settings for an organization
- [Toggle overage](https://supermemory.ai/docs/api-reference/organization-settings/toggle-overage.md): Toggle overage billing for the organization
- [Update settings](https://supermemory.ai/docs/api-reference/organization-settings/update-settings.md): Update settings for an organization
- [Get user profile](https://supermemory.ai/docs/api-reference/profile/get-user-profile.md): Get user profile with optional search results
- [Search documents](https://supermemory.ai/docs/api-reference/search/search-documents.md): Search memories with advanced filtering
- [Search memory entries](https://supermemory.ai/docs/api-reference/search/search-memory-entries.md): Search memory entries - Low latency for conversational
- [Authentication](https://supermemory.ai/docs/authentication.md): API keys, scoped keys, and connector branding.
- [Changelog](https://supermemory.ai/docs/changelog/overview.md): New updates and improvements to Supermemory
- [Supported Content Types](https://supermemory.ai/docs/concepts/content-types.md): All the content formats Supermemory can ingest and process
- [Customizing for Your Use Case](https://supermemory.ai/docs/concepts/customization.md): Configure Supermemory's behavior for your specific application
- [Organizing & Filtering Memories](https://supermemory.ai/docs/concepts/filtering.md): Use container tags and metadata to organize and retrieve memories
- [How Graph Memory Works](https://supermemory.ai/docs/concepts/graph-memory.md): Automatic memory evolution, knowledge updates, and intelligent forgetting
- [How Supermemory Works](https://supermemory.ai/docs/concepts/how-it-works.md): Understanding the knowledge graph architecture that powers intelligent memory
- [Memory vs RAG: Understanding the Difference](https://supermemory.ai/docs/concepts/memory-vs-rag.md): Learn why agent memory and RAG are fundamentally different, and when to use each approach
- [SuperRAG (Managed RAG as a service)](https://supermemory.ai/docs/concepts/super-rag.md): Supermemory provides a managed RAG solution - extraction, indexing, storing, and retrieval.
- [User Profiles](https://supermemory.ai/docs/concepts/user-profiles.md): Automatically maintained context about your users
- [GitHub Connector](https://supermemory.ai/docs/connectors/github.md): Connect GitHub repositories to sync documentation files into your Supermemory knowledge base
- [Gmail Connector](https://supermemory.ai/docs/connectors/gmail.md): Sync email threads from Gmail with real-time Pub/Sub webhooks and incremental sync
- [Google Drive Connector](https://supermemory.ai/docs/connectors/google-drive.md): Connect Google Drive to sync documents into your Supermemory knowledge base
- [Notion Connector](https://supermemory.ai/docs/connectors/notion.md): Sync Notion pages, databases, and blocks with real-time webhooks and workspace integration
- [OneDrive Connector](https://supermemory.ai/docs/connectors/onedrive.md): Sync Microsoft Office documents from OneDrive with scheduled synchronization and business account support
- [Connectors Overview](https://supermemory.ai/docs/connectors/overview.md): Integrate Google Drive, Gmail, Notion, OneDrive, GitHub and Web Crawler to automatically sync documents into your knowledge base
- [S3 Connector](https://supermemory.ai/docs/connectors/s3.md): Connect Amazon S3 or S3-compatible storage to sync files into your Supermemory knowledge base
- [Connector Troubleshooting](https://supermemory.ai/docs/connectors/troubleshooting.md): Diagnose and resolve common issues with Google Drive, Gmail, Notion, and OneDrive connectors
- [Web Crawler Connector](https://supermemory.ai/docs/connectors/web-crawler.md): Crawl and sync websites automatically with scheduled recrawling and robots.txt compliance
- [AI SDK Integration](https://supermemory.ai/docs/cookbook/ai-sdk-integration.md): Complete examples showing how to use Supermemory with Vercel AI SDK for building intelligent applications
- [Chat with Google Drive](https://supermemory.ai/docs/cookbook/chat-with-gdrive.md)
- [Customer Support Bot](https://supermemory.ai/docs/cookbook/customer-support.md): Build an intelligent support system that remembers customer history and provides personalized help
- [Document Q&A System](https://supermemory.ai/docs/cookbook/document-qa.md): Build a chatbot that answers questions from your documents with citations and source references
- [Cookbook](https://supermemory.ai/docs/cookbook/overview.md): Complete examples and recipes for building with Supermemory
- [Perplexity with memory](https://supermemory.ai/docs/cookbook/perplexity-supermemory.md)
- [Personal AI Assistant](https://supermemory.ai/docs/cookbook/personal-assistant.md): Build an AI assistant that remembers user preferences, habits, and context across conversations
- [Document Operations](https://supermemory.ai/docs/document-operations.md): List, get, update, and delete your ingested documents
- [Microsoft Agent Framework](https://supermemory.ai/docs/integrations/agent-framework.md): Add persistent memory to Microsoft Agent Framework agents with Supermemory
- [Agno](https://supermemory.ai/docs/integrations/agno.md): Add persistent memory to Agno agents with Supermemory
- [Vercel AI SDK](https://supermemory.ai/docs/integrations/ai-sdk.md): Use Supermemory with Vercel AI SDK for seamless memory management
- [Claude Code](https://supermemory.ai/docs/integrations/claude-code.md): Claude Code Supermemory Plugin — persistent memory across coding sessions
- [Claude Memory Tool](https://supermemory.ai/docs/integrations/claude-memory.md): Use Claude's native memory tool with Supermemory as the backend
- [CrewAI](https://supermemory.ai/docs/integrations/crewai.md): Add persistent memory to CrewAI agents with Supermemory
- [LangChain](https://supermemory.ai/docs/integrations/langchain.md): Build AI agents with persistent memory using LangChain and Supermemory
- [LangGraph](https://supermemory.ai/docs/integrations/langgraph.md): Add persistent memory to LangGraph agents with Supermemory
- [Mastra](https://supermemory.ai/docs/integrations/mastra.md): Add persistent memory to Mastra AI agents with Supermemory processors
- [Memory Graph](https://supermemory.ai/docs/integrations/memory-graph.md): Interactive visualization for documents, memories and connections
- [n8n](https://supermemory.ai/docs/integrations/n8n.md): Automate knowledge management with Supermemory in n8n workflows
- [OpenAI SDK](https://supermemory.ai/docs/integrations/openai.md): Memory tools for OpenAI function calling with Supermemory integration
- [OpenAI Agents SDK](https://supermemory.ai/docs/integrations/openai-agents-sdk.md): Add persistent memory to OpenAI agents with Supermemory
- [OpenClaw](https://supermemory.ai/docs/integrations/openclaw.md): OpenClaw Supermemory Plugin — works across Telegram, WhatsApp, Discord, Slack, and more
- [OpenCode](https://supermemory.ai/docs/integrations/opencode.md): OpenCode Supermemory Plugin — persistent memory across coding sessions
- [Pipecat](https://supermemory.ai/docs/integrations/pipecat.md): Integrate Supermemory with Pipecat for conversational memory in voice AI agents
- [Supermemory SDK](https://supermemory.ai/docs/integrations/supermemory-sdk.md): Official Python and JavaScript SDKs for Supermemory
- [viaSocket](https://supermemory.ai/docs/integrations/viasocket.md): Connect Supermemory with viaSocket to build automation flows using triggers, API tokens, and actions like Gmail.
- [Zapier](https://supermemory.ai/docs/integrations/zapier.md): Automate memory management with Supermemory in Zapier workflows
- [Overview — What is Supermemory?](https://supermemory.ai/docs/intro.md)
- [Managing Connection Resources](https://supermemory.ai/docs/memory-api/connectors/managing-resources.md): Get and configure resources for connections that support resource management
- [Memory Operations](https://supermemory.ai/docs/memory-operations.md): Advanced memory operations (v4 API)
- [Architecture](https://supermemory.ai/docs/memorybench/architecture.md): Understanding MemoryBench's design and implementation
- [CLI Reference](https://supermemory.ai/docs/memorybench/cli.md): Command-line interface for running MemoryBench evaluations
- [Contributing](https://supermemory.ai/docs/memorybench/contributing.md): Guidelines for contributing to MemoryBench
- [Extend Benchmark](https://supermemory.ai/docs/memorybench/extend-benchmark.md): Add a custom benchmark dataset to MemoryBench
- [Extend Provider](https://supermemory.ai/docs/memorybench/extend-provider.md): Add a custom memory provider to MemoryBench
- [MemoryBench on GitHub](https://supermemory.ai/docs/memorybench/github.md)
- [Installation](https://supermemory.ai/docs/memorybench/installation.md): Get MemoryBench up and running in your environment
- [Integrations](https://supermemory.ai/docs/memorybench/integrations.md): Supported benchmarks and providers in MemoryBench
- [MemScore](https://supermemory.ai/docs/memorybench/memscore.md): A composite metric for comparing memory providers across quality, latency, and token efficiency
- [MemoryBench](https://supermemory.ai/docs/memorybench/overview.md): Open-source framework for standardized, reproducible benchmarks of memory layer providers
- [Quick Start](https://supermemory.ai/docs/memorybench/quickstart.md): Run your first benchmark evaluation in 3 steps
- [Migrating from Mem0 to Supermemory](https://supermemory.ai/docs/migration/from-mem0.md): Complete guide to migrate your data and applications from Mem0 to Supermemory
- [Migrating from Zep to Supermemory](https://supermemory.ai/docs/migration/from-zep.md): Quick guide to migrate from Zep to Supermemory
- [Use Cases](https://supermemory.ai/docs/overview/use-cases.md): What can you do with supermemory?
- [Quickstart](https://supermemory.ai/docs/quickstart.md): Make your first API call to Supermemory - add and retrieve memories.
- [Search](https://supermemory.ai/docs/search.md): Semantic search across your memories and documents
- [Overview](https://supermemory.ai/docs/supermemory-mcp/mcp.md): Give your AI assistants persistent memory with the Model Context Protocol
- [Setup and Usage](https://supermemory.ai/docs/supermemory-mcp/setup.md): How to set up and use Supermemory MCP Server 4.0
- [User Profiles](https://supermemory.ai/docs/user-profiles.md): Fetch and use automatically maintained user context
- [Vibe Coding Setup](https://supermemory.ai/docs/vibe-coding.md): Automatic Supermemory integration using AI coding agents

## OpenAPI Specs

- [openapi](https://api.supermemory.ai/v3/openapi)

# Ingesting context to supermemory

> Add text, files, and URLs to Supermemory

Send any raw content to Supermemory — conversations, documents, files, URLs. We extract the memories automatically.

<Tip>
  **Use `customId`** to identify your content (conversation ID, document ID, etc.). This enables updates and prevents duplicates.
</Tip>

## Quick Start

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import Supermemory from 'supermemory';

    const client = new Supermemory();

    // Add text content
    await client.add({
      content: "Machine learning enables computers to learn from data",
      containerTag: "user_123",
      metadata: { category: "ai" }
    });

    // Add a URL (auto-extracted)
    await client.add({
      content: "https://youtube.com/watch?v=dQw4w9WgXcQ",
      containerTag: "user_123"
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from supermemory import Supermemory

    client = Supermemory()

    # Add text content
    client.add(
        content="Machine learning enables computers to learn from data",
        container_tag="user_123",
        metadata={"category": "ai"}
    )

    # Add a URL (auto-extracted)
    client.add(
        content="https://youtube.com/watch?v=dQw4w9WgXcQ",
        container_tag="user_123"
    )
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.supermemory.ai/v3/documents" \
      -H "Authorization: Bearer $SUPERMEMORY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "content": "Machine learning enables computers to learn from data",
        "containerTag": "user_123",
        "metadata": {"category": "ai"}
      }'
    ```
  </Tab>
</Tabs>

**Response:**

```json  theme={null}
{ "id": "abc123", "status": "queued" }
```

***

## Updating Content

Use `customId` to update existing documents or conversations. When you send content with the same `customId`, Supermemory intelligently processes only what's new.

### Two ways to update:

**Option 1: Send only the new content**

```typescript  theme={null}
// First request
await client.add({
  content: "user: Hi, I'm Sarah.\nassistant: Nice to meet you!",
  customId: "conv_123",
  containerTag: "user_sarah"
});

// Later: send only new messages
await client.add({
  content: "user: What's the weather?\nassistant: It's sunny today.",
  customId: "conv_123",  // Same ID — Supermemory links them
  containerTag: "user_sarah"
});
```

**Option 2: Send the full updated content**

```typescript  theme={null}
// Supermemory detects the diff and only processes new parts
await client.add({
  content: "user: Hi, I'm Sarah.\nassistant: Nice to meet you!\nuser: What's the weather?\nassistant: It's sunny today.",
  customId: "conv_123",
  containerTag: "user_sarah"
});
```

Both work — choose what fits your architecture.

### Replace entire document

To completely replace a document's content (not append), use `memories.update()`:

```typescript  theme={null}
// Replace the entire document content
await client.documents.update("doc_id_123", {
  content: "Completely new content replacing everything",
  metadata: { version: 2 }
});
```

This triggers full reprocessing of the document. If you only update metadata (no content change), the document is updated in place with no reindexing.

### Formatting conversations

Format your conversations however you want. Supermemory handles any string format:

```typescript  theme={null}
// Simple string
content: "user: Hello\nassistant: Hi there!"

// JSON stringify
content: JSON.stringify(messages)

// Template literal
content: messages.map(m => `${m.role}: ${m.content}`).join('\n')

// Any format — just make it a string
content: formatConversation(messages)
```

***

## Upload Files

Upload PDFs, images, and documents directly.

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import fs from 'fs';

    await client.documents.uploadFile({
      file: fs.createReadStream('document.pdf'),
      containerTags: 'user_123'
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    with open('document.pdf', 'rb') as file:
        client.documents.upload_file(
            file=file,
            container_tags='user_123'
        )
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.supermemory.ai/v3/documents/file" \
      -H "Authorization: Bearer $SUPERMEMORY_API_KEY" \
      -F "file=@document.pdf" \
      -F "containerTags=user_123"
    ```
  </Tab>
</Tabs>

### Supported File Types

| Type         | Formats                 | Processing                     |
| ------------ | ----------------------- | ------------------------------ |
| Documents    | PDF, DOC, DOCX, TXT, MD | Text extraction, OCR for scans |
| Images       | JPG, PNG, GIF, WebP     | OCR text extraction            |
| Spreadsheets | CSV, Google Sheets      | Structured data extraction     |
| Videos       | YouTube URLs, MP4       | Auto-transcription             |

**Limits:** 50MB max file size

***

## Parameters

| Parameter       | Type   | Description                                                                                                                      |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `content`       | string | **Required.** Any raw content — text, conversations, URLs, HTML                                                                  |
| `customId`      | string | **Recommended.** Your ID for the content (conversation ID, doc ID). Enables updates and deduplication                            |
| `containerTag`  | string | Group by user/project. Required for user profiles                                                                                |
| `metadata`      | object | Key-value pairs for filtering (strings, numbers, booleans)                                                                       |
| `entityContext` | string | Context for memory extraction on this container tag. Max 1500 chars. See [Customization](/concepts/customization#entity-context) |

<AccordionGroup>
  <Accordion title="Parameter Details & Examples">
    **Content Types:**

    ```typescript  theme={null}
    // Any text — conversations, notes, documents
    { content: "Meeting notes from today's standup" }
    { content: JSON.stringify(messages) }

    // URLs (auto-detected and extracted)
    { content: "https://example.com/article" }
    { content: "https://youtube.com/watch?v=abc123" }

    // Markdown, HTML, or any format
    { content: "# Project Docs\n\n## Features\n- Real-time sync" }
    ```

    **Container Tags:**

    ```typescript  theme={null}
    // By user
    { containerTag: "user_123" }

    // By project
    { containerTag: "project_alpha" }

    // Hierarchical
    { containerTag: "org_456_team_backend" }
    ```

    **Custom IDs (Recommended):**

    ```typescript  theme={null}
    // Use IDs from your system
    { customId: "conv_abc123" }        // Conversation ID
    { customId: "doc_456" }            // Document ID
    { customId: "thread_789" }         // Thread ID
    { customId: "meeting_2024_01_15" } // Meeting ID

    // Updates: same customId = same document
    // Supermemory only processes new/changed content
    await client.add({
      content: "Updated content...",
      customId: "doc_456"  // Links to existing document
    });
    ```

    **Metadata:**

    ```typescript  theme={null}
    {
      metadata: {
        source: "slack",
        author: "john",
        priority: 1,
        reviewed: true
      }
    }
    ```

    * No nested objects or arrays
    * Values: string, number, or boolean only

    **Entity Context:**

    ```typescript  theme={null}
    // Guide memory extraction for this container tag
    {
      containerTag: "session_abc123",
      entityContext: `Design exploration conversation between john@acme.com and Brand.ai assistant.
        Focus on John's design preferences and brand requirements.`
    }
    ```

    * Max 1500 characters
    * Persists on the container tag
    * Combines with org-level filter prompts
  </Accordion>
</AccordionGroup>

***

## Processing Pipeline

When you add content, Supermemory:

1. **Validates** your request
2. **Stores** the document and queues for processing
3. **Extracts** content (OCR, transcription, web scraping)
4. **Chunks** into searchable memories
5. **Embeds** for vector search
6. **Indexes** for retrieval

Track progress with `GET /v3/documents/{id}`:

```typescript  theme={null}
const doc = await client.documents.get("abc123");
console.log(doc.status); // "queued" | "processing" | "done"
```

<AccordionGroup>
  <Accordion title="Batch Upload">
    Process multiple documents with rate limiting:

    ```typescript  theme={null}
    async function batchUpload(documents: Array<{id: string, content: string}>) {
      const results = [];

      for (const doc of documents) {
        try {
          const result = await client.add({
            content: doc.content,
            customId: doc.id,
            containerTag: "batch_import"
          });
          results.push({ id: doc.id, success: true, docId: result.id });
        } catch (error) {
          results.push({ id: doc.id, success: false, error });
        }

        // Rate limit: 1 second between requests
        await new Promise(r => setTimeout(r, 1000));
      }

      return results;
    }
    ```

    **Tips:**

    * Batch size: 3-5 documents at once
    * Delay: 1-2 seconds between requests
    * Use `customId` to track and deduplicate
  </Accordion>

  <Accordion title="Error Handling">
    | Status | Error                 | Cause                                       |
    | ------ | --------------------- | ------------------------------------------- |
    | 400    | BadRequestError       | Missing required fields, invalid parameters |
    | 401    | AuthenticationError   | Invalid or missing API key                  |
    | 403    | PermissionDeniedError | Insufficient permissions                    |
    | 429    | RateLimitError        | Too many requests or quota exceeded         |
    | 500    | InternalServerError   | Processing failure                          |

    ```typescript  theme={null}
    import { BadRequestError, RateLimitError } from 'supermemory';

    try {
      await client.add({ content: "..." });
    } catch (error) {
      if (error instanceof RateLimitError) {
        // Wait and retry
        await new Promise(r => setTimeout(r, 60000));
      } else if (error instanceof BadRequestError) {
        // Fix request parameters
        console.error("Invalid request:", error.message);
      }
    }
    ```
  </Accordion>

  <Accordion title="Delete Content">
    **Single delete:**

    ```typescript  theme={null}
    await client.documents.delete("doc_id_123");
    ```

    **Bulk delete by IDs:**

    ```typescript  theme={null}
    await client.documents.deleteBulk({
      ids: ["doc_1", "doc_2", "doc_3"]
    });
    ```

    **Bulk delete by container tag:**

    ```typescript  theme={null}
    // Delete all content for a user
    await client.documents.deleteBulk({
      containerTags: ["user_123"]
    });
    ```

    Deletes are permanent — no recovery.
  </Accordion>
</AccordionGroup>

***

## Next Steps

* [Search Memories](/search) — Query your content
* [User Profiles](/user-profiles) — Get user context
* [Organizing & Filtering](/concepts/filtering) — Container tags and metadata

---

> ## Documentation Index
> Fetch the complete documentation index at: https://supermemory.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

> Semantic search across your memories and documents

Search through your memories and documents with a single API call.

<Tip>
  **Use `searchMode: "hybrid"`** for best results. It searches both memories and document chunks, returning the most relevant content.
</Tip>

## Quick Start

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import Supermemory from 'supermemory';

    const client = new Supermemory();

    const results = await client.search.memories({
      q: "machine learning",
      containerTag: "user_123",
      searchMode: "hybrid",
      limit: 5
    });

    results.results.forEach(result => {
      console.log(result.memory || result.chunk, result.similarity);
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from supermemory import Supermemory

    client = Supermemory()

    results = client.search.memories(
        q="machine learning",
        container_tag="user_123",
        search_mode="hybrid",
        limit=5
    )

    for result in results.results:
        print(result.memory or result.chunk, result.similarity)
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.supermemory.ai/v4/search" \
      -H "Authorization: Bearer $SUPERMEMORY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "q": "machine learning",
        "containerTag": "user_123",
        "searchMode": "hybrid",
        "limit": 5
      }'
    ```
  </Tab>
</Tabs>

**Response:**

```json  theme={null}
{
  "results": [
    {
      "id": "mem_xyz",
      "memory": "User is interested in machine learning for product recommendations",
      "similarity": 0.91,
      "metadata": { "topic": "interests" },
      "updatedAt": "2024-01-15T10:30:00.000Z",
      "version": 1
    },
    {
      "id": "chunk_abc",
      "chunk": "Machine learning enables personalized experiences at scale...",
      "similarity": 0.87,
      "metadata": { "source": "onboarding_doc" },
      "updatedAt": "2024-01-14T09:15:00.000Z",
      "version": 1
    }
  ],
  "timing": 92,
  "total": 5
}
```

<Info>
  In hybrid mode, results contain either a `memory` field (extracted facts) or a `chunk` field (document content), depending on the source.
</Info>

***

## Parameters

| Parameter      | Type    | Default    | Description                                        |
| -------------- | ------- | ---------- | -------------------------------------------------- |
| `q`            | string  | required   | Search query                                       |
| `containerTag` | string  | —          | Filter by user/project                             |
| `searchMode`   | string  | `"hybrid"` | `"hybrid"` (recommended) or `"memories"`           |
| `limit`        | number  | 10         | Max results                                        |
| `threshold`    | 0-1     | 0.5        | Similarity cutoff (higher = fewer, better results) |
| `rerank`       | boolean | false      | Re-score for better relevance (+100ms)             |
| `filters`      | object  | —          | Metadata filters (`AND`/`OR` structure)            |

### Search Modes

* **`hybrid`** (recommended) — Searches both memories and document chunks, returns the most relevant
* **`memories`** — Only searches extracted memories

```typescript  theme={null}
// Hybrid: memories + document chunks (recommended)
await client.search.memories({
  q: "quarterly goals",
  containerTag: "user_123",
  searchMode: "hybrid"
});

// Memories only: just extracted facts
await client.search.memories({
  q: "user preferences",
  containerTag: "user_123",
  searchMode: "memories"
});
```

***

## Filtering

Filter by `containerTag` to scope results to a user or project:

```typescript  theme={null}
const results = await client.search.memories({
  q: "project updates",
  containerTag: "user_123",
  searchMode: "hybrid"
});
```

Use `filters` for metadata-based filtering:

```typescript  theme={null}
const results = await client.search.memories({
  q: "meeting notes",
  containerTag: "user_123",
  filters: {
    AND: [
      { key: "type", value: "meeting" },
      { key: "year", value: "2024" }
    ]
  }
});
```

<Accordion title="Filter Types">
  * **String equality:** `{ key: "status", value: "active" }`
  * **String contains:** `{ filterType: "string_contains", key: "title", value: "react" }`
  * **Numeric:** `{ filterType: "numeric", key: "priority", value: "5", numericOperator: ">=" }`
  * **Array contains:** `{ filterType: "array_contains", key: "tags", value: "important" }`
  * **Negate:** `{ key: "status", value: "draft", negate: true }`

  See [Organizing & Filtering](/concepts/filtering) for full syntax.
</Accordion>

***

## Query Optimization

### Reranking

Re-scores results for better relevance. Adds \~100ms latency.

```typescript  theme={null}
const results = await client.search.memories({
  q: "complex technical question",
  containerTag: "user_123",
  rerank: true
});
```

### Threshold

Control result quality vs quantity:

```typescript  theme={null}
// Broad search — more results
await client.search.memories({ q: "...", threshold: 0.3 });

// Precise search — fewer, better results
await client.search.memories({ q: "...", threshold: 0.8 });
```

***

## Chatbot Example

Optimal configuration for conversational AI:

```typescript  theme={null}
async function getContext(userId: string, message: string) {
  const results = await client.search.memories({
    q: message,
    containerTag: userId,
    searchMode: "hybrid",
    threshold: 0.6,
    limit: 5
  });

  return results.results
    .map(r => r.memory || r.chunk)
    .join('\n\n');
}
```

<Accordion title="Response Schema">
  ```typescript  theme={null}
  interface SearchResult {
    id: string;
    memory?: string;        // Present for memory results
    chunk?: string;         // Present for document chunk results
    similarity: number;     // 0-1
    metadata: object | null;
    updatedAt: string;
    version: number;
  }

  interface SearchResponse {
    results: SearchResult[];
    timing: number;         // ms
    total: number;
  }
  ```
</Accordion>

***

## Next Steps

* [Ingesting Content](/add-memories) — Add content to search
* [User Profiles](/user-profiles) — Get user context with search
* [Organizing & Filtering](/concepts/filtering) — Container tags and metadata

---

> ## Documentation Index
> Fetch the complete documentation index at: https://supermemory.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Profiles

> Fetch and use automatically maintained user context

User profiles are extremely short summaries of context about an entity (Usually a user, but can be anything) which includes both the *static* facts about them, as well as a few recent episodes.

> You can think of these as a dynamic compaction that's done by supermemory in real-time.

This profile should be injected into the agent context for truly personalized experiences. To read more, visit [User profiles - Concept](/concepts/user-profiles)

Get a user's profile — their static facts and dynamic context — with a single API call.

<Tip>
  Profiles are built automatically as you [ingest content](/add-memories). No setup required.
</Tip>

## Quick Start

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import Supermemory from 'supermemory';

    const client = new Supermemory();

    const { profile } = await client.profile({
      containerTag: "user_123"
    });

    console.log(profile.static);   // Long-term facts
    console.log(profile.dynamic);  // Recent context
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from supermemory import Supermemory

    client = Supermemory()

    result = client.profile(container_tag="user_123")

    print(result.profile.static)   # Long-term facts
    print(result.profile.dynamic)  # Recent context
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.supermemory.ai/v4/profile" \
      -H "Authorization: Bearer $SUPERMEMORY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"containerTag": "user_123"}'
    ```
  </Tab>
</Tabs>

**Response:**

```json  theme={null}
{
  "profile": {
    "static": [
      "User is a software engineer",
      "User specializes in Python and React",
      "User prefers dark mode interfaces"
    ],
    "dynamic": [
      "User is working on Project Alpha",
      "User recently started learning Rust",
      "User is debugging authentication issues"
    ]
  }
}
```

***

## Profile + Search

Get profile and search results in one call by adding the `q` parameter:

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    const result = await client.profile({
      containerTag: "user_123",
      q: "deployment errors"
    });

    // Profile data
    const { static: facts, dynamic: context } = result.profile;

    // Search results (only if q was provided)
    const memories = result.searchResults?.results || [];
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    result = client.profile(
        container_tag="user_123",
        q="deployment errors"
    )

    # Profile data
    facts = result.profile.static
    context = result.profile.dynamic

    # Search results
    memories = result.search_results.results if result.search_results else []
    ```
  </Tab>
</Tabs>

***

## Parameters

| Parameter      | Type   | Required | Description                                        |
| -------------- | ------ | -------- | -------------------------------------------------- |
| `containerTag` | string | Yes      | User/project identifier                            |
| `q`            | string | No       | Search query (includes search results in response) |
| `threshold`    | 0-1    | No       | Filter search results by relevance score           |

***

## Building Prompts

The most common pattern — inject profile into your LLM's system prompt:

```typescript  theme={null}
async function chat(userId: string, message: string) {
  const { profile } = await client.profile({ containerTag: userId });

  const systemPrompt = `You are assisting a user.

ABOUT THE USER:
${profile.static?.join('\n') || 'No profile yet.'}

CURRENT CONTEXT:
${profile.dynamic?.join('\n') || 'No recent activity.'}

Personalize responses to their expertise and preferences.`;

  return llm.chat({
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: message }
    ]
  });
}
```

***

## Full Context Pattern

Get profile + query-specific memories in one call:

```typescript  theme={null}
async function getContext(userId: string, query: string) {
  const result = await client.profile({
    containerTag: userId,
    q: query,
    threshold: 0.6
  });

  return `
User Background:
${result.profile.static.join('\n')}

Current Context:
${result.profile.dynamic.join('\n')}

Relevant Memories:
${result.searchResults?.results.map(m => m.memory).join('\n') || 'None'}
  `;
}
```

***

## Framework Examples

<Accordion title="Express.js Middleware">
  ```typescript  theme={null}
  async function withProfile(req, res, next) {
    if (!req.user?.id) return next();

    try {
      const { profile } = await client.profile({
        containerTag: req.user.id
      });
      req.userProfile = profile;
    } catch (e) {
      req.userProfile = null;
    }
    next();
  }

  app.use(withProfile);

  app.post('/chat', (req, res) => {
    // req.userProfile available in all routes
  });
  ```
</Accordion>

<Accordion title="Next.js API Route">
  ```typescript  theme={null}
  // app/api/chat/route.ts
  export async function POST(req: NextRequest) {
    const { userId, message } = await req.json();

    const { profile } = await client.profile({
      containerTag: userId
    });

    const response = await generateResponse(message, profile);
    return NextResponse.json({ response });
  }
  ```
</Accordion>

<Accordion title="AI SDK Integration">
  ```typescript  theme={null}
  import { withSupermemory } from "@supermemory/tools/ai-sdk"
  import { openai } from "@ai-sdk/openai"

  // Profiles automatically injected
  const model = withSupermemory(openai("gpt-4"), "user-123")

  const result = await generateText({
    model,
    messages: [{ role: "user", content: "Help with my project" }]
  });
  ```

  See [AI SDK Integration](/integrations/ai-sdk) for details.
</Accordion>

***

## Response Schema

```typescript  theme={null}
interface ProfileResponse {
  profile: {
    static: string[];   // Long-term facts
    dynamic: string[];  // Recent context
  };
  searchResults?: {     // Only if q parameter provided
    results: SearchResult[];
    total: number;
    timing: number;
  };
}
```

***

## Next Steps

* [User Profiles Concept](/concepts/user-profiles) — Understand static vs dynamic
* [Ingesting Content](/add-memories) — Build profiles by adding content
* [AI SDK Integration](/integrations/ai-sdk) — Automatic profile injection
