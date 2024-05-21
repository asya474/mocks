import unittest
from unittest.mock import Mock
from order import Order, NotificationService

class TestOrder(unittest.TestCase):
    def test_process_order(self):
        mock_notification_service=Mock(spec_set=NotificationService)
        order=Order(user_id=123, product_name="Product")
        order.notification_service=mock_notification_service

        order.process_order()

        mock_notification_service.send_notification.assert_called_once_with(123,
        "Your order of Product has been processed")

        print("Test passed successfully")

    def test_process_order_different_product(self):
        mock_notification_service=Mock(spec_set=NotificationService)
        order=Order(user_id=456, product_name="Another Product")
        order.notification_service=mock_notification_service

        order.process_order()

        mock_notification_service.send_notification.assert_called_once_with(
            456, "Your order of Another Product has been processed"
        )

        print("Test passed successfully")

    def test_process_order_empty_product_name(self):
        mock_notification_service=Mock(spec_set=NotificationService)
        order=Order(user_id=789, product_name="")
        order.notification_service=mock_notification_service

        order.process_order()

        mock_notification_service.send_notification.assert_called_once_with(
            789, "Your order for  has been processed"
        )

        print("Test passed successfully")

if __name__=='__main__':
    unittest.main()

