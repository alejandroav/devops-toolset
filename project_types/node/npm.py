""" Contains wrappers for npm commands and tasks """

import tools.cli as cli
from core.LiteralsCore import LiteralsCore
from core.CommandsCore import CommandsCore
from project_types.node.commands import Commands as NodeCommands
from project_types.node.Literals import Literals as NodeLiterals
from core.app import App

app: App = App()
literals = LiteralsCore([NodeLiterals])
commands = CommandsCore([NodeCommands])


def convert_npm_extra_args(*args):
    """ Converts a list of variable args into extra args of a command -- <args> """
    if len(args) > 0:
        return " -- " + " ".join(args)
    return ""


def convert_npm_parameter_if_present(value: bool):
    """ Converts a boolean value to a --if-present string."""
    if value:
        return "--if-present"
    return ""


def convert_npm_parameter_silent(value: bool):
    """ Converts a boolean value to a --silent string."""
    if value:
        return "--silent"
    return ""


def run_script(command: str, silent: bool = False, if_present: bool = False, *args):
    """ Wrapper for running arbitrary package scripts

    See Also:
        https://docs.npmjs.com/cli-commands/run-script.html
    Args:

        command: Command to run.
        silent: Prevents showing npm ERR! output on error.
        if_present: Prevents exiting with a non-zero exit code when the script is undefined.
        *args: Extra parameters will be passed as arguments to the subyacent npm run command.
    """
    cli.call_subprocess(commands.get("npm_run").format(
        command=command,
        silent=convert_npm_parameter_silent(silent),
        if_present=convert_npm_parameter_if_present(if_present),
        extra_args=convert_npm_extra_args(args)
    ))


def install(folder: str = ""):
    """ Installs a package, and any packages that it depends on

    See Also:
        https://docs.npmjs.com/cli/install

    Args:
        folder: Install the package in the directory as a symlink in the current project

    """
    cli.call_subprocess(commands.get("npm_install").format(
        folder=folder,
    ), live_log=True)


def theme_build(theme_slug: str, wordpress_path: str):
    """ Executes the src task gulp build task

    Args:
        theme_slug: Name / slug of the theme to build
        wordpress_path: Path of the wordpress installation
    """
    cli.call_subprocess(commands.get("theme_src_build").format(
        theme_slug=theme_slug,
        path=wordpress_path
    ))


if __name__ == "__main__":
    help(__name__)
