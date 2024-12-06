# Shakib's Code

class NotificationSystem:
    def __init__(self, message: str = "", recipient: str = ""):
        """Initialize the notification system with optional default message and recipient."""
        self.message: str = message
        self.recipient: str = recipient
        self.notifications: list[str] = []  # List to store all notifications
    
    def set_notification(self, message: str):
        """Add a custom notification to the list."""
        self.notifications.append(f"Custom: {message}")

    def add_system_notification(self, message: str):
        """Add a system-generated notification to the list."""
        self.notifications.append(f"System: {message}")

    def get_notifications(self) -> list[str]:
        """Retrieve all notifications."""
        return self.notifications

    def clear_notifications(self):
        """Clear all notifications."""
        self.notifications = []

    def send_notification(self) -> str:
        """Send the current notification."""
        return f"Notification sent to {self.recipient}: {self.message}"

    def update_message(self, new_message: str) -> str:
        """Update the message content."""
        self.message = new_message
        return f"Notification message updated to: {self.message}"

    def set_recipient(self, new_recipient: str) -> str:
        """Update the recipient."""
        self.recipient = new_recipient
        return f"Recipient updated to: {self.recipient}"

    def send_reminder(self, event: str, time: str) -> str:
        """Send a reminder for an event."""
        return f"Reminder for {self.recipient}: {event} at {time}."

    def send_payment_notification(self, amount: float, status: str) -> str:
        """Send a payment notification."""
        return f"Payment Notification for {self.recipient}: Payment of ${amount:.2f} was {status}."

    def send_alert(self, alert_type: str, details: str) -> str:
        """Send an alert."""
        return f"ALERT ({alert_type}) for {self.recipient}: {details}"

    def send_update(self, update_type: str, content: str) -> str:
        """Send an update."""
        return f"UPDATE ({update_type}) for {self.recipient}: {content}"

