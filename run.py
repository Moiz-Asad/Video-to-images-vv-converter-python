import cv2 as cv
import glob
import time
import math

vidsrc = cv.VideoCapture('video/video.mp4')

success, image = vidsrc.read()


print("Menu")
print("Enter 1 to convert video to images.")
print("Enter 2 to convert Images to video.")
inp = ""
inp = str(input("Choice : "))


if int(inp) == 1:
    O_Starting_Time = time.time()
    count = 0
    while success:
        path = "image/image"+str(count)+".jpg"
        print(path)
        cv.imwrite(path,image)
        count+=1
        success, image = vidsrc.read()

    O_Ending_Time = time.time()
    ExecTime = math.floor(O_Ending_Time-O_Starting_Time)

    print("Conversion [Video -> Images] takes : "+str(ExecTime)+"sec.")
elif int(inp) == 2:
    try:
        O_Starting_Time = time.time()
        img = cv.imread("image/image0.jpg")
        print("Enter Frames of video ~[1-60].")
        frames = ""
        frames = int(input("Frames : "))
        framesize = (img.shape[1],img.shape[0])
        output = cv.VideoWriter("video/output.avi",cv.VideoWriter_fourcc(*'DIVX'),frames,framesize)
        files = glob.glob("image/*.jpg")
        for filenm in range(0,len(files)):
            frame = cv.imread("image/image"+str(filenm)+".jpg")
            print("image/image"+str(filenm)+".jpg")
            output.write(frame)
            print(str(filenm)+".jpg Added.")
        
        O_Ending_Time = time.time()
        ExecTime = math.floor(O_Ending_Time-O_Starting_Time)
        print("Conversion [Video -> Images] takes : "+str(ExecTime)+"sec.")

    except FileNotFoundError:
        print("No Such File Found!")


output.release()




