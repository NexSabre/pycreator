import os

from pycreator.actions.action import Action
from pycreator.core.create_folders import create_new_action
from pycreator.framework.messages import Messages


class AddAction(Action):
    ACTION = "add"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument('-n', '--name', type=str, help="Create new application")

    def process_action(self, configuration):
        self._is_correct_cwd(new_action_name=configuration.name)

    def _is_correct_cwd(self, new_action_name: str) -> bool:
        if not self._available_to_create_directory("actions"):
            return False
        action_location = os.path.join(os.getcwd(), "actions")
        if not create_new_action(action_location,  new_action_name):
            return False

        if not os.path.exists(os.path.join(action_location, new_action_name)):
            Messages.warn(f"{new_action_name} action dir was not created")
            return False
        Messages.info(f"New action {new_action_name} was created")
        Messages.info(f"Remember to import a '{new_action_name}' at 'actions_dispatcher.py'")
        return True

    @staticmethod
    def _available_to_create_directory(dir_name) -> bool:
        # try to find a "actions" directory
        working_dir = os.getcwd()
        if os.path.exists(os.path.join(working_dir, dir_name)):
            return True
        return False
