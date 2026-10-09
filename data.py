from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Token:
    start: int
    length: int
    char: str

    def __str__(self) -> str:
        return f"({self.start},{self.length},{self.char})"

    @staticmethod
    def read(string: str) -> "Token":
        match = re.fullmatch(r"\((\d+),(\d+),(.)\)", string, re.DOTALL)
        if not match:
            raise ValueError(f"Invalid string: {string!r}")
        return Token(int(match[1]), int(match[2]), match[3])

