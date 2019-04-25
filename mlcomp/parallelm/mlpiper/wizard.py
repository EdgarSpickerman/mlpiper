#
# Copyright (c) 2015, Adam Meily <meily.adam@gmail.com>
# Pypsi - https://github.com/ameily/pypsi
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#


'''
This is an example Pypsi shell using several key features of the Pypsi API and
architecture. The code is provided as an example of the overarching Pypsi design
and API. The demo shell can be used as a skeleton for new shells and can be
easily modified.
'''

from pypsi.shell import Shell
from pypsi.core import Command
from pypsi.commands.help import HelpCommand, Topic
from pypsi.commands.tip import TipCommand

from pypsi import wizard as wiz
from pypsi.format import Table, Column, title_str
from pypsi.completers import path_completer

from pypsi.ansi import AnsiCodes
from pypsi import topics

from pypsi.os import find_bins_in_path

import sys

ShellTopic = """These commands are built into the Pypsi shell (all glory and honor to the pypsi shell).
This is a single newline

and This is a double"""

from parallelm.pipeline.component_language import ComponentLanguage
from parallelm.pipeline.component_group import ComponentGroup
from parallelm.pipeline.data_type import EngineType
from parallelm.pipeline.component_model_behavior_type import ComponentModelBehaviorType

from parallelm.pipeline.component_info import ComponentInfo, ComponentInfoEncoder
from parallelm.pipeline.component_connection_info import ComponentConnectionInfo
from parallelm.pipeline.component_argument_info import ComponentArgumentInfo
from parallelm.pipeline import json_fields

import six
import json

# TODO: make dependencies a list
# show options on each step
# make connection type an options list
# show available commands on start
# save to file
# edit existing input/output/argument with default from prev step
# arguments: check that there is no duplication keys
# unset values
# remove input/output/argument
# questions: do you have inputs? do you have outputs? more inputs?

# component info: get argument by key; get connection by index


# getting __dict__ attributes and filtering only what is needed
language_options = [v for k, v in vars(ComponentLanguage).items() if not k.startswith("__")]
engine_options = [v for k, v in vars(EngineType).items() if not k.startswith("__")]
group_options = list(map(lambda e: e.value, ComponentGroup))
model_behavior_options = list(map(lambda e: e.value, ComponentModelBehaviorType))
boolean_options = ["True", "False"]
argument_type_options = ["string", "int", "long", "float", "double", "boolean", "sequence.string", "sequence,string"]


def options_to_str(options_list):
    tmp_list = ["{} - {}".format(i + 1, o) for i, o in enumerate(options_list)]
    return "; ".join(tmp_list)

class CommandName:
    COMPONENT = "comp"
    ARGUMENT = "argument"
    INPUT = "input"
    OUTPUT = "output"
    SHOW = "show"


def my_choice_validator(choices):
    def validator(ns, value):

        if value is None:
            raise ValueError('Invalid input. Please input: {}'.format(options_to_str(choices)))

        # value is always of a string type here
        try:
            value = int(value)
        except ValueError:
            pass

        # value is still a string if it was not converted to int
        if isinstance(value, six.string_types):
            if value not in choices:
                raise ValueError('Invalid input. Please input: {}'.format(options_to_str(choices)))
        elif isinstance(value, six.integer_types):
            if value < 1 or value > len(choices):
                raise ValueError('Invalid input. Please input: {}'.format(options_to_str(choices)))
            selected = choices[value - 1]
            print(selected)
            return selected
        else:
            raise ValueError('Invalid input. Please input: {}'.format(options_to_str(choices)))

        return value

    return validator


class MainSectionWizard(object):
    def __init__(self, component_info):
        self.wizard = wiz.PromptWizard(
            name="Component Configuration",
            description="Shows various examples of wizard steps",
            steps=[
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_NAME_FIELD,
                               name='Name', help='Name',
                               default=component_info.name,
                               validators=wiz.required_validator),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ENGINE_TYPE_FIELD,
                               name="Engine Type", help="Engine type",
                               default=component_info.engine_type if component_info.engine_type else EngineType.GENERIC,
                               validators=my_choice_validator(engine_options)),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_LANGUAGE_FIELD,
                               name='Language', help='Component programming language',
                               default=component_info.language if component_info.language else ComponentLanguage.PYTHON,
                               validators=my_choice_validator(language_options)),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_GROUP_FIELD,
                               name='Group', help='Component Group',
                               default=component_info.group,
                               validators=my_choice_validator(group_options)),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_LABEL_FIELD,
                               name='Label', help='Label to be displayed in MCenter UI',
                               default=component_info.label),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_DESCRIPTION_FIELD,
                               name='Description', help='Component functionality description. It will be displayed in MCenter UI',
                               default=component_info.description),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_VERSION_FIELD,
                               name="Component version", help="Component version number",
                               default=component_info.version if component_info.version else 1),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_USER_STAND_ALONE,
                               name='User standalone', help='Component can be standalone or connected',
                               default=component_info.user_standalone if component_info.user_standalone else "False",
                               validators=(my_choice_validator(boolean_options))),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_PROGRAM_FIELD,
                               name='Program', help='Program file',
                               default=component_info.program),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_CLASS_FIELD,
                               name='Component class', help='Component class',
                               default=component_info.component_class),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_MODEL_BEHAVIOR_FIELD,
                               name='Model Behavior', help='Model behavior',
                               default=component_info.model_behavior if component_info.model_behavior else ComponentModelBehaviorType.AUXILIARY.value,
                               validators=(my_choice_validator(model_behavior_options))),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_USE_MLOPS_FIELD,
                               name='Use MLOps', help='If to use MLOps',
                               default=component_info.use_mlops if component_info.use_mlops else 'True',
                               validators=(my_choice_validator(boolean_options))),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_PYTHON_DEPS,
                               name='Dependencies', help='Dependencies packages, comma separated',
                               default=component_info.deps,
                               validators=self._deps_validator),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_INCLUDE_GLOB_PATTERNS,
                               name='Include Glob Patterns', help='Example: **/folder | file.txt',
                               default=component_info.include_glob_patterns),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_EXCLUDE_GLOB_PATTERNS,
                               name='Exclude Glob Patterns', help='Example: **/folder | file.txt',
                               default=component_info.exclude_glob_patterns)
            ]
        )

    def run(self, shell):
        return self.wizard.run(shell)

    def _deps_validator(self, ns, value):
        if isinstance(value, six.string_types):
            if not len(value):
                return None
            try:
                value = value.replace(" ", "").split(",")
            except:
                raise ValueError("Wrong format. Comma separated values expected")
        return value


class ConnectionWizard(object):
    def __init__(self):
        self.wizard = wiz.PromptWizard(
            name="Connection Configuration",
            description="Shows various examples of wizard steps",
            steps=[
                wiz.WizardStep(id=json_fields.CONNECTION_DESC_DESCRIPTION_FIELD,
                               name='Description', help='Connection Description.'),
                wiz.WizardStep(id=json_fields.CONNECTION_DESC_LABEL_FIELD,
                               name='Label', help='Label to be displayed in MCenter UI'),
                wiz.WizardStep(id=json_fields.CONNECTION_DESC_TYPE_FIELD,
                               name='Type', help='Type', default="str"),
                wiz.WizardStep(id=json_fields.CONNECTION_DESC_GROUP_FIELD,
                               name='Group', help='Group', default="data"),
                wiz.WizardStep(id=json_fields.CONNECTION_DESC_DEFAULT_COMPONENT_FIELD,
                               name='Default Component', help='Default Component')
            ]
        )

    def run(self, shell):
        return self.wizard.run(shell)


class ArgumentWizard(object):
    def __init__(self):
        self.wizard = wiz.PromptWizard(
            name="Connection Configuration",
            description="Shows various examples of wizard steps",
            steps=[
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_KEY,
                               name='Key', help='Key'),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_TYPE,
                               name='Type', help='Type', default="string", validators=my_choice_validator(argument_type_options)),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_LABEL,
                               name='Label', help='Label'),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_DESCRIPTION,
                               name='Description', help='Description'),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_ENV_VAR,
                               name='Env Var', help='Env Var'),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_OPTIONAL, default="False",
                               name='Optional', help='Is parameter optional', validators=(my_choice_validator(boolean_options))),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_TAG,
                               name='Tag', help='Tag'),
                wiz.WizardStep(id=json_fields.COMPONENT_DESC_ARGUMENT_DEFAULT_VAL,
                               name='Default Value', help='Default Value')
            ]
        )

    def run(self, shell):
        return self.wizard.run(shell)


class WizardCommandHandler(Command):
    '''
    Simple command to launch an example configuration wizard.
    '''

    def __init__(self, name, **kwargs):
        super(WizardCommandHandler, self).__init__(name=name, **kwargs)
        self._name = name

    def _wizard_factory(self, component_info):
        if self._name in [CommandName.INPUT, CommandName.OUTPUT]:
            w = ConnectionWizard()
        elif self._name == CommandName.ARGUMENT:
            w = ArgumentWizard()
        elif self._name == CommandName.COMPONENT:
            w = MainSectionWizard(component_info)
        return w

    def run(self, shell, args):
        component_info = shell._component_info
        w = self._wizard_factory(component_info)
        ns = w.run(shell)
        if ns:
            dd = {}
            for k, v in ns.__dict__.items():
                if isinstance(v, six.string_types) and len(v) == 0:
                    continue
                dd[k] = v

            if self._name == CommandName.INPUT:
                connection = ComponentConnectionInfo(dd)
                if component_info._inputs is None:
                    component_info._inputs = []
                component_info._inputs.append(connection)
            elif self._name == CommandName.OUTPUT:
                connection = ComponentConnectionInfo(dd)
                if component_info._outputs is None:
                    component_info._outputs = []
                component_info._outputs.append(connection)
            elif self._name == CommandName.ARGUMENT:
                arg = ComponentArgumentInfo(dd)
                if component_info.arguments is None:
                    component_info.arguments = []
                component_info.arguments.append(arg)
            elif self._name == CommandName.COMPONENT:
                component_info.load_from_json(dd)
            else:
                pass

        else:
            pass

        return 0


class PrintCommand(Command):
    '''
    Simple command to launch an example configuration wizard.
    '''

    def __init__(self, name, **kwargs):
        super(PrintCommand, self).__init__(name=name, **kwargs)

    def run(self, shell, args):
        component_info = shell._component_info
        print(json.dumps(component_info, indent=4, cls=ComponentInfoEncoder))

        return 0


class DemoShell(Shell):
    '''
    Example demonstration shell.
    '''

    # First, add commands and plugins to the shell
    print_cmd = PrintCommand(name=CommandName.SHOW)
    comp_wiz = WizardCommandHandler(name=CommandName.COMPONENT)
    input_conn_wiz = WizardCommandHandler(name=CommandName.INPUT)
    output_conn_wiz = WizardCommandHandler(name=CommandName.OUTPUT)
    argument_wiz = WizardCommandHandler(name=CommandName.ARGUMENT)

    # Drop commands to cmd.exe if the platform is Windows
    help_cmd = HelpCommand()

    def __init__(self):
        # You must call the Shell.__init__() method.
        super(DemoShell, self).__init__()

        self.prompt = "{cyan}component builder{r} {green}>{r} ".format(
            r=AnsiCodes.reset.prompt(),
            cyan=AnsiCodes.cyan.prompt(), green=AnsiCodes.green.prompt()
        )

        # Register the shell topic for the help command
        self.help_cmd.add_topic(self, Topic("shell", "Builtin Shell Commands"))
        # Add the I/O redirection topic
        self.help_cmd.add_topic(self, topics.IoRedirection)

        self._sys_bins = None

        self._component_info = ComponentInfo()

    def on_cmdloop_begin(self):
        print(AnsiCodes.clear_screen)

    ############################################################################
    # This functions demonstrate that existing Python :mod:`cmd` shell commands
    # work without modification in Pypsi.
    ############################################################################
    def do_cmddoc(self, args):
        '''
        This is some long description for the cmdargs command.
        '''
        print("do_cmdargs(", args, ")")
        return 0

    def help_cmdout(self):
        print("this is the help message for the cmdout command")

    def do_cmdout(self, args):
        print("do_cmdout(", args, ")")
        return 0

    def get_command_name_completions(self, prefix):
        if not self._sys_bins:
            self._sys_bins = find_bins_in_path()

        return sorted(
            [name for name in self.commands if name.startswith(prefix)] +
            [name for name in self._sys_bins if name.startswith(prefix)]
        )
