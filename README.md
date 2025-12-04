# Slack Error Logger

A Python library for centralized error logging to Slack via Incoming Webhooks. Perfect for multi-service architectures where you want all errors logged to a single Slack channel.

## Quick Start (GitHub Teams)

```bash
# 1. Push this package to GitHub
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/quis-slack-logger.git
git push -u origin main

# 2. In your other project's requirements.txt:
#    git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0

# 3. Install and use
pip install -r requirements.txt
```

```python
from slack_logger import SlackLogger
logger = SlackLogger(service_name="my-service")
logger.error("Something went wrong", exception=e)
```

📖 **Full team setup guide: [TEAM_SETUP.md](TEAM_SETUP.md)**

## Features

- 🎯 **Multiple Log Levels**: INFO, WARNING, ERROR, CRITICAL
- 📊 **Rich Formatting**: Beautiful Slack messages with blocks API
- 🔍 **Stack Traces**: Automatic stack trace capture and formatting
- 🏷️ **Service Tagging**: Identify which service generated each log
- ⚡ **Async Support**: Fire-and-forget logging option
- 🔧 **Easy Configuration**: Environment variables or direct parameters
- 🛡️ **Error Handling**: Prevents logging failures from breaking your app
- 🔄 **Retry Logic**: Automatic retries with configurable delays

## Installation

### For GitHub Teams (Recommended)

If your projects are on GitHub and you're working with a team:

1. **Push this package to GitHub** (see [TEAM_SETUP.md](TEAM_SETUP.md) for details)
2. **Add to your project's `requirements.txt`**:
   ```txt
   git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0
   ```
3. **Install**: `pip install -r requirements.txt`

Team members will automatically get the package when they install dependencies!

See [TEAM_SETUP.md](TEAM_SETUP.md) for complete team collaboration guide.

---

### Option 1: Install from Local Directory (Development)

If you have the package locally and want to use it in other projects:

```bash
# Navigate to the package directory
cd /path/to/Quis-Slack-Logger

# Install in editable mode (changes reflect immediately)
pip install -e .

# Or install normally
pip install .
```

### Option 2: Install from Git Repository

If the package is in a Git repository:

```bash
# Install directly from Git
pip install git+https://github.com/yourusername/quis-slack-logger.git

# Or for a specific branch/tag
pip install git+https://github.com/yourusername/quis-slack-logger.git@main
```

### Option 3: Install from Local Path in Other Projects

In your other project, you can install it directly from the local path:

```bash
# From your other project directory
pip install /path/to/Quis-Slack-Logger

# Or use relative path
pip install ../Quis-Slack-Logger
```

### Option 4: Add to requirements.txt in Other Projects

Add this line to your other project's `requirements.txt`:

```txt
# For local development
-e /path/to/Quis-Slack-Logger

# Or from Git
git+https://github.com/yourusername/quis-slack-logger.git

# Or if published to PyPI (see Publishing section below)
slack-error-logger>=1.0.0
```

### Option 5: Build and Install Distribution Package

Build a distribution package and install it:

```bash
# Build the package
cd /path/to/Quis-Slack-Logger
pip install build
python -m build

# This creates dist/slack_error_logger-1.0.0.tar.gz
# Install it in other projects:
pip install dist/slack_error_logger-1.0.0.tar.gz
```

### Publishing to PyPI (Optional)

If you want to publish to PyPI for easy installation:

```bash
# Install build and twine
pip install build twine

# Build the package
python -m build

# Upload to PyPI (requires PyPI account)
twine upload dist/*

# Then others can install with:
pip install slack-error-logger
```

## Setup

### 1. Create a Slack Incoming Webhook

1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Create a new app or select an existing one
3. Navigate to "Incoming Webhooks"
4. Activate Incoming Webhooks
5. Click "Add New Webhook to Workspace"
6. Select the channel where you want to receive logs
7. Copy the webhook URL

### 2. Configure the Logger

You can configure the logger in two ways:

#### Option A: Environment Variables (Recommended)

Create a `.env` file or set environment variables:

```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
export SLACK_LOGGER_SERVICE_NAME="my-service"
export SLACK_LOGGER_TIMEOUT=10
export SLACK_LOGGER_RETRY_COUNT=3
export SLACK_LOGGER_RETRY_DELAY=1
```

#### Option B: Direct Parameters

Pass configuration directly when initializing the logger.

## Using in Other Projects

### Quick Setup for GitHub Teams

1. **Push this package to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/quis-slack-logger.git
   git push -u origin main
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```

2. **In your other project's `requirements.txt`**:
   ```txt
   git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0
   ```

3. **Install and use**:
   ```bash
   pip install -r requirements.txt
   ```
   ```python
   from slack_logger import SlackLogger
   logger = SlackLogger(service_name="my-service")
   logger.error("Something went wrong", exception=e)
   ```

**That's it!** Team members just need to run `pip install -r requirements.txt` and they'll get the package automatically.

📖 **See [TEAM_SETUP.md](TEAM_SETUP.md) for complete team collaboration guide.**

### Adding to Your Project's requirements.txt

```txt
# For GitHub teams (recommended)
git+https://github.com/yourusername/quis-slack-logger.git@v1.0.0

# Or use latest from main branch
git+https://github.com/yourusername/quis-slack-logger.git@main

# For local development
-e /absolute/path/to/Quis-Slack-Logger

# If published to PyPI
slack-error-logger>=1.0.0
```

## Usage

### Basic Usage

```python
from slack_logger import SlackLogger

# Initialize logger
logger = SlackLogger(
    webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
    service_name="my-service"
)

# Log different levels
logger.info("Service started successfully")
logger.warning("High memory usage detected")
logger.error("Failed to process request")
logger.critical("Database connection lost")
```

### Logging Exceptions

```python
try:
    # Your code here
    result = risky_operation()
except Exception as e:
    logger.error("Failed to execute risky operation", exception=e)
    # or use the convenience method
    logger.log_exception("Failed to execute risky operation", e)
```

### Adding Additional Context

```python
logger.error(
    "Payment processing failed",
    exception=e,
    additional_context={
        "user_id": 12345,
        "order_id": "ORD-789",
        "amount": 99.99,
        "payment_method": "credit_card"
    }
)
```

### Async Logging (Fire and Forget)

For non-blocking logging, use `async_send=True`:

```python
logger.error(
    "Non-critical error occurred",
    exception=e,
    async_send=True  # Won't block execution
)
```

### Using Environment Variables

```python
from slack_logger import SlackLogger

# Will automatically use SLACK_WEBHOOK_URL and SLACK_LOGGER_SERVICE_NAME
# from environment variables
logger = SlackLogger()
```

## Examples

### Example 1: Flask Application

```python
from flask import Flask
from slack_logger import SlackLogger

app = Flask(__name__)
logger = SlackLogger(service_name="flask-api")

@app.route('/api/users')
def get_users():
    try:
        # Your code here
        users = fetch_users_from_db()
        return {"users": users}
    except Exception as e:
        logger.error("Failed to fetch users", exception=e)
        return {"error": "Internal server error"}, 500
```

### Example 2: Django Application

```python
# settings.py
from slack_logger import SlackLogger

SLACK_LOGGER = SlackLogger(service_name="django-backend")

# views.py
from django.conf import settings

def my_view(request):
    try:
        # Your code here
        pass
    except Exception as e:
        settings.SLACK_LOGGER.error("View error", exception=e)
```

### Example 3: Background Task

```python
from slack_logger import SlackLogger

logger = SlackLogger(service_name="background-worker")

def process_queue():
    while True:
        try:
            item = queue.get()
            process_item(item)
        except Exception as e:
            # Use async to avoid blocking the queue processing
            logger.error(
                "Error processing queue item",
                exception=e,
                additional_context={"item_id": item.id},
                async_send=True
            )
```

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SLACK_WEBHOOK_URL` | Slack incoming webhook URL | Required |
| `SLACK_LOGGER_SERVICE_NAME` | Name of your service | `unknown-service` |
| `SLACK_LOGGER_TIMEOUT` | HTTP request timeout (seconds) | `10` |
| `SLACK_LOGGER_RETRY_COUNT` | Number of retry attempts | `3` |
| `SLACK_LOGGER_RETRY_DELAY` | Delay between retries (seconds) | `1` |

### Constructor Parameters

```python
SlackLogger(
    webhook_url=None,      # Optional if set in env
    service_name=None,     # Optional if set in env
    timeout=None           # Optional, defaults to 10
)
```

## Message Format

Messages are sent to Slack using the Blocks API with:

- **Header**: Log level and service name with emoji
- **Message**: Main error/message text
- **Exception Details**: Exception type and message (if provided)
- **Stack Trace**: Full stack trace in code block (if exception provided)
- **Additional Context**: Key-value pairs (if provided)
- **Timestamp**: UTC timestamp

## Error Handling

The logger is designed to never break your application:

- All exceptions in the logger are caught and logged internally
- Failed webhook requests are retried automatically
- If all retries fail, the logger silently fails (logs to Python logger)
- Use `async_send=True` for fire-and-forget logging

## Requirements

- Python 3.7+
- `requests` library
- `python-dotenv` library (for environment variable support)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.





