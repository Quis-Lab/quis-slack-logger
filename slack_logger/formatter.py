"""
Formatter for creating rich Slack messages with blocks API.
"""

import json
import traceback
from datetime import datetime
from typing import Optional, Dict, Any
from enum import Enum


class LogLevel(Enum):
    """Log level enumeration."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class SlackMessageFormatter:
    """Formatter for creating Slack message blocks."""
    
    # Color mapping for different log levels
    COLOR_MAP = {
        LogLevel.INFO: "#36a64f",      # Green
        LogLevel.WARNING: "#ffa500",   # Orange
        LogLevel.ERROR: "#ff0000",     # Red
        LogLevel.CRITICAL: "#8b0000",  # Dark Red
    }
    
    # Emoji mapping for different log levels
    EMOJI_MAP = {
        LogLevel.INFO: "ℹ️",
        LogLevel.WARNING: "⚠️",
        LogLevel.ERROR: "❌",
        LogLevel.CRITICAL: "🚨",
    }
    
    @staticmethod
    def format_message(
        message: str,
        level: LogLevel,
        service_name: str,
        exception: Optional[Exception] = None,
        additional_context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Format a message into Slack blocks format.
        
        Args:
            message: The main error/message text
            level: Log level
            service_name: Name of the service sending the log
            exception: Optional exception object
            additional_context: Optional dictionary with additional context
            
        Returns:
            Slack message payload with blocks
        """
        timestamp = datetime.utcnow().isoformat()
        color = SlackMessageFormatter.COLOR_MAP.get(level, "#808080")
        emoji = SlackMessageFormatter.EMOJI_MAP.get(level, "📝")
        
        blocks = []
        
        # Header block with color bar
        blocks.append({
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"{emoji} {level.value.upper()}: {service_name}"
            }
        })
        
        # Divider
        blocks.append({"type": "divider"})
        
        # Main message block
        message_text = f"*Message:*\n{message}"
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message_text
            }
        })
        
        # Exception details if provided
        if exception:
            exception_type = type(exception).__name__
            exception_message = str(exception)
            
            # Stack trace
            stack_trace = "".join(traceback.format_exception(
                type(exception),
                exception,
                exception.__traceback__
            ))
            
            # Truncate stack trace if too long (Slack has message limits)
            max_stack_length = 3000
            if len(stack_trace) > max_stack_length:
                stack_trace = stack_trace[:max_stack_length] + "\n... (truncated)"
            
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Exception Type:* `{exception_type}`\n*Exception Message:* `{exception_message}`"
                }
            })
            
            # Stack trace in code block
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Stack Trace:*\n```{stack_trace}```"
                }
            })
        
        # Additional context if provided
        if additional_context:
            context_text = "*Additional Context:*\n"
            for key, value in additional_context.items():
                # Format value appropriately
                if isinstance(value, (dict, list)):
                    value_str = json.dumps(value, indent=2)
                else:
                    value_str = str(value)
                
                context_text += f"• *{key}:* `{value_str}`\n"
            
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": context_text
                }
            })
        
        # Timestamp footer
        blocks.append({
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"🕐 {timestamp} UTC"
                }
            ]
        })
        
        # Return payload with blocks
        payload = {
            "blocks": blocks
        }
        
        # Add fallback text for notifications
        fallback_text = f"{level.value.upper()}: {message}"
        if exception:
            fallback_text += f" ({type(exception).__name__})"
        payload["text"] = fallback_text
        
        return payload
    
    @staticmethod
    def format_simple_message(
        message: str,
        level: LogLevel,
        service_name: str
    ) -> Dict[str, Any]:
        """
        Format a simple message without exception details.
        
        Args:
            message: The message text
            level: Log level
            service_name: Name of the service
            
        Returns:
            Slack message payload
        """
        return SlackMessageFormatter.format_message(
            message=message,
            level=level,
            service_name=service_name,
            exception=None,
            additional_context=None
        )

