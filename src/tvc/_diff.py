import argparse

from ._utils import execute_multiple, Command, check_tools


def diff_command(ns: argparse.Namespace) -> bool:
    """
    Executes the diff command.

    :param ns: the parsed options for the diff command
    :type ns: argparse.Namespace
    :return: True if successfully executed
    :rtype: bool
    """
    check_tools(fail=True)

    git = ["git", "diff"]
    dvc = ["dvc", "diff"]
    if ns.dir is not None:
        git.append(ns.dir)
        if ns.dir != ".":
            dvc.append(ns.dir)

    return execute_multiple([
        Command(cmd=git),
        Command(cmd=dvc),
    ])


def append_diff_subcmd(subparsers):
    """
    Adds the diff sub-command.

    :param subparsers: the sub-parsers to extend
    """
    parser = subparsers.add_parser('diff', help='Outputs a diff of the local changes.')
    parser.set_defaults(func=diff_command)
    parser.add_argument('dir', nargs='?', default=None, help="The directory to generate the diff for.")
