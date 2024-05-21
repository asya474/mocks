class NotificationService:
    def send_notification(self, user_id, message):
        pass

class Order:
    def __init__(self, user_id, product_name):
        self.user_id=user_id
        self.product_name=product_name
        self.notification_service=NotificationService()

    def process_order(self):
        message=f"Your order of {self.product_name} has been processed"
        self.notification_service.send_notification(self.user_id, message)
