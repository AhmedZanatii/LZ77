from compression import LZ77Compressor, Token, compress
from decompression import decompress


def main():
    while True:
        print("\n========== LZ77 MENU ==========")
        print("1. Compress text")
        print("2. Decompress tokens")
        print("3. Exit")
        print("===============================")

        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            text = input("Enter text to compress: ")

            try:
                compressor = LZ77Compressor(text)
                tokens = compressor.compress()

                print("\nCompressed tokens:")
                for token in tokens:
                    print(token)

                restored = decompress(tokens)

                print("\nVerification:", restored == text)

            except (ValueError, TypeError, IndexError) as error:
                print("Error:", error)

        elif choice == "2":
            print("Enter tokens in this format:")
            print("(start,length,char)")
            print("Enter an empty line when finished.")

            tokens = []

            while True:
                line = input().strip()

                if not line:
                    break

                try:
                    # Split into 3 parts so char may contain commas.
                    parts = line.strip("()").split(",", 2)

                    if len(parts) != 3:
                        raise ValueError("Expected 3 token fields.")

                    start = int(parts[0].strip())
                    length = int(parts[1].strip())
                    char = parts[2]

                    if len(char) != 1:
                        raise ValueError(
                            "The character must be exactly one character."
                        )

                    tokens.append(Token(start, length, char))

                except ValueError as error:
                    print("Invalid token:", error)
                    print("Please enter this token again.")
                    continue

            try:
                result = decompress(tokens)
                print("\nDecompressed text:")
                print(result)

            except (ValueError, TypeError, IndexError) as error:
                print("Error:", error)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
