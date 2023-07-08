#!/usr/bin/env python3
""" Annotated function with Complex type argument"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    fumction takes lists of floats argument
    and returns their sum as a float.
    """

    return sum(input_list)
