#!/usr/bin/env python3
""" Annotated function with complex types argument """
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a strind and int or float as
    arguments and returns a tuple
    """
    return (k, v**2)
