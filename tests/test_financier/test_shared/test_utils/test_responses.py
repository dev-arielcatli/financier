from http import HTTPStatus
from unittest import TestCase

from shared.utils import responses


class TestResponses(TestCase):
    def test_make_response(self):
        self.assertEqual(
            responses.make_response({"test": "test"}, HTTPStatus.OK),
            {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "isBase64Encoded": False,
                "multiValueHeaders": {},
                "body": '{"test": "test"}',
            },
        )

    def test_make_response_no_content(self):
        self.assertEqual(
            responses.make_response({}, HTTPStatus.NO_CONTENT),
            {
                "statusCode": 204,
                "headers": {"Content-Type": "application/json"},
                "isBase64Encoded": False,
                "multiValueHeaders": {},
                "body": None,
            },
        )

    def test_make_error_response(self):
        self.assertEqual(
            responses.make_error_response(),
            {
                "statusCode": 500,
                "headers": {
                    "Content-Type": "application/json",
                    "x-amzn-ErrorType": 500,
                },
                "isBase64Encoded": False,
                "body": '{"error": "unhandled_error", "message": "Server got itself in trouble"}',
            },
        )

    def test_make_error_response_custom(self):
        self.assertEqual(
            responses.make_error_response(body="test"),
            {
                "statusCode": 500,
                "headers": {
                    "Content-Type": "application/json",
                    "x-amzn-ErrorType": 500,
                },
                "isBase64Encoded": False,
                "body": '{"error": "unhandled_error", "message": "test"}',
            },
        )

    def test_make_list_response(self):
        self.assertEqual(
            responses.make_list_response([1, 2, 3], "test", HTTPStatus.OK),
            {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "isBase64Encoded": False,
                "multiValueHeaders": {},
                "body": '{"items": [1, 2, 3], "count": 3, "last_evaluated_key": "test"}',
            },
        )
