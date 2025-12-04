# Team Setup Guide - Using Slack Logger in GitHub Projects

This guide explains how to use the Slack Error Logger package in your projects when working with a team.

## Installation

### Add to requirements.txt

In your project's `requirements.txt`, add this line:

```txt
git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.0.0
```

### Install

```bash
pip install -r requirements.txt
```

That's it! The package will be automatically installed from GitHub.

## Usage

```python
from slack_logger import SlackLogger

logger = SlackLogger(service_name="my-service")
logger.error("Something went wrong", exception=e)
```

## For Team Members

When team members clone your project:

```bash
git clone https://github.com/yourusername/your-project.git
cd your-project
pip install -r requirements.txt
```

The Slack logger will be automatically installed from GitHub!

## Version Management

### Using Specific Versions (Recommended)

For production, use a specific version tag:

```txt
git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.0.0
```

### Updating to a New Version

When a new version is released:

1. **Update requirements.txt**:
   ```txt
   git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.1.0
   ```

2. **Update installation**:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

## Example Project Structure

### Your Project's requirements.txt

```txt
Flask==2.3.0
git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.0.0
```

## Troubleshooting

### "Could not find a version that satisfies the requirement"

**Solution**: 
- Make sure the repository URL is correct: `https://github.com/Quis-Lab/quis-slack-logger.git`
- Verify the version tag exists (e.g., `v1.0.0`)
- Ensure you have access to the repository (if it's private)

### "Permission denied" for private repos

**Solution**: 
- Ensure team members have GitHub access to the repository
- Make sure Git credentials are configured

### Team members can't install

**Solution**: 
- Verify they have access to the Quis-Lab organization
- Try: `pip install --upgrade pip setuptools wheel`
- Check Git is installed: `git --version`

## Best Practices

1. **Use version tags** (e.g., `@v1.0.0`) instead of branches in production
2. **Pin specific versions** in requirements.txt for stability
3. **Update versions** in a controlled manner
4. **Test new versions** before updating production projects

## Quick Reference

```txt
# In requirements.txt
git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.0.0
```

```bash
# Install
pip install -r requirements.txt
```

```python
# Use in code
from slack_logger import SlackLogger
logger = SlackLogger(service_name="my-service")
```
