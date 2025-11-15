"""Simple math helpers for the TEST repository."""
from __future__ import annotations


def square(value: float | int) -> float | int:
    """Return the square of ``value``.

    Parameters
    ----------
    value:
        Numeric value to raise to the second power.

    Returns
    -------
    int | float
        The result of ``value`` multiplied by itself.
    """

    return value * value


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Square a number")
    parser.add_argument("value", type=float, help="Value to square")
    args = parser.parse_args()

    result = square(args.value)
    print(f"{args.value}^2 = {result}")
