import shutil
import subprocess
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Command:
    cmd: List[str]  # the command to execute
    message: Optional[str] = None  # optional message to output


def check_executable(executable: str, msg: str, fail: bool = False) -> bool:
    """
    Checks whether the specified is present.

    :param executable: the executable to check
    :type executable: str
    :param msg: the message to output if not
    :type msg: str
    :param fail: whether to fail with an exception or just output a message
    :type fail: bool
    :return: True if present
    :rtype: bool
    """
    result = shutil.which(executable) is not None
    if not result:
        if fail:
            raise Exception(msg)
        else:
            print(msg)
    return result


def check_git(fail: bool = False) -> bool:
    """
    Tests whether the git executable is available.

    :param fail: whether to raise an Exception or just print/log a message
    :type fail: bool
    :return: True if available
    :rtype: bool
    """
    return check_executable(
        "git",
        "git executable not present or not on PATH environment variable? You can download it from here: https://git-scm.com/",
        fail=fail)


def check_dvc(fail: bool = False) -> bool:
    """
    Tests whether the dvc executable is available.

    :param fail: whether to raise an Exception or just print/log a message
    :type fail: bool
    :return: True if available
    :rtype: bool
    """
    return check_executable(
        "dvc",
        "dvc executable not present or not on PATH environment variable? You can download it from here: https://dvc.org/",
        fail=fail)


def check_tools(fail: bool = False) -> bool:
    """
    Checks git and dvc.

    :param fail: whether to raise an Exception or just print/log a message
    :type fail: bool
    :return: True if available
    :rtype: bool
    """
    return check_git(fail=fail) and check_dvc(fail=fail)


def execute_command(cmd: Command) -> bool:
    """
    Executes the command in tandem.

    :param cmd: the command to execute
    :type cmd: Command
    :return: whether the execution was successful
    :rtype: bool
    """
    print("Executing: %s" % " ".join(cmd.cmd))
    completed = subprocess.run(cmd.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if completed.stdout is not None:
        if cmd.message is not None:
            print(cmd.message)
        print(completed.stdout.decode("utf-8"))
    return completed.returncode == 0


def execute_multiple(cmds: List[Command]) -> bool:
    """
    Executes the two commands in tandem.

    :param cmds: the commands to execute
    :type cmds: list
    :return: whether the execution was successful
    :rtype: bool
    """
    result = True
    for cmd in cmds:
        result = execute_command(cmd)
        if not result:
            break
    return result
