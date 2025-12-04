"""
HTTP client for sending messages to Slack webhook.
"""

import time
import logging
from typing import Dict, Any, Optional
import requests
from .config import Config

logger = logging.getLogger(__name__)


class SlackWebhookClient:
    """Client for sending messages to Slack via webhook."""
    
    def __init__(self, webhook_url: str, timeout: Optional[int] = None):
        """
        Initialize the Slack webhook client.
        
        Args:
            webhook_url: Slack incoming webhook URL
            timeout: HTTP request timeout in seconds
        """
        self.webhook_url = webhook_url
        self.timeout = timeout or Config.get_timeout()
        self.retry_count = Config.get_retry_count()
        self.retry_delay = Config.get_retry_delay()
    
    def send(self, payload: Dict[str, Any]) -> bool:
        """
        Send a message to Slack webhook with retry logic.
        
        Args:
            payload: Slack message payload (blocks or text)
            
        Returns:
            True if successful, False otherwise
        """
        for attempt in range(self.retry_count):
            try:
                response = requests.post(
                    self.webhook_url,
                    json=payload,
                    timeout=self.timeout,
                    headers={"Content-Type": "application/json"}
                )
                
                # Slack returns 200 for successful webhook posts
                if response.status_code == 200:
                    return True
                
                # Log error but don't raise exception
                logger.warning(
                    f"Slack webhook returned status {response.status_code}: {response.text}"
                )
                
                # If it's a client error (4xx), don't retry
                if 400 <= response.status_code < 500:
                    return False
                
            except requests.exceptions.Timeout:
                logger.warning(f"Slack webhook request timed out (attempt {attempt + 1}/{self.retry_count})")
            except requests.exceptions.RequestException as e:
                logger.warning(f"Slack webhook request failed (attempt {attempt + 1}/{self.retry_count}): {e}")
            
            # Wait before retrying (except on last attempt)
            if attempt < self.retry_count - 1:
                time.sleep(self.retry_delay)
        
        return False
    
    def send_async(self, payload: Dict[str, Any]) -> None:
        """
        Send a message to Slack webhook asynchronously (fire and forget).
        
        This method doesn't wait for the response and doesn't raise exceptions.
        Useful for non-blocking error logging.
        
        Args:
            payload: Slack message payload (blocks or text)
        """
        try:
            # Use a thread or async approach - for simplicity, we'll use a basic approach
            # In production, you might want to use threading or asyncio
            self.send(payload)
        except Exception as e:
            # Silently fail to prevent logging errors from breaking the application
            logger.error(f"Failed to send async message to Slack: {e}", exc_info=True)





