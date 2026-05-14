# Claude Code — Install & Setup

Quick setup guide for installing and using [Claude Code](https://claude.ai/code?utm_source=chatgpt.com) in local development environments.

---

## What is Claude Code?

Claude Code is a terminal-based AI coding assistant by [Anthropic](https://www.anthropic.com?utm_source=chatgpt.com).

Used for:

- code generation
- debugging
- refactoring
- terminal workflows
- repo understanding
- AI-assisted development

---

## Supported Platforms

- macOS
- Linux
- WSL
- Windows
- VS Code
- JetBrains
- Web
- Desktop App

---

# Terminal Native Install

## Recommended Method

Fastest and cleanest setup.

---

## macOS / Linux / WSL

```bash id="3g1f40"
curl -fsSL https://claude.ai/install.sh | bash
```

---

## Windows PowerShell

```powershell id="j3my9s"
irm https://claude.ai/install.ps1 | iex
```

---

## Windows CMD

```cmd id="ztz3m4"
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

---

## Verify Installation

```bash id="0e2fks"
claude --version
```

---

# Start Claude Code

Open any project:

```bash id="vgpr1n"
cd your-project
```

Start Claude:

```bash id="xrzm0w"
claude
```

---

# Login

Inside Claude terminal:

```bash id="2h6nru"
/login
```

This opens browser authentication.

---

# Recommended Workflow

## Create/Open Project

```bash id="5h58lk"
mkdir ai-project
cd ai-project
```

---

## Start Claude

```bash id="l09qyx"
claude
```

---

## Ask Coding Tasks

Example prompts:

```text id="y0zjv9"
Create FastAPI CRUD structure
```

```text id="7b7qrd"
Refactor this Python service
```

```text id="6p9jru"
Explain this SQL query
```

---

# Common Commands

| Command   | Purpose           |
| --------- | ----------------- |
| `claude`  | start Claude Code |
| `/login`  | authenticate      |
| `/logout` | remove session    |
| `/help`   | show commands     |
| `/clear`  | clear context     |
| `exit`    | quit              |

---

# VS Code Integration

Claude can work alongside:

- VS Code terminal
- Git workflows
- local repositories

Recommended setup:

```text id="z2c42o"
VS Code + Git + Claude Code
```

---

# Best Practices

- open Claude inside project root
- use Git repositories
- keep terminal clean
- review generated code
- commit changes frequently
- avoid exposing secrets

---

# Common Mistakes

!!! warning

```
AI-generated code still requires manual review.
```

---

## Frequent Issues

- running outside project folder
- missing login
- internet/firewall issues
- trusting generated code blindly
- exposing `.env` or secrets

---

# Security Notes

## Never Share

- API keys
- `.env`
- production credentials
- SSH private keys

---

## Add to `.gitignore`

```gitignore id="hkh1t8"
.env
node_modules
venv
dist
build
```

---

# Recommended Dev Setup

| Tool        | Purpose             |
| ----------- | ------------------- |
| Git         | version control     |
| Claude Code | AI coding assistant |
| VS Code     | editor              |
| GitHub      | repository hosting  |
| SSH         | secure Git auth     |

---

# Summary

- Claude Code = terminal AI coding assistant
- install using native shell script
- run with `claude`
- authenticate using `/login`
- works best inside Git projects
- useful for debugging, scaffolding, refactoring

!!! success

```
Claude Code is most effective when combined with Git, terminal workflows, and real project repositories.
```
