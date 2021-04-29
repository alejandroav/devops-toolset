""" Cli implementation of the dotnet project_type """

from core.app import App
from project_types.linux.utils import edit_multiple_in_place
import project_types.dotnet.dotnet_cli as dotnet_cli
from core.LiteralsCore import LiteralsCore
from project_types.Literals import Literals as ProjectTypesLiterals
import logging

app: App = App()
literals = LiteralsCore([ProjectTypesLiterals])


def init(**kwargs):
    """ Defines pre-build tasks """
    logging.info(literals.get("phase_start").format(phase_name="init"))

    if "replacements" in kwargs.keys() and "file_path" in kwargs.keys():
        edit_multiple_in_place(kwargs["replacements"], kwargs["file_path"])

    logging.info(literals.get("phase_end").format(phase_name="init"))


def build(path: str, **kwargs):
    """ Defines build / compile tasks """
    logging.info(literals.get("phase_start").format(phase_name="build"))

    dotnet_cli.build(path, **kwargs)

    logging.info(literals.get("phase_end").format(phase_name="build"))


def test(path: str, **kwargs):
    """ Defines code-testing, e2e-testing (or other testing) tasks """
    pass


def pack(path: str, **kwargs):
    """ Defines artifact generation tasks """
    pass


def merge(path: str, **kwargs):
    """ Defines content merge between the destination artifact and the built artifact. For example: user content"""
    pass


def deploy(path: str, **kwargs):
    """ Defines artifact deployment tasks """
    logging.info(literals.get("phase_start").format(phase_name="deploy"))

    dotnet_cli.publish(path, **kwargs)

    logging.info(literals.get("phase_end").format(phase_name="deploy"))

if __name__ == "__main__":
    help(__name__)
