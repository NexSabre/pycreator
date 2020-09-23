from argparse import ArgumentParser

from python_wheel_boilerplate.actions.create.create_action import CreateAction
from python_wheel_boilerplate.actions.version import ShowVersion
from python_wheel_boilerplate.framework.messages import Messages


class ActionDispatcher:
    ACTION_HANDLERS = [CreateAction, ShowVersion]

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
            Messages.clean("python_wheel_boilerplate ::")
            Messages.clean("quick tool for pip -> spack package conversion\n")
            Messages.clean("Choose operation:"
                           "\n\t\t - create -- for creation a new package"
                           "\n\t\t - update -- for update a existing package.py")
            Messages.clean("")
            Messages.info("All information are base on the pypi.org")
