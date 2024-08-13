import os

# Get the absolute path of the directory containing this script
base_path = os.path.dirname(os.path.abspath(__file__)).split("project1")[0].replace("\\","/")

print("Base path:", base_path)
