"""A collection of is_even methods"""

from .main import (bitwise_method, convince_method, fast_range_method,
                   hardcoded_method, input_method, intended_method,
                   loop_method, range_method, recursive_method, string_method,
                   switch_method)

__all__ = [
    "intended_method",
    "bitwise_method",
    "string_method",
    "recursive_method",
    "loop_method",
    "switch_method",
    "range_method",
    "fast_range_method",
    "input_method",
    "hardcoded_method",
    "convince_method",
]

__patch_letter__ = "b"
__version__ = str(len(__all__)) + __patch_letter__
