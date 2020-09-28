from typing import Tuple, Dict


class Template:
    def __init__(self, location: Tuple, dest_name: str, template_name: str, render_vars: Dict = None) -> None:
        self.location = location
        self.dest_name = dest_name
        self.template_name = template_name
        self.render_vars = render_vars if render_vars else {}