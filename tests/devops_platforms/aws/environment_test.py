"""Unit core for the environment file"""
import os

from core.CommandsCore import CommandsCore
from unittest.mock import patch
from project_types.linux.commands import Commands as LinuxCommands
import devops_platforms.aws.environment as sut

linux_commands = CommandsCore([LinuxCommands])


# region create_environment_variables()


@patch("logging.info")
@patch("tools.cli.call_subprocess")
def test_create_environment_variables_given_dict_when_not_empty_calls_to_create_env_variables_command(
        call_subprocess_mock, logger_mock, platformdata):
    """Given a dictionary, when it is not empty, writes environment variables
    to stdout in the Azure DevOps notation"""

    # Arrange
    environment_variables = platformdata.environment_variables_dict

    # Act
    with patch.dict(os.environ, {}, clear=True):
        sut.create_environment_variables(environment_variables)

        # Assert
        assert "ENV_VAR_1" in os.environ and "ENV_VAR_2" in os.environ

# endregion
