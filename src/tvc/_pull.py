import argparse

from ._utils import execute_multiple, Command, check_tools


def pull_command(ns: argparse.Namespace) -> bool:
    """
    Executes the pull command.

    :param ns: the parsed options for the status command
    :type ns: argparse.Namespace
    :return: True if successfully executed
    :rtype: bool
    """
    check_tools(fail=True)
    return execute_multiple([
        Command(cmd=["git", "pull"]),
        Command(cmd=["dvc", "pull"]),
    ])


def append_pull_subcmd(subparsers):
    """
    Adds the pull sub-command.

    :param subparsers: the sub-parsers to extend
    """
    parser = subparsers.add_parser('pull', help='Pulls data from the remote.')
    parser.set_defaults(func=pull_command)
