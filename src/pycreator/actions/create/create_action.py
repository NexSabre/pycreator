import os

from pycreator.actions.action import Action
from pycreator.core import create_folders


class CreateAction(Action):
    ACTION = "create"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument('-n', '--name', type=str, help='Name for the new project', required=True)
        self.parser.add_argument('-l', '--location', type=str, help='Custom location to create a new app', default=None)

    def process_action(self, configuration):
        target_location = configuration.location if configuration.location else os.getcwd()
        self.create_boilerplate(target_location, configuration.name)

    @staticmethod
    def create_boilerplate(tgt_location: str, app_name: str):
        initial_steps = (
            create_folders.create_application_dirs,
            create_folders.create_inits,
            create_folders.create_additional_files,
            create_folders.create_files_from_templates
        )
        for step in initial_steps:
            step(tgt_location, app_name)
