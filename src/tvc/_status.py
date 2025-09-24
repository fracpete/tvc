import argparse

from ._utils import execute_multiple, Command, check_tools


def status_command(ns: argparse.Namespace) -> bool:
    """
    Executes the status command.

    :param ns: the parsed options for the status command
    :type ns: argparse.Namespace
    :return: True if successfully executed
    :rtype: bool
    """
    check_tools(fail=True)

    git = ["git", "status"]
    dvc = ["dvc", "status"]
    if ns.dir is not None:
        git.append(ns.dir)
        if ns.dir != ".":
            dvc.append(ns.dir)

    return execute_multiple([
        Command(cmd=git),
        Command(cmd=dvc),
    ])


def append_status_subcmd(subparsers):
    """
    Adds the status sub-command.

    :param subparsers: the sub-parsers to extend
    """
    parser = subparsers.add_parser('status', help='Outputs the local status.')
    parser.set_defaults(func=status_command)
    parser.add_argument('dir', nargs='?', default=None, help="The directory to output the status for.")
