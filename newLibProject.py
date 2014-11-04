import json, os, sys, shutil
from xml.etree import ElementTree as ET

# load config file
def load_config():
    config_params = {}
    config_file = file("config.json")
    config_json = json.load(config_file)
    source_project = config_json["source_project"]
    target_folder = config_json["target_folder"]
    config_params['source_project'] = source_project
    config_params['target_folder'] = target_folder
    return config_params

# copy project
def copy_project(source_project, target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    shutil.copytree(source_project, target_dir)

    print("copy source project successed!!!")

# modify target project
def modify_project(project_dir, project_file):

    source_tree = ET.parse(project_dir + "\\" + project_file)
    source_root = source_tree.getroot()

    lib_name = project_dir.split("\\")[-1]

    name_node = source_root.find('name')

    if name_node is not None:
        name_node.text = lib_name
        source_tree.write(project_dir + "\\" + project_file, 'UTF-8')

        print "projet:%s file:%s has modified!!!" %(lib_name, project_file)

# modify target res
def modify_res(project_dir, res_file):
    source_tree = ET.parse(project_dir + "\\res\\values\\" + res_file)
    source_root = source_tree.getroot()

    lib_name = project_dir.split("\\")[-1]

    for res_string in source_root.iter('string'):
        if res_string.attrib['name'] == 'app_name':
            res_string.text = lib_name
            source_tree.write(project_dir + "\\res\\values\\" + res_file, 'UTF-8')

            print "projet:%s file:%s has modified!!!" %(project_name, res_file)

#main
if __name__ == '__main__':
    # pre params
    project_name = "libs_" + sys.argv[1]
    config_list = load_config()
    source_project = config_list["source_project"]
    target_project = config_list["target_folder"] + project_name
    # operate
    copy_project(source_project, target_project)
    modify_project(target_project, ".project")
    modify_res(target_project, "strings.xml")

    print("Create new lib project successed !!!")