# Week 3 – Research Desk

## What I Built

This week I upgraded my Week 2 agent into a research assistant called **Research Desk**. The agent can search the web, read papers, save notes, and remember previous conversations through persistent sessions.

The core logic is implemented inside an `Agent` class. The same agent can be used in an interactive REPL, a one-shot command, or through a Textual UI.

## Features Implemented

### Persistent Sessions

- Conversations are saved as JSON files inside `.agent/sessions/`.
- Sessions can be resumed later using their session IDs.
- The agent remembers previous discussions.

### AGENTS.md

- Rules are loaded from `AGENTS.md` and used as the system prompt.
- The file contains instructions about citations, paper usage, research notes, and response style.

### Web Tools

Implemented:

- `web_search()`
- `web_fetch()`

These tools are used for non-academic questions.

### Paper Tools

Implemented:

- `paper_search()`
- `read_paper()`

The tools use the Hugging Face Papers API and allow the agent to search and read arXiv papers.

### File Tools

Implemented:

- `read_file()`
- `write_file()`
- `list_files()`
- `edit_file()`

The file tools support reading specific line ranges and editing files through append, replace, and delete operations.

### REPL and One-Shot CLI

Interactive mode:

```bash
python agent.py
```

One-shot mode:

```bash
python agent.py "What is Q-learning?"
```

The same Agent class powers both modes.

### Research Notes

The agent can create and update notes inside the `notes/` directory. Existing notes can be modified without rewriting the entire file.

## Challenges Faced

The biggest challenge was understanding Git repositories and remotes. I initially worked inside a cloned repository and later changed the remote to my own GitHub repository before pushing the final project.

I also spent time debugging session persistence, file paths, and integrating paper tools with the agent.

## What I Learned

Through this project I learned:

- How to store conversations using JSON.
- How persistent memory works in agents.
- How to separate agent logic from the user interface.
- How tool-based agents are structured.
- Basic software architecture and code organization.
- Git remote management and repository handling.

Overall, this project gave me a better understanding of how research agents like Cursor and Claude Code maintain memory and interact with tools.