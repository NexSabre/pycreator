import os

from pycreator.framework.messages import Messages

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
        if self.check_app_exists(target_location, configuration.name):
            exit(1)
        if not self.create_boilerplate(target_location, configuration.name):
            Messages.error(f"Some error occur. The pycreator does not create an application {configuration.name}"
                           f" at {target_location}")
            return
        Messages.ok(f"The pycreator successfully create a new application {configuration.name}"
                    f" at {target_location}")

    @staticmethod
    def create_boilerplate(tgt_location: str, app_name: str):
        try:
            initial_steps = (
                create_folders.create_application_dirs,
                create_folders.create_inits,
                create_folders.create_additional_files,
                create_folders.create_files_from_templates
            )
            for step in initial_steps:
                step(tgt_location, app_name)
        except Exception as e:
            print(e)
            return False
        return True

    @staticmethod
    def check_app_exists(tgt_location: str, app_name: str):
        potential_app_location = os.path.join(tgt_location, app_name)
        if os.path.exists(potential_app_location) and os.path.isdir(potential_app_location):
            Messages.error(f"Application {app_name} exist at {tgt_location}. Choose different name or location.")
            return True
        return False
