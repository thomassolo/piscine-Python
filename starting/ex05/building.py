import sys
import string


def count_characters(text):
    counts = {
        "upper": sum(1 for c in text if c.isupper()),
        "lower": sum(1 for c in text if c.islower()),
        "punctuation": sum(1 for c in text if c in string.punctuation),
        "spaces": sum(1 for c in text if c.isspace()),
        "digits": sum(1 for c in text if c.isdigit()),
    }
    return counts


def main():
    if len(sys.argv) > 2:
        raise AssertionError("Too many arguments provided.")

    if len(sys.argv) == 1:
        try:
            text = input("What is the text to count? \n")
        except EOFError:
            text = ""
    else:
        text = sys.argv[1]

    counts = count_characters(text)

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
