from financier.shared.config import APP_NAME, STAGE


def get_function_name(name: str) -> str:
    return f'{APP_NAME}-{STAGE}-function-{name}'


def get_table_name(name: str) -> str:
    return f'{APP_NAME}-{STAGE}-table-{name}'


def get_api_name(name: str) -> str:
    return f'{APP_NAME}-{STAGE}-api-{name}'
