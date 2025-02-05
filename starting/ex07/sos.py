import sys


def Morse_dico():
    Nested_Morse = {"A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    " ": "/ ",
                    "\n": "\n"}
    return Nested_Morse


def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    if len(sys.argv) > 2:
        raise AssertionError("Too many arguments provided.")
    else:
        input_text = sys.argv[1].upper()
        for i in input_text:
            if i not in Morse_dico():
                raise AssertionError("The arguments are bad")

    print(" ".join([Morse_dico()[i] for i in input_text]))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
        sys.exit(1)
