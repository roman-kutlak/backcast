"""This module is the main entry point to the system."""

import logging

from backcast import goals
from backcast.system import BackCast


def main():
    system = BackCast()
    print(system.communicate(goals.DescribeYear(2001)))
    print(system.communicate(goals.DescribeMonth(2001, 'January')))
    print(system.communicate(goals.Compare()))


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    main()
