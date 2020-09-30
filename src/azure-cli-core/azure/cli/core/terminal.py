# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from prompt_toolkit import Application
from prompt_toolkit.widgets import Frame, TextArea
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.layout.layout import Layout


def command_prompt(line_number, wrap_count):
    return '>'


class Terminal(object):
    def __init__(self):
        self.header_container = Frame(TextArea(
            text='1', multiline=True, accept_handler=self.command_handler, get_line_prefix=command_prompt
        ), height=20)
        self.command_container = Frame(TextArea(
            text='', multiline=False, accept_handler=self.command_handler, get_line_prefix=command_prompt
        ), height=4)
        self.content_container = Frame(TextArea(
            text='I am just a placeholder'
        ))
        self.status_container = Frame(TextArea(
            text='', multiline=False, accept_handler=self.command_handler, get_line_prefix=command_prompt
        ), height=8)
        self.app = Application(
            layout=Layout(HSplit([
                self.header_container,
                self.command_container,
                self.content_container,
                self.status_container
            ])),
            full_screen=True,
            mouse_support=True
        )
        self.layout = None

    def command_handler(self, buffer):
        cmd = buffer.text
        print(cmd)
        if cmd == 'exit':
            self.app.exit()

    def run(self):
        self.app.run()


