from pycreator.actions.action import Action


class ShowVersion(Action):
    ACTION = "version"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        pass

    def process_action(self, configuration):
        print("pycreator: v0.1.2")
