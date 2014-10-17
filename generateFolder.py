import json, os
from xml.etree import ElementTree as ET

def load_config():
    config_params = {}
    config_file = file("config.json")
    config_json = json.load(config_file)
    source_project = config_json["source_project"]
    target_folder = config_json["target_folder"]
    config_params['source_project'] = source_project
    config_params['target_folder'] = target_folder
    return config_params

def copy_project(source_project,  target_dir):
 for file in os.listdir(source_project):
     source_file = os.path.join(source_project,  file)
     target_file = os.path.join(target_dir,  file)
     if os.path.isfile(source_file):
         if not os.path.exists(source_project):
             os.makedirs(source_project)
         if not os.path.exists(target_file) or(os.path.exists(target_file) and (os.path.getsize(target_file) != os.path.getsize(source_file))):
                 open(target_file, "wb").write(open(source_file, "rb").read())
     if os.path.isdir(source_file):
         copy_project(source_file, target_file)

def modify_project(project_dir, project_file):
    source_tree = ET.parse(project_dir + project_file)
    source_root = source_tree.getroot()

    name_node = source_root.find('name')
    if name_node is not None and len(name_node)>0:
        name_node.set("name", "libs_")


if __name__ == '__main__':
   config_list = load_config()
   copy_project(config_list["source_project"], config_list["target_folder"])