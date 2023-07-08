#!/usr/bin/env python3
""" Annotated function """
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as
    argument, andreturns a function that multiplies
    a float by multiplier.
    """
    def f(n: float) -> float:
        """ Thid function multiplies a float by a multiplier """
        return float(n * multiplier)

    return f
