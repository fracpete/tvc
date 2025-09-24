import argparse
import traceback

from tvc import append_add_subcmd, append_diff_subcmd, append_pull_subcmd, append_push_subcmd, append_status_subcmd


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Combines common command combinations of git (https://git-scm.com/) and dvc (https://dvc.org/).',
        prog="tvc",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(help='The available sub-commands.', required=True)
    append_add_subcmd(subparsers)
    append_diff_subcmd(subparsers)
    append_pull_subcmd(subparsers)
    append_push_subcmd(subparsers)
    append_status_subcmd(subparsers)
    parsed = parser.parse_args(args=args)
    parsed.func(parsed)


def sys_main() -> int:
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.

    :return: 0 for success, 1 for failure.
    """
    try:
        main()
        return 0
    except Exception:
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    main()
