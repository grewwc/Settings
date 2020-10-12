import argparse
from apis import *

parser = argparse.ArgumentParser()


# vscode
# pycharm
# intellij
# goland

all_arguments = [
    "--push-vscode-setting",
    "--push-vscode-keybinding",
    "--push-vscode",

    "--pull-vscode-setting",
    "--pull-vscode-keybinding",
    "--pull-vscode",
]

app_type_dict = {
    'vscode': vscode_app
}


for argument in all_arguments:
    parser.add_argument(argument, action='store_true')

parsed = parser.parse_args()

parsed_dict = vars(parsed)


for k, v in parsed_dict.items():
    if v:
        k = k.lstrip('-')
        action, app_type, *file_type = k.split('_')
        if not file_type:
            file_type = ['setting', 'keybinding']
            app = app_type_dict[app_type]
            func_names = ['_'.join([action, f]) for f in file_type]
            for func_name in func_names:
                getattr(app, func_name)()
        else:
            app = app_type_dict[app_type]
            func_name = '_'.join([action, *file_type])
            getattr(app, func_name)()
