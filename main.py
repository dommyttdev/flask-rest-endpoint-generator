import generator
from util import file

if __name__ == "__main__":
    module = "web.user"
    file.mkdirs(module.replace(".", "/"))
