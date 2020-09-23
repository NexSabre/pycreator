from pycreator.actions.create.create_action import CreateAction


class GoesAction(CreateAction):
    ACTION = "goes"

    def fill_parser_arguments(self):
        self.parser.add_argument('name', type=str, help='Name for the new project')
        self.parser.add_argument('-l', '-at', '--location', type=str, help='Custom location to create a new app')
