"""Base class for Project"""

from core.app import App
import os

app: App = App()

class Project(object):
    """Base class for Project"""

    def __init__(self):
        """ Creates an instance of the configured project_type in settings and expose its concrete methods
        Arguments:
            path: Indicates where the project is located inside the filesystem.
        """
        self.cli = app.load_project_specific("cli")
        self.project_path = "."
        if "PROJECT_PATH" in os.environ:
            self.project_path = os.environ["PROJECT_PATH"]

    def init(self, **kwargs):
        """ Calls the project_type.cli's init method with desired settings """
        return self.cli.init(self.project_path, **kwargs)

    def build(self, **kwargs):
        """ Calls the project_type.cli's build method with desired settings """
        return self.cli.build(self.project_path, **kwargs)

    def test(self, **kwargs):
        """ Calls the project_type.cli's test method with desired settings """
        return self.cli.test(self.project_path, **kwargs)

    def pack(self, **kwargs):
        """ Calls the project_type.cli's test method with desired settings """
        return self.cli.pack(self.project_path, **kwargs)

    def merge(self, **kwargs):
        """ Calls the project_type.cli's merge method with desired settings """
        return self.cli.merge(self.project_path, **kwargs)

    def deploy(self, **kwargs):
        """ Calls the project_type.cli's deploy method with desired settings """
        return self.cli.deploy(self.project_path **kwargs)

