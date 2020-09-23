import os

from pycreator.actions.action import Action
from pycreator.core import create_folders
from pycreator.framework.messages import Messages


class CreateAction(Action):
    ACTION = "create"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument('-n', '--name', type=str, help='Name for the new project', required=True)
        self.parser.add_argument('-l', '--location', type=str, help='Custom location to create a new app', default=None)

    def process_action(self, configuration):
        target_location = configuration.location if configuration.location else os.getcwd()

        # # if os.path.exists(os.path.join(target_location, configuration.name)):
        # #     Messages.error(f"Application with such a name {configuration.name} exists")
        # #     raise
        create_folders.create_application_dirs(location=target_location, app_name=configuration.name)
        create_folders.create_inits(location=target_location, app_name=configuration.name)
        create_folders.create_additional_files(location=target_location, app_name=configuration.name)
        create_folders.create_files_from_templates(target_location, configuration.name)
