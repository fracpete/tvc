import argparse

from ._utils import execute_multiple, Command, check_tools


def push_command(ns: argparse.Namespace) -> bool:
    """
    Executes the push command.

    :param ns: the parsed options for the status command
    :type ns: argparse.Namespace
    :return: True if successfully executed
    :rtype: bool
    """
    check_tools(fail=True)
    return execute_multiple([
        Command(cmd=["git", "push"]),
        Command(cmd=["dvc", "push"]),
    ])


def append_push_subcmd(subparsers):
    """
    Adds the push sub-command.

    :param subparsers: the sub-parsers to extend
    """
    parser = subparsers.add_parser('push', help='Pushes the local changes to the remote.')
    parser.set_defaults(func=push_command)
