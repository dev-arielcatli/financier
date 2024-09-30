from http import HTTPStatus
from shared.models.errors import ErrorCodes


def make_response(body: dict, status: HTTPStatus = HTTPStatus.OK) -> dict:
    return {
        "statusCode": status.value,
        "headers": {
            "Content-Type": "application/json"
        },
        "isBase64Encoded": False,
        "multiValueHeaders": {},
        "body": body
    }


def make_error_response(error_code: ErrorCodes = ErrorCodes.UNHANDLED_ERROR, status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR) -> dict:
    return {
        "statusCode": status.value,
        "headers": {
            "Content-Type": "application/json",
            "x-amzn-ErrorType": status.value
        },
        "isBase64Encoded": False,
        "body": {
            "error": error_code.value,
        }
    }
