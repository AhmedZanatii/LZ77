from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    start: int
    length: int
    char: str

    def __str__(self):
        return f"({self.start},{self.length},{self.char})"


class LZ77Compressor:
    def __init__(self, string: str):
        self.pos = 0
        self.string = string
        self.tokens: list[Token] = []

    def get_look_ahead_window(self) -> int:
        return min(self.pos, len(self.string) - self.pos - 1)

    def compress(self) -> list[Token]:
        if self.pos >= len(self.string):
            return self.tokens

        window = self.get_look_ahead_window()

        # try the longest match first, then shrink
        for length in range(window, 0, -1):
            pattern = self.string[self.pos : self.pos + length]
            start_pos = self.pos - length
            while start_pos >= 0:
                if self.string[start_pos : start_pos + length] == pattern:
                    self.tokens.append(
                        Token(start_pos, length, self.string[self.pos + length])
                    )
                    self.pos += length + 1
                    return self.compress()
                else:
                    start_pos -= 1

        # no match found (or window == 0): emit a literal
        self.tokens.append(Token(0, 0, self.string[self.pos]))
        self.pos += 1
        return self.compress()


# Backward-compatible alias
LZ77 = LZ77Compressor


def compress(text: str) -> list[Token]:
    """Helper function to compress a string using LZ77."""
    return LZ77Compressor(text).compress()
