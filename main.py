from LZ77 import compress, decompress
from data import Token


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

            tokens = compress(text)
            print("\nCompressed tokens:")
            for token in tokens:
                print(token)

        elif choice == "2":
            print("Enter tokens in this format:")
            print("(start,length,char)")
            print("Enter an empty line when finished.")

            tokens = []

            while True:
                line = input()

                if not line.strip():
                    break

                try:
                    tokens.append(Token.read(line.strip()))
                except ValueError as error:
                    print("Invalid token:", error)
                    print("Please enter this token again.")

            try:
                result = decompress(tokens)
            except ValueError as error:
                print("Error decompressing tokens:", error)
                continue

            print("\nDecompressed text:")
            print(result)


        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
