import os
import pathlib
from collections import namedtuple
from typing import List

OldNew = namedtuple("OldNew", ["old", "new"])

def mkdirs(dir_name):
    os.makedirs(dir_name)

def touch(file_path):
    pathlib.Path(file_path).touch()

def get_content(file_path):
    with open(file_path, "r") as f:
        return f.read()

def write_content(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

def replace(content, old_new_list: List[OldNew]):
    for old_new in old_new_list:
        content = content.replace(old_new.old, old_new.new) 
    return content

if __name__ == "__main__":
    content = ""
    module_name = "resource.user"
    endpoint_name = "/web/user"
    methods = ["get", "post", "delete", "put"]

    resource_class_template = get_content("template/resource_class.txt")
    method_template = get_content("template/method.txt")
    app_template = get_content("template/app.txt")

    # make methods code
    method_content = "\r\n\r\n".join([replace(method_template, [
        OldNew("%METHOD%", method.upper()),
        OldNew("%method%", method.lower())
    ]) for method in methods])

    # make resource class code
    resource_class_content = replace(
        resource_class_template,
        [
            OldNew("%ENDPOINT_NAME%", endpoint_name),
            OldNew("%CLASS_NAME%", endpoint_name.split("/")[-1].capitalize()),
            OldNew("%METHODS%", method_content)
        ]
    )

    print(resource_class_content)
