from compression import Token


def decompress(tokens: list[Token]) -> str:
    """Decompress a list of LZ77 tokens back into the original string."""
    decompressed_string = ""

    for token in tokens:
        if token.length > 0:
            match = decompressed_string[token.start : token.start + token.length]
            decompressed_string += match

        decompressed_string += token.char

    return decompressed_string


# Backward-compatible class-style wrapper if needed
class LZ77Decompressor:
    @staticmethod
    def decompress(tokens: list[Token]) -> str:
        return decompress(tokens)
