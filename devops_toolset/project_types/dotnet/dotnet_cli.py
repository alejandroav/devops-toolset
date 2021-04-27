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


def restore(path: str, force: bool = False, debug: bool = False):
    """ Performs a dotnet restore in the desired path
    Arguments:
        path: The path where restore will be executed.
        force: Adds --force argument.
        debug: Enables diagnostic logs to the command.

    More info: https://docs.microsoft.com/es-es/dotnet/core/tools/dotnet-restore

    """
    tools.cli.call_subprocess(commands.get("dotnet_restore").format(
        force=argument_converters.convert_force_parameter(force),
        path=path,
        debug=argument_converters.convert_debug_parameter(debug)),
        log_before_process=[literals.get("dotnet_restore_before").format(path=path)],
        log_after_err=[literals.get("dotnet_restore_err").format(path=path)])


def build(path: str, configuration: str = "Release", output: str = ".", framework: str = "net5.0",
          runtime: str = "linux-x64", with_restore: bool = False, force: bool = False, debug: bool = False):
    """ Performs a dotnet build in the desired path
    Arguments:
        path: The path where build will be executed.
        configuration: The configuration used for build. Default is "Release".
        output: Adds --output argument. Specifies the output path of the build command. Defaults "."
        framework: The dotnet framework used to build. Default is "net5.0".
        runtime: The runtime used to build. Default is "linux-x64".
        with_restore: Adds --no-restore argument when False. Default to False.
        force: Adds --force argument.
        debug: Enables diagnostic logs to the command.

    More info: https://docs.microsoft.com/es-es/dotnet/core/tools/dotnet-build

    """
    tools.cli.call_subprocess(commands.get("dotnet_build").format(
        force=argument_converters.convert_force_parameter(force),
        path=path,
        debug=argument_converters.convert_debug_parameter(debug),
        configuration=configuration,
        output=output,
        framework=framework,
        runtime=runtime,
        with_restore=argument_converters.convert_with_restore_parameter(with_restore)),
        log_before_process=[literals.get("dotnet_build_before").format(path=path)],
        log_after_err=[literals.get("dotnet_build_err").format(path=path)])


def publish(path: str, self_contained: bool = False, configuration: str = "Release", output: str = ".",
            framework: str = "net5.0", runtime: str = "linux-x64", with_restore: bool = False, force: bool = False,
            debug: bool = False):
    """ Performs a dotnet publish in the desired path
    Arguments:
        path: The path where build will be executed.
        self_contained: Adds --self-contained argument.
        configuration: The configuration used for build. Default is "Release".
        output: Adds --output argument. Specifies the output path of the build command. Defaults "."
        framework: The dotnet framework used to build. Default is "net5.0".
        runtime: The runtime used to build. Default is "linux-x64".
        with_restore: Adds --no-restore argument when False. Default to False.
        force: Adds --force argument.
        debug: Enables diagnostic logs to the command.

    More info: https://docs.microsoft.com/es-es/dotnet/core/tools/dotnet-publish

    """
    tools.cli.call_subprocess(commands.get("dotnet_publish").format(
        force=argument_converters.convert_force_parameter(force),
        path=path,
        debug=argument_converters.convert_debug_parameter(debug),
        configuration=configuration,
        output=output,
        framework=framework,
        runtime=runtime,
        self_contained=argument_converters.convert_self_contained_parameter(self_contained),
        with_restore=argument_converters.convert_with_restore_parameter(with_restore)),
        log_before_process=[literals.get("dotnet_publish_before").format(path=path)],
        log_after_err=[literals.get("dotnet_publish_err").format(path=path)])

if __name__ == "__main__":
    help(__name__)
