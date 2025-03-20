from django.test import TestCase

from users.models import User


class UserModelTests(TestCase):
    def test_employee_id_generation(self):
        user1 = User.objects.create(username='user1', email='user1@example.com')
        self.assertEqual(user1.employee_id, 1)

        user2 = User.objects.create(username='user2', email='user2@example.com')
        self.assertEqual(user2.employee_id, 2)

    def test_employee_id_with_existing_users(self):
        user1 = User.objects.create(username='user1', email='user1@example.com', employee_id=100)
        self.assertEqual(user1.employee_id, 100)

        user2 = User.objects.create(username='user2', email='user2@example.com')
        self.assertEqual(user2.employee_id, 101)

    def test_formatted_employee_id(self):
        user = User.objects.create(username='user1', email='user1@example.com', employee_id=123)
        self.assertEqual(user.formatted_employee_id(), '000123')
