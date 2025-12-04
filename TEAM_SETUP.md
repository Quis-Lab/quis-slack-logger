# Team Setup Guide - Using Slack Logger in GitHub Projects

This guide explains how to use the Slack Error Logger package when your projects are on GitHub and you're collaborating with other developers.

## Step 1: Push the Package to GitHub

### 1.1 Initialize Git Repository (if not already done)

```bash
cd /path/to/Quis-Slack-Logger
git init
git add .
git commit -m "Initial commit: Slack Error Logger package"
```

### 1.2 Create GitHub Repository

1. Go to GitHub and create a new repository (e.g., `quis-slack-logger`)
2. **Important**: Make it a **public** repository (or ensure team members have access if private)

### 1.3 Push to GitHub

```bash
git remote add origin https://github.com/yourusername/quis-slack-logger.git
git branch -M main
git push -u origin main
```

### 1.4 Create Version Tags (Recommended)

For stable releases, create git tags:

```bash
# Tag the current version
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# For future versions
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.1.0
```

## Step 2: Use in Your Other GitHub Projects

### 2.1 Add to requirements.txt

In each of your other projects, add this line to `requirements.txt`:

```txt
# Install from GitHub repository
git+https://github.com/yourusername/quis-slack-logger.git@main

# Or use a specific version tag (recommended for production)
git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0
```

### 2.2 Install in Your Project

```bash
# In your other project directory
pip install -r requirements.txt
```

### 2.3 Use in Your Code

```python
from slack_logger import SlackLogger

logger = SlackLogger(service_name="my-service")
logger.error("Something went wrong")
```

## Step 3: Team Member Setup

### 3.1 For New Team Members

When a new team member clones your project:

```bash
# Clone your project
git clone https://github.com/yourusername/your-project.git
cd your-project

# Install dependencies (this will automatically install slack-logger from GitHub)
pip install -r requirements.txt
```

That's it! The `requirements.txt` will automatically pull the Slack logger from GitHub.

### 3.2 If Using Private Repository

If your Slack logger repository is private, team members need:

1. **GitHub access** to the repository
2. **Git credentials** configured (or use SSH):

```txt
# Use SSH instead of HTTPS
git+ssh://git@github.com/yourusername/quis-slack-logger.git@main
```

Or configure Git to use SSH:
```bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

## Step 4: Version Management

### 4.1 Using Specific Versions (Recommended)

For production projects, pin to specific versions:

```txt
# requirements.txt
git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0
```

### 4.2 Using Latest from Branch

For development, use the latest from a branch:

```txt
# requirements.txt
git+https://github.com/yourusername/quis-slack-logger.git@main
```

### 4.3 Updating Versions

When you release a new version:

1. **Update version** in `slack_logger/__init__.py` and `pyproject.toml`
2. **Create a new tag**:
   ```bash
   git tag -a v1.1.0 -m "Release version 1.1.0"
   git push origin v1.1.0
   ```
3. **Update requirements.txt** in your projects:
   ```txt
   git+https://github.com/yourusername/quis-slack-logger.git@v1.1.0
   ```
4. **Team members update**:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

## Step 5: Example Project Structure

### Your Slack Logger Repository
```
quis-slack-logger/
├── slack_logger/
│   ├── __init__.py
│   ├── logger.py
│   ├── config.py
│   ├── client.py
│   └── formatter.py
├── pyproject.toml
├── setup.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Your Other Project (e.g., Flask API)
```
my-flask-api/
├── app/
│   └── main.py
├── requirements.txt  ← Contains: git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0
└── README.md
```

### requirements.txt in Your Other Project
```txt
Flask==2.3.0
slack-error-logger @ git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0
```

## Step 6: CI/CD Integration

### GitHub Actions Example

If you use GitHub Actions, the package will be installed automatically:

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          # This will automatically install slack-logger from GitHub
      
      - name: Run tests
        run: pytest
```

## Step 7: Troubleshooting

### Issue: "Could not find a version that satisfies the requirement"

**Solution**: Make sure:
- The repository URL is correct
- The repository is public (or team members have access)
- The branch/tag exists

### Issue: "Permission denied" for private repos

**Solution**: 
- Use SSH URLs: `git+ssh://git@github.com/...`
- Or ensure GitHub credentials are configured

### Issue: Team members can't install

**Solution**: 
- Verify they have access to the repository
- Check if they need to install Git: `pip install gitpython` (usually not needed)
- Try: `pip install --upgrade pip setuptools wheel`

## Best Practices

1. **Use version tags** instead of branches in production
2. **Keep the package repository separate** from your application repositories
3. **Document version changes** in your project's CHANGELOG
4. **Test new versions** in a development branch before updating production
5. **Use semantic versioning** (v1.0.0, v1.1.0, v2.0.0)

## Quick Reference

```bash
# Install in any project
pip install git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0

# Update to latest
pip install git+https://github.com/yourusername/quis-slack-logger.git@main --upgrade

# Use in code
from slack_logger import SlackLogger
logger = SlackLogger(service_name="my-service")
```

