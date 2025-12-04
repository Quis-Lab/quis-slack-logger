"""
Configuration management for Slack Logger.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class Config:
    """Configuration class for Slack Logger."""
    
    # Default settings
    DEFAULT_TIMEOUT = 10  # seconds
    DEFAULT_RETRY_COUNT = 3
    DEFAULT_RETRY_DELAY = 1  # seconds
    
    @staticmethod
    def get_webhook_url(webhook_url: Optional[str] = None) -> Optional[str]:
        """
        Get webhook URL from parameter or environment variable.
        
        Args:
            webhook_url: Optional webhook URL parameter
            
        Returns:
            Webhook URL or None if not found
        """
        if webhook_url:
            return webhook_url
        
        # Try environment variable
        env_url = os.getenv("SLACK_WEBHOOK_URL")
        if env_url:
            return env_url
        
        return None
    
    @staticmethod
    def get_service_name(service_name: Optional[str] = None) -> str:
        """
        Get service name from parameter or environment variable.
        
        Args:
            service_name: Optional service name parameter
            
        Returns:
            Service name or default
        """
        if service_name:
            return service_name
        
        # Try environment variable
        env_name = os.getenv("SLACK_LOGGER_SERVICE_NAME")
        if env_name:
            return env_name
        
        return "unknown-service"
    
    @staticmethod
    def get_timeout() -> int:
        """Get HTTP timeout from environment or use default."""
        return int(os.getenv("SLACK_LOGGER_TIMEOUT", Config.DEFAULT_TIMEOUT))
    
    @staticmethod
    def get_retry_count() -> int:
        """Get retry count from environment or use default."""
        return int(os.getenv("SLACK_LOGGER_RETRY_COUNT", Config.DEFAULT_RETRY_COUNT))
    
    @staticmethod
    def get_retry_delay() -> int:
        """Get retry delay from environment or use default."""
        return int(os.getenv("SLACK_LOGGER_RETRY_DELAY", Config.DEFAULT_RETRY_DELAY))





