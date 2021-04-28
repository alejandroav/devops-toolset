"""Base class for Project"""

from core.app import App

app: App = App()

class Project(object):
    """Base class for Project"""

    def __init__(self):
        """ Creates an instance of the configured project_type in settings and expose its concrete methods
        """
        self.cli = app.load_project_specific("cli")
        self.settings = app.settings.get_project_specific_settings()

    def init(self):
        """ Calls the project_type.cli's init method with desired settings """
        return self.cli.init(self.settings["init"])

    def build(self):
        """ Calls the project_type.cli's build method with desired settings """
        return self.cli.build(self.settings["build"])

    def deploy(self):
        """ Calls the project_type.cli's deploy method with desired settings """
        return self.cli.deploy(self.settings["deploy"])

