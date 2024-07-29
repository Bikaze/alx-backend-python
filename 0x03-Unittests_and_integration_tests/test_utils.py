#!/usr/bin/env python3
"""
This module contains unit tests for the access_nested_map function from
the utils module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Any, Dict, Tuple
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str, ...], expected: Any) -> None:
        """
        Test access_nested_map with different inputs and expected outputs.

        Args:
            nested_map (Dict[str, Any]): The nested map to access.
            path (Tuple[str, ...]): The path to access in the nested map.
            expected (Any): The expected result from accessing the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                                         path: Tuple[str, ...]) -> None:
        """
        Test access_nested_map raises KeyError for invalid paths.

        Args:
            nested_map (Dict[str, Any]): The nested map to access.
            path (Tuple[str, ...]): The path to access in the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any],
                      mock_get: Mock) -> None:
        """
        Test get_json with different inputs and expected outputs.

        Args:
            test_url (str): The URL to get JSON from.
            test_payload (Dict[str, Any]): The expected JSON payload.
            mock_get (Mock): The mocked requests.get function.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
