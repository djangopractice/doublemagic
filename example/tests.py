from django.test import TestCase
from unittest.mock import patch, MagicMock
from example.models import Example


class ExampleTestCase(TestCase):
    def setUp(self):
        self.example = Example.objects.create(name='Example 1', description='The first example')

    def test_example_exists(self):
        self.assertEqual(self.example.description, 'The first example')

    @patch('example.models.request')
    def test_example_get_page(self, req):
        example = Example.objects.get(name='Example 1')
        url = MagicMock()
        example._get_page(url)
        req.assert_called_once_with('GET', url)

    @patch('example.models.Example._get_page')
    def test_example_page_has_name(self, getpage):
        example = Example.objects.get(name='Example 1')
        resp = MagicMock()
        resp.content = 'Text that contains {} in it'.format(example.name)
        getpage.return_value = resp
        self.assertTrue(example.name_in_page(MagicMock()))
