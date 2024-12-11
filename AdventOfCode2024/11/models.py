from typing import TypeAlias

__all__ = ["Stone"]

Stone: TypeAlias = int


def get_expansion_code(stone: Stone, times: int):
    return f"{stone}#{times}"
