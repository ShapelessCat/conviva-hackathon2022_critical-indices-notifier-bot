import os.path as path

project_root = path.abspath(path.join(path.dirname(__file__), ".."))
path2tokens = path.join(project_root, "tokens.json")
# TODO:
#  In reality, this should be a remote location. Since we don't have time to
#  finish the whole pipeline, we use this fake location for testing.
path2reports_folder = path.join(project_root, "reports")
