#!/usr/bin/env python3
""" Duck typed iterable object"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function generates a tuple of an iterable
    and length of the iterable"""
    return [(i, len(i)) for i in lst]
