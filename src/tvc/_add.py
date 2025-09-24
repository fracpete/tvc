import argparse
import os

from ._utils import execute_multiple, Command, check_tools


def add_command(ns: argparse.Namespace) -> bool:
    """
    Executes the add command.

    :param ns: the parsed options for the add command
    :type ns: argparse.Namespace
    :return: True if successfully executed
    :rtype: bool
    """
    check_tools(fail=True)

    # dvc add
    cmds = [Command(["dvc", "add", ns.dir])]

    # do we need to add the newly generated .dvc file?
    dvc_file = ns.dir + ".dvc"
    if not os.path.exists(dvc_file):
        cmd = Command(["git", "add", dvc_file])
        if os.path.exists(".gitignore"):
            cmd.cmd.append(".gitignore")
        cmds.append(cmd)

    # git commit
    cmd = Command(["git", "commit", "-m", ns.message, dvc_file])
    if os.path.exists(".gitignore"):
        cmd.cmd.append(".gitignore")
    cmds.append(cmd)

    return execute_multiple(cmds)


def append_add_subcmd(subparsers):
    """
    Adds the add sub-command.

    :param subparsers: the sub-parsers to extend
    """
    parser = subparsers.add_parser('add', help='Adds the specified data directory to dvc and ignores it with git.')
    parser.set_defaults(func=add_command)
    parser.add_argument("-m", "--message", metavar="MESSAGE", help="The git commit message to use.", default=None, type=str, required=True)
    parser.add_argument('dir', default=None, help="The directory to add.")
