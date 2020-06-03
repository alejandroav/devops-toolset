"""Contains tools for working with the command line"""

import subprocess
import core.log_tools
from typing import List


def call_subprocess(command: str,
                    log_before_out: List[str] = None, log_after_out: List[str] = None,
                    log_before_err: List[str] = None, log_after_err: List[str] = None):
    """Calls a subprocess.

    Args:
        command: Command to be executed.
        log_before_out: List of strings to log as info before the stdout, if
            no errors.
        log_after_out: List of strings to log as info after the stdout, if
            no errors.
        log_before_err: List of strings to log as error before the stderr, if
            errors.
        log_after_err: List of strings to log as error after the stderr, if
            errors.
    """

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        core.log_tools.log_list(log_before_out, core.log_tools.LogLevel.info)
        core.log_tools.log_stdouterr(out, core.log_tools.LogLevel.info)
        core.log_tools.log_list(log_after_out, core.log_tools.LogLevel.info)
    if err:
        core.log_tools.log_list(log_before_err, core.log_tools.LogLevel.error)
        core.log_tools.log_stdouterr(err, core.log_tools.LogLevel.error)
        core.log_tools.log_list(log_after_err, core.log_tools.LogLevel.error)


if __name__ == "__main__":
    help(__name__)
