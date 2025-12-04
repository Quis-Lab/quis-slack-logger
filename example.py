"""
Example usage of Slack Error Logger.

Before running this example:
1. Set up a Slack Incoming Webhook
2. Set the SLACK_WEBHOOK_URL environment variable or pass it directly
"""

from slack_logger import SlackLogger

# Initialize the logger
# Option 1: Using environment variables
# Set SLACK_WEBHOOK_URL and SLACK_LOGGER_SERVICE_NAME in your environment
logger = SlackLogger(service_name="example-service")

# Option 2: Pass webhook URL directly
# logger = SlackLogger(
#     webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
#     service_name="example-service"
# )


def example_basic_logging():
    """Example of basic logging at different levels."""
    logger.info("Service started successfully")
    logger.warning("High memory usage detected: 85%")
    logger.error("Failed to connect to database")
    logger.critical("System is down!")


def example_exception_logging():
    """Example of logging exceptions."""
    try:
        # Simulate an error
        result = 1 / 0
    except ZeroDivisionError as e:
        logger.error("Division by zero error", exception=e)
        # Or use the convenience method
        logger.log_exception("Division by zero error", e)


def example_with_context():
    """Example of logging with additional context."""
    try:
        # Simulate processing a user request
        user_id = 12345
        order_id = "ORD-789"
        amount = 99.99
        
        # Simulate an error
        raise ValueError("Payment gateway timeout")
    except Exception as e:
        logger.error(
            "Payment processing failed",
            exception=e,
            additional_context={
                "user_id": user_id,
                "order_id": order_id,
                "amount": amount,
                "payment_method": "credit_card",
                "retry_count": 3
            }
        )


def example_async_logging():
    """Example of async (non-blocking) logging."""
    try:
        # Some operation that might fail
        raise ConnectionError("Network timeout")
    except Exception as e:
        # Use async_send=True for fire-and-forget logging
        # This won't block your application
        logger.error(
            "Non-critical error occurred",
            exception=e,
            async_send=True
        )
        print("Application continues without waiting for Slack response")


if __name__ == "__main__":
    print("Slack Logger Examples")
    print("=" * 50)
    
    # Uncomment the examples you want to run:
    # example_basic_logging()
    # example_exception_logging()
    # example_with_context()
    # example_async_logging()
    
    print("\nNote: Make sure to set SLACK_WEBHOOK_URL before running examples!")





