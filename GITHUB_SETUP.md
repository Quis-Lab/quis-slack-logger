# Quick GitHub Setup Guide

Follow these steps to push your Slack Logger package to GitHub.

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository name: `quis-slack-logger` (or your preferred name)
4. Description: "A Python library for centralized error logging to Slack via webhooks"
5. Choose **Public** (or Private if you prefer, but team members need access)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click **"Create repository"**

## Step 2: Push to GitHub

### Option A: Use the Setup Script (Easiest)

```bash
./setup-github.sh
```

The script will ask for your GitHub username and repository name, then push everything.

### Option B: Manual Commands

```bash
# Add remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/quis-slack-logger.git

# Push code
git push -u origin main

# Create and push version tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Step 3: Verify

1. Go to your GitHub repository page
2. You should see all your files
3. Check the "Releases" section - you should see v1.0.0 tag

## Step 4: Use in Other Projects

In your other projects' `requirements.txt`:

```txt
git+https://github.com/YOUR_USERNAME/quis-slack-logger.git@v1.0.0
```

Then install:
```bash
pip install -r requirements.txt
```

## Troubleshooting

### "Repository not found"
- Make sure you created the repository on GitHub first
- Check the repository name and username are correct
- If private repo, make sure you're authenticated

### "Permission denied"
- You may need to authenticate. Try:
  ```bash
  gh auth login  # If you have GitHub CLI
  ```
  Or use SSH:
  ```bash
  git remote set-url origin git@github.com:YOUR_USERNAME/quis-slack-logger.git
  ```

### "Remote origin already exists"
- Check existing remote: `git remote -v`
- Update it: `git remote set-url origin NEW_URL`
- Or remove and re-add: `git remote remove origin`

