from enum import Enum


class Action(Enum):
    GET = "get"
    CREATE = "create"
    UPDATE = "update"
    READ = "read"
    DELETE = "delete"
    LIST = "list"
