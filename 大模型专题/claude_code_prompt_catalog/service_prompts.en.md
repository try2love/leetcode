# Service and Background Prompts

This file excerpts prompts used by Claude Code for summarization, memory, documentation maintenance, suggestions, and sidecar behaviors.

## 1. Conversation Compact / Summarization Prompts
Source:
- `restored-src/src/services/compact/prompt.ts`

Variants:
- `BASE_COMPACT_PROMPT`
- `PARTIAL_COMPACT_PROMPT`
- `PARTIAL_COMPACT_UP_TO_PROMPT`

Core excerpt:
- Respond with text only.
- Produce an `<analysis>` block and a `<summary>` block.
- Summaries must preserve:
  - user requests and intent
  - technical concepts
  - files and code sections
  - errors and fixes
  - pending tasks
  - current work / next step
- Partial variants summarize only the recent portion of the conversation or only the earlier prefix being compacted.

## 2. Session Memory Template and Update Prompt
Source:
- `restored-src/src/services/SessionMemory/prompts.ts`

Core template sections:
- Session Title
- Current State
- Task specification
- Files and Functions
- Workflow
- Errors & Corrections
- Codebase and System Documentation
- Learnings
- Key results
- Worklog

Update-prompt excerpt:
- This note-taking instruction is not part of the real user conversation.
- Update the session notes file using Edit only.
- Preserve section headers and italicized template instructions exactly.
- Write dense, specific, actionable notes.
- Keep “Current State” accurate.

## 3. Magic Docs Update Prompt
Source:
- `restored-src/src/services/MagicDocs/prompts.ts`

Extract:
- Update a tracked Magic Doc only if there is substantial new information.
- Keep docs current to the latest codebase state.
- Update in place rather than appending history.
- Focus on architecture, entry points, rationale, patterns, and navigation value.
- Avoid exhaustive function-by-function documentation.

## 4. Memory Extraction Prompt
Source:
- `restored-src/src/services/extractMemories/prompts.ts`

Variants:
- `buildExtractAutoOnlyPrompt(...)`
- `buildExtractCombinedPrompt(...)`

Extract:
- Act as a memory-extraction subagent.
- Use only the most recent messages to update persistent memory.
- Do not investigate beyond those messages.
- Prefer updating existing memory files instead of creating duplicates.
- Follow memory type and frontmatter conventions.
- When team memory is enabled, choose between private and team memory scopes carefully and never save sensitive secrets to shared memory.

## 5. Away Summary Prompt
Source:
- `restored-src/src/services/awaySummary.ts`

Extract:
- The user stepped away and is coming back.
- Write exactly 1-3 short sentences.
- Start with the high-level task.
- Then state the concrete next step.
- Skip status-report fluff and commit recaps.

## 6. Agent Progress Summary Prompt
Source:
- `restored-src/src/services/AgentSummary/agentSummary.ts`

Extract:
- Describe the most recent action in 3-5 words.
- Use present tense / `-ing`.
- Name the file or function, not the branch.
- Do not use tools.
- Must say something new if there was a previous summary.

## 7. Tool-Use Summary Prompt
Source:
- `restored-src/src/services/toolUseSummary/toolUseSummaryGenerator.ts`

Extract:
- Write a short single-line label describing what recent tool calls accomplished.
- Designed for mobile UI rows that truncate around 30 characters.
- Use past tense and the most distinctive noun.

## 8. Prompt Suggestion Prompt
Source:
- `restored-src/src/services/PromptSuggestion/promptSuggestion.ts`

Extract:
- Suggest what the user might naturally type next into Claude Code.
- Predict what the user would actually type, not what Claude wants them to do.
- Keep it to 2-12 words.
- Avoid evaluative comments, Claude-voice phrasing, new ideas, and multiple sentences.
- Return only the suggestion or silence.

## 9. Dream / Memory Consolidation Prompt
Source:
- `restored-src/src/services/autoDream/consolidationPrompt.ts`

Extract:
- Perform a reflective pass over memory files.
- Orient in the memory directory and recent transcripts.
- Consolidate useful new information into durable topic memories.
- Remove contradictions and stale memories.
- Keep the memory index concise and navigable.

## 10. Claude-in-Chrome Prompt Family
Source:
- `restored-src/src/utils/claudeInChrome/prompt.ts`

### Base Chrome Prompt
Extract:
- Use Chrome browser automation tools for web interaction.
- Record GIFs for multi-step flows when helpful.
- Use console-reading tools carefully with filtering.
- Avoid triggering modal dialogs that block the extension.
- Start each browser session by reading tab context.
- Stop and ask the user if browser automation enters a rabbit hole or repeatedly fails.

### Chrome ToolSearch Instructions
Extract:
- Before using any `mcp__claude-in-chrome__*` tool, first load it via ToolSearch.

### Claude-in-Chrome Skill Hints
Extract:
- If the extension is present, the model may get a startup hint telling it to invoke the `claude-in-chrome` skill first.
- When WebBrowser is also available, the hint steers development-loop tasks to WebBrowser and reserves claude-in-chrome for authenticated real-user Chrome sessions.
