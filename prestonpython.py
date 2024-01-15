"""
@package prestonpython
@brief   A collection of miscellaneous Python functions that may be helpful in a variety of circumstances

@date    1/14/2024
@updated 1/14/2024

@author  Preston Buterbaugh
@credit
"""
# Imports
import sys

from colorama import Fore, Style


def red(text: str) -> str:
    """
    @brief  Function to print text in red
    @param  text (str): The text to print red
    @return (str) The red text
    """
    return Fore.RED + text + Style.RESET_ALL


def green(text: str) -> str:
    """
    @brief  Function to print text in green
    @param  text (str): The text to print green
    @return (str) The green text
    """
    return Fore.GREEN + text + Style.RESET_ALL


if __name__ == '__main__':
    print('This script is a library of functions that are intended to be imported and used individually.')
    print('It has no functionality on its own')
    sys.exit(0)
