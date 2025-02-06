import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list using NumPy and prints its \
    shape before and after slicing.

    Args:
        family (list): 2D list representing the array.
        start (int): Starting index for slicing.
        end (int): Ending index for slicing.

    Returns:
        list: The truncated 2D list converted back from NumPy.
    """
    # Convert list to NumPy array
    family_array = np.array(family)

    # Print the original shape
    print(f"My shape is : {family_array.shape}")

    # Apply slicing
    sliced_array = family_array[start:end]

    # Print the new shape
    print(f"My new shape is : {sliced_array.shape}")

    # Convert back to a list before returning
    return sliced_array.tolist()
