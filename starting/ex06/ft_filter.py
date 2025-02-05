def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def is_even(num):
    return num % 2 == 0


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(list(ft_filter(is_even, nums)))
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
