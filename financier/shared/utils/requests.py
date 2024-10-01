import json

def extract_path_parameters(event: dict) -> dict:
    return event.get("pathParameters", {}) or {}


def extract_query_parameters(event: dict) -> dict:
    return event.get("queryStringParameters", {}) or {}


def extract_multi_value_query_parameters(event: dict) -> dict:
    return event.get("multiValueQueryStringParameters", {}) or {}


def extract_body(event: dict) -> dict:
    body_str = event.get("body", "")
    return json.loads(body_str) or {}
