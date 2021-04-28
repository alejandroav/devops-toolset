""" Contains dotnet utilities """

import tools.cli
from core.app import App
from core.LiteralsCore import LiteralsCore
from project_types.dotnet.Literals import Literals as DotnetLiterals
from core.CommandsCore import CommandsCore
from project_types.dotnet.commands import Commands as DotnetCommands
import project_types.dotnet.argument_converters as argument_converters

app: App = App()
literals = LiteralsCore([DotnetLiterals])
commands = CommandsCore([DotnetCommands])


def restore(path: str, **kwargs):
    """ Performs a dotnet restore in the desired path
    Arguments:
        path: The path where restore will be executed.
        kwargs: Dict of arguments passed through the command

    More info: https://docs.microsoft.com/es-es/dotnet/core/tools/dotnet-restore

    """
    tools.cli.call_subprocess(commands.get("dotnet_restore").format(
        path=path,
        args=argument_converters.convert_argument_set(**kwargs)),
        log_before_process=[literals.get("dotnet_restore_before").format(path=path)],
        log_after_err=[literals.get("dotnet_restore_err").format(path=path)])


def build(path: str, **kwargs):
    """ Performs a dotnet build in the desired path
    Arguments:
        path:  The path where build will be executed.
        kwargs: Dict of arguments passed through the command

    More info: https://docs.microsoft.com/es-es/dotnet/core/tools/dotnet-build

    """

    tools.cli.call_subprocess(commands.get("dotnet_build").format(
        path=path,
        args=argument_converters.convert_argument_set(**kwargs)),
        log_before_process=[literals.get("dotnet_build_before").format(path=path)],
        log_after_err=[literals.get("dotnet_build_err").format(path=path)])


def publish(path: str, **kwargs):
    """ Performs a dotnet publish in the desired path
    Arguments:
        path:  The path where build will be executed.
        kwargs: Dict of arguments passed through the command

    More info: https://docs.microsoft.com/es-es/dotnet/core/tools/dotnet-publish

    """
    tools.cli.call_subprocess(commands.get("dotnet_publish").format(
        path=path,
        args=argument_converters.convert_argument_set(**kwargs)),
        log_before_process=[literals.get("dotnet_publish_before").format(path=path)],
        log_after_err=[literals.get("dotnet_publish_err").format(path=path)])

if __name__ == "__main__":
    help(__name__)
