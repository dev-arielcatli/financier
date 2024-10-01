import json
from http import HTTPStatus

from shared.models.errors import ErrorCodes


def make_response(body: dict, status: HTTPStatus = HTTPStatus.OK) -> dict:
    return {
        "statusCode": status.value,
        "headers": {"Content-Type": "application/json"},
        "isBase64Encoded": False,
        "multiValueHeaders": {},
        "body": json.dumps(body, default=str),
    }


def make_error_response(
    error_code: ErrorCodes = ErrorCodes.UNHANDLED_ERROR,
    status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
) -> dict:
    return {
        "statusCode": status.value,
        "headers": {
            "Content-Type": "application/json",
            "x-amzn-ErrorType": status.value,
        },
        "isBase64Encoded": False,
        "body": json.dumps(
            {
                "error": error_code.value,
            }
        ),
    }

def make_list_response(items: list, last_evaluated_key: str, status: HTTPStatus = HTTPStatus.OK) -> dict:
    return make_response(
        {
            "items": items,
            "count": len(items),
            "last_evaluated_key": last_evaluated_key,
        },
        status,
    )