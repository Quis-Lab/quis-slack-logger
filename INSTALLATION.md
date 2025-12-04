# Installation Guide for Using in Other Projects

This guide explains how to install and use the Slack Error Logger package in your other Python projects.

## Quick Start

### Method 1: Install from Local Directory (Recommended for Development)

1. **In your other project**, add to `requirements.txt`:
   ```txt
   -e /absolute/path/to/Quis-Slack-Logger
   ```

2. **Install it**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Use it in your code**:
   ```python
   from slack_logger import SlackLogger
   
   logger = SlackLogger(service_name="my-service")
   logger.error("Something went wrong")
   ```

### Method 2: Install from Git Repository

If you push this package to a Git repository:

1. **Add to requirements.txt**:
   ```txt
   git+https://github.com/yourusername/quis-slack-logger.git
   ```

2. **Install it**:
   ```bash
   pip install -r requirements.txt
   ```

### Method 3: Build and Install Distribution Package

1. **Build the package** (in the Slack Logger directory):
   ```bash
   cd /path/to/Quis-Slack-Logger
   pip install build
   python -m build
   ```

2. **Install in your other project**:
   ```bash
   pip install /path/to/Quis-Slack-Logger/dist/slack_error_logger-1.0.0.tar.gz
   ```

### Method 4: Publish to PyPI (For Production)

1. **Create accounts**:
   - PyPI: https://pypi.org/account/register/
   - TestPyPI: https://test.pypi.org/account/register/

2. **Build the package**:
   ```bash
   pip install build twine
   python -m build
   ```

3. **Upload to TestPyPI first**:
   ```bash
   twine upload --repository testpypi dist/*
   ```

4. **Test installation**:
   ```bash
   pip install -i https://test.pypi.org/simple/ slack-error-logger
   ```

5. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

6. **Install in other projects**:
   ```bash
   pip install slack-error-logger
   ```

## Example: Using in a Flask Project

```python
# app.py
from flask import Flask
from slack_logger import SlackLogger

app = Flask(__name__)
logger = SlackLogger(service_name="flask-api")

@app.route('/api/users')
def get_users():
    try:
        # Your code
        users = fetch_users()
        return {"users": users}
    except Exception as e:
        logger.error("Failed to fetch users", exception=e)
        return {"error": "Internal server error"}, 500
```

## Example: Using in a Django Project

```python
# settings.py
from slack_logger import SlackLogger

SLACK_LOGGER = SlackLogger(service_name="django-backend")

# views.py
from django.conf import settings

def my_view(request):
    try:
        # Your code
        pass
    except Exception as e:
        settings.SLACK_LOGGER.error("View error", exception=e)
```

## Example: Using in a FastAPI Project

```python
# main.py
from fastapi import FastAPI
from slack_logger import SlackLogger

app = FastAPI()
logger = SlackLogger(service_name="fastapi-service")

@app.get("/items")
async def get_items():
    try:
        # Your code
        return {"items": []}
    except Exception as e:
        logger.error("Failed to get items", exception=e)
        raise
```

## Configuration in Other Projects

Set environment variables in your other project:

```bash
# .env file or environment variables
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
export SLACK_LOGGER_SERVICE_NAME="my-service"
```

Or pass directly:

```python
logger = SlackLogger(
    webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
    service_name="my-service"
)
```

## Troubleshooting

### Import Error: No module named 'slack_logger'

Make sure the package is installed:
```bash
pip list | grep slack-error-logger
```

If not found, reinstall:
```bash
pip install -e /path/to/Quis-Slack-Logger
```

### ModuleNotFoundError: No module named 'requests'

Install dependencies:
```bash
pip install requests python-dotenv
```

Or install the package which should include dependencies:
```bash
pip install -e /path/to/Quis-Slack-Logger
```

