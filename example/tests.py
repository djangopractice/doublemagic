from django.test import TestCase
from unittest.mock import patch, MagicMock
from example.models import Example


class ExampleTestCase(TestCase):
    def setUp(self):
        self.example = Example.objects.create(name='Example 1', description='The first example')

    def test_example_exists(self):
        self.assertEqual(self.example.description, 'The first example')

    @patch('example.models.request')
    def test_get_page(self, req):
        url = MagicMock()
        self.example._get_page(url)
        req.assert_called_once_with('GET', url)

    @patch('example.models.Example._get_page')
    def test_name_in_page_calls_get_page(self, getpage):
        url = MagicMock()
        self.example.name_in_page(url)
        getpage.assert_called_once_with(url)

    @patch('example.models.Example._get_page')
    def test_name_in_page(self, getpage):
        resp = MagicMock()
        resp.content = 'Text that contains {} in it'.format(self.example.name)
        getpage.return_value = resp
        self.assertTrue(self.example.name_in_page(MagicMock()))

    @patch('example.models.Example._get_page')
    def test_name_in_page_not(self, getpage):
        resp = MagicMock()
        resp.content = 'Text that does not contain the name'
        getpage.return_value = resp
        self.assertFalse(self.example.name_in_page(MagicMock()))
