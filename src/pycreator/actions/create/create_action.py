from python_wheel_boilerplate.actions.action import Action


class CreateAction(Action):
    ACTION = "create"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument('arg', type=str, nargs='+', help='Example argument')

    def process_action(self, configuration):
        print(configuration)
