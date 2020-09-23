from typing import Tuple, Dict


def get_internal_paths(app_name):
    return (
        ("src", app_name),
        ("src", app_name, "actions"),
        ("src", app_name, "actions", "example_action"),
        ("src", app_name, "core"),
        ("src", app_name, "framework"),
        ("src", app_name, "main")
    )


def create_application_dirs(location, app_name: str):
    import os
    internal_paths = (
        ("src",),
        *get_internal_paths(app_name)
    )
    # TODO add verification before this method
    os.makedirs(os.path.join(location, app_name))

    for internal_path in internal_paths:
        os.makedirs(os.path.join(*(location, app_name, *internal_path)))


def create_inits(location, app_name: str):
    import os
    internal_paths = get_internal_paths(app_name)

    for internal_path in internal_paths:
        # if not os.path.exists(os.path.join(location, internal_path)):
        #     continue
        with open(os.path.join(*(location, app_name, *internal_path, "__init__.py")), 'w') as init_file:
            init_file.write('')


def create_additional_files(location, app_name: str):
    import os
    internal_paths = (
        "README.md",
        "VERSION",
        "LICENSE.md"
    )

    for internal_path in internal_paths:
        with open(os.path.join(*(location, app_name, internal_path)), 'w') as init_file:
            init_file.write(f"{app_name} {internal_path}")


def create_pycreator_hook(location):
    """
    Create a '.pycreator' file which works like a lock for the pycreator app.
    :param location: Absolute path to the root directory of the new application
    :return: None
    """
    import os
    with open(os.path.join(location, '.pycreator')) as pycreator_hook:
        pycreator_hook.write('')


class Template:
    def __init__(self, location: Tuple, dest_name: str, template_name: str, render_vars: Dict = None) -> None:
        self.location = location
        self.dest_name = dest_name
        self.template_name = template_name
        self.render_vars = render_vars if render_vars else {}


def create_files_from_templates(location: str, app_name: str):
    import os
    from jinja2 import Environment, PackageLoader, select_autoescape
    env = Environment(
        loader=PackageLoader('pycreator', 'templates'),
        autoescape=select_autoescape(['html', 'xml', 'j2'])
    )

    files_per_template = (
        Template(("src", app_name), 'setup.py', 'setup.j2', {"creator_app_name": app_name}),
        Template(("src", app_name, "main"), "main.py", "main.j2", {"creator_app_name": app_name}),
        Template(("src", app_name, "framework"), "messages.py", "messages.j2", {"creator_app_name": app_name}),
        Template(("src", app_name, "actions"), "version.py", "version.j2", {"creator_app_name": app_name}),
        Template(("src", app_name, "actions"), "action_dispatcher.py", "action_dispatcher.j2",
                 {"creator_app_name": app_name}),
        Template(("src", app_name, "actions"), "action.py", "action.j2", {"creator_app_name": app_name}),
        Template(("src", app_name, "actions", "example_action"), "example_action.py", "example_action.j2",
                 {"creator_app_name": app_name,
                  "creator_class_name": "ExampleAction",
                  "creator_class_name_action": "example"}),
    )

    for file_template in files_per_template:
        path_file_template = os.path.join(*(location, app_name, *file_template.location, file_template.dest_name))
        with open(path_file_template, 'w') as new_file:
            template = env.get_template(file_template.template_name)
            new_file.write(template.render(**file_template.render_vars))
