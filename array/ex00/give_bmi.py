import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """Calculate BMI for each height-weight pair.

    Args:
        height: List of heights in meters
        weight: List of weights in kilograms

    Returns:
        list: A list of BMI values
    """
    if not (isinstance(height, list) and isinstance(weight, list)):
        raise TypeError("Both height and weight should be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    if not all(isinstance(h, (int, float)) and h > 0 for h in height):
        raise ValueError("All height values must be positive \
                         integers or floats.")

    if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
        raise ValueError("All weight values must be positive \
                         integers or floats.")

    return (np.array(weight) / np.array(height) ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Compare BMI values against a limit.

    Args:
        bmi: List of BMI values
        limit: Integer threshold to compare against

    Returns:
        list: Boolean values (True if BMI > limit, False otherwise)
    """
    if not isinstance(bmi, list) or \
       not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI must be a list of integers or floats.")

    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be a number (int or float).")

    return (np.array(bmi) > limit).tolist()
