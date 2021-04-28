"""Environment-related functionality for Aws"""

from core.app import App
from core.LiteralsCore import LiteralsCore
from core.CommandsCore import CommandsCore
from devops_platforms.aws.Literals import Literals as AwsLiterals
from project_types.linux.commands import Commands as LinuxCommands
import tools.cli as cli
import logging
import os

app: App = App()
literals = LiteralsCore([AwsLiterals])
linux_commands = CommandsCore([LinuxCommands])


def create_environment_variables(key_value_pairs: dict):
    """Creates environment variables

    Args:
        key_value_pairs: Key-value pair dictionary
    """

    for key, value in key_value_pairs.items():
        name = key.upper()
        logging.info(literals.get("platform_created_ev").format(key=name, value=value))
        os.environ[name] = value


if __name__ == "__main__":
    help(__name__)
