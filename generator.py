import os

from util import json, file

TEMPLATE_DIR_PATH = "template"
APP_TEMPLATE_FILE = "app.txt"


def generate(endpoints_json, output_dir):
    if not os.path.exists(endpoints_json):
        return
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    json_obj = json.load_file(endpoints_json)


def create_module_file(output_dir, module_name):
    module_path = module_name.split(".")
    print(module_path)
    if len(module_path) == 0:
        return None
    module_name = "{}.py".format(module_path[-1])
    dir_name = module_path[0:-1] if 2 <= len(module_path) else []
    module_file_path = os.path.join(output_dir, *dir_name, module_name)

    if not os.path.exists(dir_name):
        file.mkdirs(dir_name)
    if not os.path.exists(module_file_path):
        file.touch(module_file_path)


if __name__ == "__main__":
    pass
