"""Example library for Robot Framework.

Demonstrates basics of the library API.
"""

from typing import Literal


def example_keyword():
    """Documentation for the example keyowrd.

    Simple *formatting* is _supported_.

    See also `One argument`.
    """
    print('Hello, Mimmit koodaa!')


def one_argument(name):
    print(f'Hello, {name}!')


def three_arguments(arg1, arg2, arg3):
    pass


def default_values(name, ending='!', separator=', '):
    print(f'Hello{separator}{name}{ending}')


def upper(arg):
    return arg.upper()


# The `int | float` syntax requires Python 3.10. Import `Union` from
# `typing` and use `Union[int, float]` with earlier.
def should_be_positive(number: int | float):
    if number <= 0:
        raise AssertionError(f'{number} is not positive')


# Literal conversion is new in Robot Framework 7.0. No conversion is
# done with earlier versions.
def mimmit(action: Literal['koodaa', 'bailaa']):
    print(f'Mimmit {action}!')


def deprecated_keyword():
    """*DEPRECATED* Use `Example keyword` instead."""
    pass
