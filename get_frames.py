"""
file: get_frames.py
description:
    This is Chelsea Steel's utility script that uses ffmpeg to grab first/last frames of video clips in a directory.
author: Chelsea   Steel
date: 2021-09-13

Usage:
    #TODO

"""
import ffmpeg
import subprocess
import functools
import os
import shutil

# **** REPLACE ME **** (my folder)
MY_FOLDER = "C:\\Users\\clsteel\\Desktop\\video\\big_fucking_video\\output"
# MY_FILE = "C:\\Users\\clsteel\\Desktop\\video\\BStar_1a_05092016.MP4"
# MY_FILE = "C:\\Users\\clsteel\\Desktop\\video\\soccer.mp4"

def main(folder_name):
    # Grab frames for all the videos in the folder! Or at least the non .. files...
    for filename in os.listdir(folder_name):
        if filename == ".." or filename == ".":
            continue
        get_frames(os.path.join(folder_name, filename))

    # move all pngs to a subfolder

    # make the subfolder:
    output_dir = os.path.join(folder_name, "output")
    os.mkdir(output_dir)

    # for each file in the directory we wrote pngs to...
    for filename in os.listdir(folder_name):
        # if its a png...
        if len(filename) >= 5 and filename[-4:]==".png":
            # move that shit to our new output folder!
            shutil.move(os.path.join(folder_name, filename), output_dir)

def get_frames(filename):
    # 1. Gets number of frames
    frame_count = get_frame_count(filename)
    # 2. Grab the frames and save them
    save_frame(filename, frame_index=0)
    save_frame(filename, frame_index=frame_count-2)

def get_frame_count(filename):
    # 1. Get number of frames
    # 1a. Run command on specified file 'filename'
    #     ffprobe -show_streams IN.AVI
    output = subprocess.check_output(["ffprobe" , "-show_streams" , filename])

    # 1b. Find the video stream
    streamlist = output.split(b'/STREAM')
    vidstream = streamlist[0]
    if vidstream.find(b'audio') != -1:
        print("[Error] might've tried the audio stream - bailing...")
        return -1

    # 1c. Parse the output for frame number 'nb_frames'
    n_frames = -1
    mylist = vidstream.split(b"\r\n")
    for line in mylist:
        if line.find(b"nb_frames") == -1:
            continue
        splitline = line.split(b"=")
        n_frames = int(splitline[1])
        print(n_frames)
    return n_frames


def save_frame(filename, frame_index=0):
    # ffmpeg -i IN.AVI -vf "select='eq(n,LAST_FRAME_INDEX)'" -vframes 1 LAST_FRAME.PNG
    print(f"[save_frame] Saving the {frame_index}th frame of '{filename}'")
    frame_filename = filename + "_" + str(frame_index) + ".png"
    print(f"[save_frame]\t{frame_filename=}")
    crunchy_string = "\"select='eq(n," + str(frame_index) + ")'\""
    print(f"[save_frame]crunchy_string=\n{crunchy_string}")

    # output = subprocess.check_output(["ffmpeg", "-i", filename, "-vf", crunchy_string, "-vframes", "1", frame_filename])
    # Have to do this the janky way with os.system because subprocess fails to properly format all our "'s
    st = functools.reduce(lambda x,y: x + " " + y, ["ffmpeg", "-i", filename, "-vf", crunchy_string, "-vframes", "1", frame_filename])
    print(st)

    os.system(st)
    # print(output)

if __name__=="__main__":
    print("[get_frames.py] I'm running!")

    # if demoing get_folder_frames:
    main(MY_FOLDER)

    # # If demoing get_frames:
    # get_frames(MY_FILE)

