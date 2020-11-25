import cv2
import numpy as np
import os

from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    k =(files[6:9])
    print(k)
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[6:9]))

    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

def main():

    #pathIn= "D:/Personal/Crowd_PETS09/S2/L3/Time_14-41/View_001/"
    pathIn = " C:/Users/vishnu.s/Downloads/Crowd_PETS09/S1/L1/Time_13-57/View_001/"
    pathOut = 'Walking_1.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()