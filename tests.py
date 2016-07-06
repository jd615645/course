from django.test import TestCase
from apps.course.models import Course_of_user, Course
from django.utils import timezone # auto generate create time.

# Create your tests here.
class book_of_courseTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        To ensure courseID and name of course are not None or ""
        """

        self.assertEqual(check_courseID_and_name_not_empty(), True)