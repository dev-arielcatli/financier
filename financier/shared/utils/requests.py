def extract_path_parameters(event: dict) -> dict:
    return event.get("pathParameters", {})


def extract_query_parameters(event: dict) -> dict:
    return event.get("queryStringParameters", {})


def extract_multi_value_query_parameters(event: dict) -> dict:
    return event.get("multiValueQueryStringParameters", {})


def extract_body(event: dict) -> dict:
    return event.get("body", {})
