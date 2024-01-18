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


def should_be_positive(number: int | float):
    if number <= 0:
        raise AssertionError(f'{number} is not positive')


def mimmit(action: Literal['koodaa', 'bailaa']):
    print(f'Mimmit {action}!')


def deprecated_keyword():
    """*DEPRECATED* Use `Example keyword` instead."""
    pass
