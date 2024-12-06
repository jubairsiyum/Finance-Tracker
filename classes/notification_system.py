# Shakib's Code

class NotificationSystem:
    def __init__(self, message: str, recipient: str):
        """Initialize the notification with a message and recipient."""
        self.message: str = message
        self.recipient: str = recipient
        self.notifications: list[str] = []  # List to store notifications
    
    def set_notification(self, message: str):
        """Add a notification to the list."""
        self.notifications.append(message)

    def send_notification(self) -> str:
        """Send the notification."""
        return f"Notification sent to {self.recipient}: {self.message}"

    def update_message(self, new_message: str) -> str:
        """Update the message content."""
        self.message = new_message
        return f"Notification message updated to: {self.message}"

    def set_recipient(self, new_recipient: str) -> str:
        """Update the recipient."""
        self.recipient = new_recipient
        return f"Recipient updated to: {self.recipient}"

    def get_details(self) -> str:
        """Return notification details."""
        return f"Recipient: {self.recipient}, Message: {self.message}"

    # Additional Methods

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
