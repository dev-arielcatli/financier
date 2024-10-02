from unittest import TestCase

from shared.utils import requests


class TestRequests(TestCase):
    def test_extract_path_parameters(self):
        event = {"pathParameters": {"test": "test"}}
        self.assertEqual(requests.extract_path_parameters(event), {"test": "test"})

    def test_extract_query_parameters(self):
        event = {"queryStringParameters": {"test": "test"}}
        self.assertEqual(requests.extract_query_parameters(event), {"test": "test"})

    def test_extract_multi_value_query_parameters(self):
        event = {"multiValueQueryStringParameters": {"test": ["test"]}}
        self.assertEqual(
            requests.extract_multi_value_query_parameters(event), {"test": ["test"]}
        )

    def test_extract_body(self):
        event = {"body": '{"test": "test"}'}
        self.assertEqual(requests.extract_body(event), {"test": "test"})

    def test_extract_body_empty(self):
        event = {}
        self.assertEqual(requests.extract_body(event), {})

    def test_extract_body_empty_string(self):
        event = {"body": ""}
        self.assertEqual(requests.extract_body(event), {})

    def test_extract_body_None(self):
        event = {"body": None}
        self.assertEqual(requests.extract_body(event), {})
