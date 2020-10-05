from argparse import ArgumentParser

from pycreator.actions.add.add_action import AddAction
from pycreator.actions.create.create_action import CreateAction
from pycreator.actions.goes.goes_action import GoesAction
from pycreator.actions.version import ShowVersion
from pycreator.framework.messages import Messages


class ActionDispatcher:
    ACTION_HANDLERS = [AddAction,
                       CreateAction,
                       GoesAction,
                       ShowVersion]

    def __init__(self):
        self.parser = ArgumentParser()
        subparsers = self.parser.add_subparsers()
        self.action_handlers = {action_handler.ACTION: action_handler(subparsers) for action_handler in
                                self.ACTION_HANDLERS}

    def process_application(self):
        configuration = self.parser.parse_args()
        try:
            self.action_handlers[configuration.ACTION].process_action(configuration)
        except AttributeError:
            Messages.clean(f"pycreator {ShowVersion.VERSION}")
            Messages.clean("quick tool to create a Python cmd boilerplate application\n")
            Messages.clean("Choose operation:"
                           "\n\t\t - create -- for creation a new package"
                           "\n\t\t - goes   -- for brrrr"
                           "\n\t\t - add    -- add a new action into actions")
            Messages.clean("")
