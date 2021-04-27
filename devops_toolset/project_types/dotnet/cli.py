""" Cli implementation of the dotnet project_type """

from project_types.linux.utils import edit_multiple_in_place
import project_types.dotnet.dotnet_cli as dotnet_cli


def init(settings: dict = {}):
    """ Defines pre-build tasks """
    if "replacements" in settings.keys() and "file_path" in settings.keys():
        edit_multiple_in_place(settings["replacements"], settings["file_path"])


def build(settings: dict = {}):
    """ Defines build / compile tasks """
    dotnet_cli.restore(settings["path"], settings["force"], False)
    dotnet_cli.build(settings["path"],
                     settings["configuration"],
                     settings["output"],
                     settings["framework"],
                     settings["runtime"],
                     settings["restore"],
                     settings["force"],
                     False)

def test():
    """ Defines code-testing, e2e-testing (or other testing) tasks """
    pass


def pack():
    """ Defines artifact generation tasks """
    pass


def merge():
    """ Defines content merge between the destination artifact and the built artifact. For example: user content"""
    pass


def deploy(settings: dict = {}):
    """ Defines artifact deployment tasks """
    dotnet_cli.publish(settings["path"],
                     settings["configuration"],
                     settings["output"],
                     settings["framework"],
                     settings["runtime"],
                     settings["restore"],
                     settings["force"],
                     settings["self_contained"],
                     False)


if __name__ == "__main__":
    help(__name__)