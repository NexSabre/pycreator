from pycreator.actions.action import Action


class ShowVersion(Action):
    ACTION = "version"
    PARAM_NAME = "ACTION"

    VERSION = "v0.2.2"

    def fill_parser_arguments(self):
        pass

    def process_action(self, configuration):
        print(f"pycreator: {ShowVersion.VERSION}")
