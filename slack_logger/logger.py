"""
Main Slack Logger class for error logging.
"""

import logging
from typing import Optional, Dict, Any
from .config import Config
from .client import SlackWebhookClient
from .formatter import SlackMessageFormatter, LogLevel

logger = logging.getLogger(__name__)


class SlackLogger:
    """
    Slack Logger for centralized error logging across multiple services.
    
    Usage:
        logger = SlackLogger(webhook_url="...", service_name="my-service")
        logger.error("Something went wrong", exception=e)
    """
    
    def __init__(
        self,
        webhook_url: Optional[str] = None,
        service_name: Optional[str] = None,
        timeout: Optional[int] = None
    ):
        """
        Initialize the Slack Logger.
        
        Args:
            webhook_url: Slack incoming webhook URL. If not provided, will try
                        to get from SLACK_WEBHOOK_URL environment variable.
            service_name: Name of the service using this logger. If not provided,
                         will try to get from SLACK_LOGGER_SERVICE_NAME environment
                         variable, or default to "unknown-service".
            timeout: HTTP request timeout in seconds. Defaults to 10.
        
        Raises:
            ValueError: If webhook_url is not provided and not found in environment.
        """
        self.webhook_url = Config.get_webhook_url(webhook_url)
        if not self.webhook_url:
            raise ValueError(
                "webhook_url must be provided either as parameter or "
                "SLACK_WEBHOOK_URL environment variable"
            )
        
        self.service_name = Config.get_service_name(service_name)
        self.client = SlackWebhookClient(self.webhook_url, timeout=timeout)
    
    def _log(
        self,
        message: str,
        level: LogLevel,
        exception: Optional[Exception] = None,
        additional_context: Optional[Dict[str, Any]] = None,
        async_send: bool = False
    ) -> bool:
        """
        Internal method to log a message.
        
        Args:
            message: The message to log
            level: Log level
            exception: Optional exception object
            additional_context: Optional dictionary with additional context
            async_send: If True, send asynchronously (fire and forget)
            
        Returns:
            True if sent successfully, False otherwise
        """
        try:
            payload = SlackMessageFormatter.format_message(
                message=message,
                level=level,
                service_name=self.service_name,
                exception=exception,
                additional_context=additional_context
            )
            
            if async_send:
                self.client.send_async(payload)
                return True
            else:
                return self.client.send(payload)
        except Exception as e:
            # Prevent logging errors from breaking the application
            logger.error(f"Failed to send log to Slack: {e}", exc_info=True)
            return False
    
    def info(
        self,
        message: str,
        additional_context: Optional[Dict[str, Any]] = None,
        async_send: bool = False
    ) -> bool:
        """
        Log an info message.
        
        Args:
            message: The message to log
            additional_context: Optional dictionary with additional context
            async_send: If True, send asynchronously (fire and forget)
            
        Returns:
            True if sent successfully, False otherwise
        """
        return self._log(
            message=message,
            level=LogLevel.INFO,
            exception=None,
            additional_context=additional_context,
            async_send=async_send
        )
    
    def warning(
        self,
        message: str,
        exception: Optional[Exception] = None,
        additional_context: Optional[Dict[str, Any]] = None,
        async_send: bool = False
    ) -> bool:
        """
        Log a warning message.
        
        Args:
            message: The message to log
            exception: Optional exception object
            additional_context: Optional dictionary with additional context
            async_send: If True, send asynchronously (fire and forget)
            
        Returns:
            True if sent successfully, False otherwise
        """
        return self._log(
            message=message,
            level=LogLevel.WARNING,
            exception=exception,
            additional_context=additional_context,
            async_send=async_send
        )
    
    def error(
        self,
        message: str,
        exception: Optional[Exception] = None,
        additional_context: Optional[Dict[str, Any]] = None,
        async_send: bool = False
    ) -> bool:
        """
        Log an error message.
        
        Args:
            message: The message to log
            exception: Optional exception object
            additional_context: Optional dictionary with additional context
            async_send: If True, send asynchronously (fire and forget)
            
        Returns:
            True if sent successfully, False otherwise
        """
        return self._log(
            message=message,
            level=LogLevel.ERROR,
            exception=exception,
            additional_context=additional_context,
            async_send=async_send
        )
    
    def critical(
        self,
        message: str,
        exception: Optional[Exception] = None,
        additional_context: Optional[Dict[str, Any]] = None,
        async_send: bool = False
    ) -> bool:
        """
        Log a critical message.
        
        Args:
            message: The message to log
            exception: Optional exception object
            additional_context: Optional dictionary with additional context
            async_send: If True, send asynchronously (fire and forget)
            
        Returns:
            True if sent successfully, False otherwise
        """
        return self._log(
            message=message,
            level=LogLevel.CRITICAL,
            exception=exception,
            additional_context=additional_context,
            async_send=async_send
        )
    
    def log_exception(
        self,
        message: str,
        exception: Exception,
        additional_context: Optional[Dict[str, Any]] = None,
        async_send: bool = False
    ) -> bool:
        """
        Convenience method to log an exception as an error.
        
        Args:
            message: The message to log
            exception: The exception object
            additional_context: Optional dictionary with additional context
            async_send: If True, send asynchronously (fire and forget)
            
        Returns:
            True if sent successfully, False otherwise
        """
        return self.error(
            message=message,
            exception=exception,
            additional_context=additional_context,
            async_send=async_send
        )





