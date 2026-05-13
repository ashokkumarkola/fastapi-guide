# Git SSH Keys & Authentication

Modern Git authentication setup using SSH keys for secure GitHub access.

---

## What is Git Authentication?

GitHub must verify your identity before:

- `git push`
- `git pull`
- `git clone`

Authentication methods:

- HTTPS + Token
- SSH Keys ✅ Recommended

---

## Why SSH?

SSH provides:

- password-less auth
- encrypted communication
- machine-based trust
- faster Git workflow

Example SSH URL:

```bash
git@github.com:user/repo.git
```

---

## SSH Authentication Flow

```text
Your Machine                    GitHub
-------------                  ----------
Private Key  ----challenge---->
              <---verify-------
Public Key   ----------------->
```

### Key Idea

- Private key → stays local
- Public key → uploaded to GitHub
- Matching pair → access granted

!!! note

```
GitHub trusts SSH keys, not passwords.
```

---

## SSH vs HTTPS

| Feature            | HTTPS    | SSH      |
| ------------------ | -------- | -------- |
| Authentication     | Token    | SSH Key  |
| Password prompts   | Frequent | Rare     |
| Setup              | Easy     | One-time |
| Professional usage | Medium   | High     |
| CI/CD friendly     | Yes      | Yes      |

---

## Recommended Modern Setup

| Use Case          | Best Method           |
| ----------------- | --------------------- |
| Personal projects | SSH                   |
| Professional work | SSH                   |
| CI/CD             | Deploy Keys / Secrets |
| APIs              | PAT                   |
| Beginners         | SSH preferred         |

---

# SSH Key Setup

---

## Step 1 — Install Git

### Ubuntu

```bash
sudo apt update
sudo apt install git -y
```

Check version:

```bash
git --version
```

---

## Step 2 — Configure Git Identity

Used in commits.

```bash
git config --global user.name "ashokkumarkola"
git config --global user.email "ashokkumarkola.dev@gmail.com"
```

Verify:

```bash
git config --global --list
```

---

## Step 3 — Generate SSH Key

### Recommended Algorithm

```bash
ssh-keygen -t ed25519 -C "ashokkumarkola.dev@gmail.com"
```

---

## Command Breakdown

| Part         | Meaning                 |
| ------------ | ----------------------- |
| `ssh-keygen` | SSH key generator       |
| `-t ed25519` | modern secure algorithm |
| `-C`         | comment label           |

!!! note

```
Email is only a label, not authentication.
```

---

## Prompts

### Save Location

```text
Enter file in which to save the key:
```

✅ Press `Enter`

Default path:

```text
~/.ssh/id_ed25519
```

---

### Passphrase

```text
Enter passphrase:
```

✅ Optional

- empty → easier setup
- passphrase → extra security

---

## Generated Files

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

| File             | Purpose     |
| ---------------- | ----------- |
| `id_ed25519`     | PRIVATE key |
| `id_ed25519.pub` | PUBLIC key  |

!!! warning

```
Never share private key.
```

---

## Step 4 — Start SSH Agent

```bash
eval "$(ssh-agent -s)"
```

### Purpose

- background SSH process
- stores keys securely in memory

---

## Step 5 — Add Key to SSH Agent

```bash
ssh-add ~/.ssh/id_ed25519
```

Expected:

```text
Identity added: ~/.ssh/id_ed25519
```

---

## Wrong Directory Fix

If keys created outside `~/.ssh`:

```bash
# Create .ssh directory
mkdir -p ~/.ssh

# Move keys
mv id_ed25519 id_ed25519.pub ~/.ssh/

# Fix permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# Add key again
ssh-add ~/.ssh/id_ed25519
```

---

## Step 6 — Copy Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy full output.

---

## Step 7 — Add Key to GitHub

Open:

[GitHub SSH Settings](https://github.com/settings/keys?utm_source=chatgpt.com)

### Add

| Field | Value              |
| ----- | ------------------ |
| Title | Device name        |
| Key   | Paste public key   |
| Type  | Authentication Key |

Save.

---

## Step 8 — Test SSH Connection

```bash
ssh -T git@github.com
```

Expected:

```text
Hi username! You've successfully authenticated.
```

This confirms:

- SSH works
- key valid
- GitHub trusts machine

---

## Step 9 — Clone Using SSH

### Correct

```bash
git clone git@github.com:user/repo.git
```

### Wrong

```text
https://github.com/user/repo.git
```

---

## Step 10 — Push Code

```bash
git push -u origin main
```

Flow:

- SSH sends private key proof
- GitHub checks public key
- push allowed

---

# SSH Files Explained

| File             | Purpose            |
| ---------------- | ------------------ |
| `id_ed25519`     | private key        |
| `id_ed25519.pub` | public key         |
| `known_hosts`    | trusted servers    |
| `config`         | SSH configurations |

---

# SSH Agent

## What is ssh-agent?

Temporary secure key manager.

### Benefits

- avoids repeated auth
- stores keys in memory
- cleaner workflow

---

# SSH Config (Multiple Accounts)

Useful for:

- personal GitHub
- work GitHub

---

## Create Multiple Keys

### Personal

```bash
ssh-keygen -t ed25519 -f ~/.ssh/personal_github
```

### Work

```bash
ssh-keygen -t ed25519 -f ~/.ssh/work_github
```

---

## Configure SSH

```bash
nano ~/.ssh/config
```

Add:

```text
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/personal_github

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/work_github
```

---

## Clone Repositories

### Personal

```bash
git clone git@github-personal:user/repo.git
```

### Work

```bash
git clone git@github-work:company/repo.git
```

---

# HTTPS Authentication (Alternative)

HTTPS uses:

- username
- PAT token

Repository URL:

```text
https://github.com/user/repo.git
```

---

## Generate GitHub Token

Open:

[GitHub Token Settings](https://github.com/settings/tokens?utm_source=chatgpt.com)

Recommended:

- Fine-grained token
- repo permissions only

---

## Clone Using HTTPS

```bash
git clone https://github.com/user/repo.git
```

Git asks:

```text
Username:
Token:
```

---

## Store Credentials

### Store permanently

```bash
git config --global credential.helper store
```

### Temporary cache

```bash
git config --global credential.helper cache
```

---

# Deploy Keys

Deploy keys are SSH keys used by:

- servers
- CI/CD
- deployments

### Common Usage

- VPS pulls private repo
- production deployments
- GitHub Actions

---

# GitHub CLI (`gh`)

Optional GitHub utility.

Install:

```bash
sudo apt install gh
```

Login:

```bash
gh auth login
```

Useful for:

- PRs
- issues
- repo management

---

# gh auth vs SSH

| System    | Purpose        |
| --------- | -------------- |
| `gh auth` | GitHub CLI     |
| SSH Keys  | Git operations |

!!! note

```
Both are independent systems.
```

---

# Security Rules

## NEVER Share

- private keys
- tokens
- `.env`
- API secrets

---

## NEVER Upload

```text
.env
.pem
.key
id_ed25519
credentials.json
```

---

## Add to `.gitignore`

```gitignore
.env
*.pem
*.key
*.p12
```

---

# Common Mistakes

!!! warning

```
Most SSH problems come from wrong permissions or wrong key paths.
```

---

## Frequent Issues

- creating keys outside `~/.ssh`
- wrong permissions
- uploading private keys
- forgetting GitHub public key upload
- mixing HTTPS and SSH URLs
- confusing Git config with auth

---

# Best Practices

## Recommended Workflow

- use SSH for Git
- use PAT only for APIs
- use `.gitignore`
- use separate work/personal keys
- use passphrase in production
- backup SSH keys securely

---

## Production Practices

| Environment        | Common Method |
| ------------------ | ------------- |
| Local dev          | SSH           |
| Company laptops    | SSH + SSO     |
| CI/CD              | secrets       |
| Production servers | deploy keys   |

---

# Quick Commands Cheat Sheet

```bash
# Generate Key
ssh-keygen -t ed25519 -C "email@example.com"

# Start Agent
eval "$(ssh-agent -s)"

# Add Key
ssh-add ~/.ssh/id_ed25519

# Copy Public Key
cat ~/.ssh/id_ed25519.pub

# Test SSH
ssh -T git@github.com

# Clone Repo
git clone git@github.com:user/repo.git

# Push Code
git push -u origin main
```

---

# Summary

- SSH = secure Git authentication
- Public key → GitHub
- Private key → local machine only
- `ssh-agent` manages keys in memory
- SSH preferred for modern development
- Deploy keys used in production
- PAT mainly used for APIs

!!! success

```
SSH authentication is machine-based, secure, fast, and industry standard.
```

Source reference:
