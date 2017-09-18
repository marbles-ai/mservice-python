from __future__ import unicode_literals, print_function
import inspect


def debug_break():
    """File rarely changes so breakpoint line number is fixed."""
    assert True
    pass


def isdebugging():
    """Check if we are running in a debugger.

    :return:
    """
    for frame in inspect.stack():
        if frame[1].endswith("pydevd.py"):
            return True
    return False


def dprint(*args, **kwargs):
    """A debug  version of print. Messages are only output if we are running in a debugger.

    :param args: print args.
    :param kwargs: print kwargs.
    """
    if isdebugging():
        print(*args, **kwargs)
