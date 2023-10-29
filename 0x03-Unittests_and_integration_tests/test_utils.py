#!/usr/bin/env python3
"""Test utils
"""
import unittest
from unittest.mock import patch, Mock
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
    """ Test JSON """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Mock HTTP calls
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)
