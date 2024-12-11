from typing import TypeAlias

__all__ = ["Stone"]

Stone: TypeAlias = int


def expansion_code(stone: Stone, times: int):
    return f"{stone}#{times}"
