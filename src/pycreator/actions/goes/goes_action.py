from pycreator.actions.create.create_action import CreateAction


class GoesAction(CreateAction):
    ACTION = "goes"
    # PARAM_NAME = "ACTION"
    #
    # def fill_parser_arguments(self):
    #     self.parser.add_argument('-n', '--name', type=str, help='Name for the new project', required=True)
    #     self.parser.add_argument('-l', '--location', type=str, help='Custom location to create a new app', default=None)
    #
    # def process_action(self, configuration):
    #     target_location = configuration.location if configuration.location else os.getcwd()
    #     CreateAction.create_boilerplate(target_location, configuration.name)
