def create_application_dirs(location, app_name: str):
    import os
    internal_paths = (
        ("src", ),
        ("src", app_name),
        ("src", app_name, "actions"),
        ("src", app_name, "core"),
        ("src", app_name, "framework"),
        ("src", app_name, "main")
    )
    # TODO add verification before this method
    os.makedirs(os.path.join(location, app_name))

    for internal_path in internal_paths:
        os.makedirs(os.path.join(*(location, app_name, *internal_path)))


def create_inits(location, app_name: str):
    import os
    internal_paths = (
        ("src", app_name),
        ("src", app_name, "actions"),
        ("src", app_name, "core"),
        ("src", app_name, "framework"),
        ("src", app_name, "main")
    )

    for internal_path in internal_paths:
        # if not os.path.exists(os.path.join(location, internal_path)):
        #     continue
        with open(os.path.join(*(location, app_name, *internal_path, "__init__.py")), 'w') as init_file:
            init_file.write('')


def create_pycreator_hook(location):
    """
    Create a '.pycreator' file which works like a lock for the pycreator app.
    :param location: Absolute path to the root directory of the new application
    :return: None
    """
    import os
    with open(os.path.join(location, '.pycreator')) as pycreator_hook:
        pycreator_hook.write('')
