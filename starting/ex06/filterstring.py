import sys


def filter_words(S, N):
    """
    Filters words from the string S that have a length greater than N.

    Args:
        S (str): The input string.
        N (int): The minimum length of words to include.

    Returns:
        list: A list of words with length greater than N.
    """
    return [word for word in S.split() if len(word) > N]


def validate_args(args):
    """
    Validates the command-line arguments.

    Args:
        args (list): The command-line arguments.

    Raises:
        AssertionError: If the number of arguments is not 2
        or if the types are invalid.
    """
    assert len(args) == 3, "AssertionError: the arguments are bad"
    assert isinstance(args[1], str), "AssertionError: the arguments are bad"
    try:
        int(args[2])
    except ValueError:
        raise AssertionError("AssertionError: the arguments are bad")


def main():
    """
    Main function to execute the program.

    Handles command-line arguments, validates them, and filters words.
    """
    try:
        validate_args(sys.argv)
        S = sys.argv[1]
        N = int(sys.argv[2])
        result = filter_words(S, N)
        print(result)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
