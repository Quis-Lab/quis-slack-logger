# Slack Error Logger

A Python library for centralized error logging to Slack via Incoming Webhooks. Perfect for multi-service architectures where you want all errors logged to a single Slack channel.

## Quick Start

Add to your project's `requirements.txt`:

```txt
git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.0.0
```

Install:

```bash
pip install -r requirements.txt
```

Use in your code:

```python
from slack_logger import SlackLogger
logger = SlackLogger(service_name="my-service")
logger.error("Something went wrong", exception=e)
```

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

Add this line to your project's `requirements.txt`:

```txt
git+https://github.com/Quis-Lab/quis-slack-logger.git@v1.0.0
```

Then install:

```bash
pip install -r requirements.txt
```

That's it! The package will be automatically installed from GitHub when you or your team members run `pip install -r requirements.txt`.

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





