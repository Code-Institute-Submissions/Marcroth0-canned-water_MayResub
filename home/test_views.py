from django.test import TestCase


class TestIndexViews(TestCase):

    def test_get_index(self):
        """
        Check the response status and
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateNotUsed(response, 'bag/bag.html')
