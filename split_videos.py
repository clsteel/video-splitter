"""
Simple script to run the ffmpeg-split.py to split our videos into chunks
"""
import subprocess

# **** REPLACE ME (file_path) ****
# Enter an extra '\' before each '\' in the path!
FILE_PATH='"C:\\Users\\clsteel\\Desktop\\video\\soccer_example\\soccer.mp4"'

args = ["python.exe", "ffmpeg-split.py", "-f", FILE_PATH, '-s', '2']

try:
    output = subprocess.check_output(args)
except Exception as e:
    print("[Error] Had issues running ffmpeg-split.py with those args/filepath. You can also do the following:")
    print("\tClone this and open in PyCharm")
    print("\tRun ffmpeg-split.py in PyCharm with a configuration using the following arg string:")
    print("\t-f \"C:\\Users\\clsteel\\Desktop\\video\\BStar_1a_05092016.MP4\" -s 2")