from shared.config import APP_NAME, FUNCTION_CODE_PATH, STAGE, TABLE_NAME_MAIN
from shared.models.actions import Action
from shared.models.features import Feature


def compose(values: list[str | None]) -> str:
    return "-".join([value or "" for value in values])


# FUNCTIONS


def get_function_name(name: str, feature: Feature, action: Action) -> str:
    return compose([APP_NAME, STAGE, "function", feature.value, name, action.value])


def get_function_handler_path(feature: Feature, action: Action) -> str:
    return f"{FUNCTION_CODE_PATH}.{feature.value}.{action.value}.handler"


def get_layer_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "layer", name])


def get_function_role_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "function", "role", name])


def get_default_function_role_name() -> str:
    return get_function_role_name("default")


# TABLES


def get_table_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "table", name])


def get_app_table_name() -> str:
    return compose([APP_NAME, STAGE, "table", TABLE_NAME_MAIN])


def get_app_table_role_name(role: str) -> str:
    return compose([APP_NAME, STAGE, "table", role, "role"])


# API GATEWAY


def get_api_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "api", name])


def get_api_stack_name() -> str:
    return get_stack_name("apigateway")


def get_deployment_name() -> str:
    return compose(
        [
            APP_NAME,
            "deployment",
            STAGE,
        ]
    )


def get_stage_name() -> str:
    return compose(
        [
            APP_NAME,
            "stage",
            STAGE,
        ]
    )


# STACKS


def get_stack_name(name: str) -> str:
    return compose([APP_NAME, STAGE, "stack", name])


def get_database_stack_name() -> str:
    return get_stack_name("database")


def get_functions_stack_name() -> str:
    return get_stack_name("functions")


def get_api_gateway_stack_name() -> str:
    return get_stack_name("apigateway")
