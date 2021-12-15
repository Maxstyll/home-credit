import os

ori_path = os.getcwd()
os.chdir(ori_path + "/src")
print(f"get cwd {os.getcwd()}")

__version__ = "0.0.0"