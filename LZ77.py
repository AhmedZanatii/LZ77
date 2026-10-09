from data import Token


def compress(string: str) -> list[Token]:
    tokens: list[Token] = []
    pos = 0

    while pos < len(string):
        steps_back, length = 0, 0

        for size in range(min(pos, len(string) - pos - 1), 0, -1):
            pattern = string[pos : pos + size]

            for start in range(pos - size, -1, -1):
                if string[start : start + size] == pattern:
                    steps_back = pos - start
                    length = size
                    break

            if length > 0: # If a match is found, no need to check smaller sizes
                break

        tokens.append(Token(steps_back, length, string[pos + length]))
        pos += length + 1

    return tokens

def decompress(tokens: list[Token]) -> str:
    decompressed_string = ""

    for token in tokens:
        if token.length > 0:
            if token.length > token.start or token.start > len(decompressed_string):
                raise ValueError(f"Invalid token {token}")

            begin = len(decompressed_string) - token.start
            decompressed_string += decompressed_string[begin : begin + token.length]

        decompressed_string += token.char

    return decompressed_string
