from financier.shared.config import APP_NAME, STAGE, TABLE_NAME_MAIN, FUNCTION_CODE_PATH
from financier.shared.utils.actions import Action
from financier.shared.utils.features import Feature


def compose(values: list[str | None]) -> str:
    return "-".join([value or "" for value in values])

# FUNCTIONS


def get_function_name(name: str, feature: Feature, action: Action) -> str:
    return compose([APP_NAME, STAGE, "function", feature.value, name, action.value])


def get_function_handler_path(feature: Feature, action: Action) -> str:
    return f"{FUNCTION_CODE_PATH}.{feature.value}.{action.value}.handler"


# TABLES


def get_table_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "table", name])


def get_app_table_name() -> str:
    return compose([APP_NAME, STAGE, "table", TABLE_NAME_MAIN])

# API


def get_api_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "api", name])

# STACKS


def get_stack_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "stack", name])


def get_database_stack_name() -> str:
    return get_stack_name("database")


def get_functions_stack_name() -> str:
    return get_stack_name("functions")
