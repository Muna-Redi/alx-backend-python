#!/usr/bin/env python3

""" Annotated function with mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  Takes a mixd list argument and returns sum as a float. """
    return float(sum(mxd_lst))
