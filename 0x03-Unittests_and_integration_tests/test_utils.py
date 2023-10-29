#!/usr/bin/env python3
"""Test utils
"""
import unittest
from unittest.mock import patch, Mock
from your_module import utils  # Import the module where utils.get_json is defined

from parameterized import parameterized
from utils import access_nested_map
from utils import get_json

class TestAccessNestedMap(unittest.TestCase):
    """Access nested map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Access nested method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path_map):
        """ Exception access nested method
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path_map)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))

class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        # Create a Mock object for requests.get
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        # Call the get_json function
        result = get_json(test_url)

        # Assert that requests.get was called exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result matches the expected test_payload
        self.assertEqual(result, test_payload)
