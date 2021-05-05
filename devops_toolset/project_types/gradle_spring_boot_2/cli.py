""" Contains spring boot 2 gradle utilities """

import tools.cli
from core.app import App
from core.LiteralsCore import LiteralsCore
from project_types.gradle_spring_boot_2.Literals import Literals as GradleSpringBootLiterals
from core.CommandsCore import CommandsCore
from project_types.gradle_spring_boot_2.commands import Commands as GradleSpringBootCommands

app: App = App()
literals = LiteralsCore([GradleSpringBootLiterals])
commands = CommandsCore([GradleSpringBootCommands])


def build(configuration: str = "jar"):
    """ Performs the Spring Boot Gradle build task.
    Arguments:
        configuration: The configuration used for build (jar or war). Default is "jar".

    More info: https://www.baeldung.com/spring-boot-gradle-plugin

    """
    task = ""

    if configuration is "jar":
        task = "bootJar"
    elif configuration is "war":
        task = "bootWar"

    tools.cli.call_subprocess(commands.get(task),
                              log_before_out=[literals.get("gradle_spring_boot_build_before").format(task=task)],
                              log_after_out=[literals.get("gradle_spring_boot_build_after").format(task=task)],
                              log_after_err=[literals.get("gradle_spring_boot_build_err").format(task=task)])


if __name__ == "__main__":
    help(__name__)
