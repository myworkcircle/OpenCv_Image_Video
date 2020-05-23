import cv2
import numpy as np
import os
import csv
def partA():
    dir="../Images/"
    with open('../Generated/cluster.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        for filename in os.listdir(dir):
            im = os.path.join(dir, filename)
            image = cv2.imread(im)
            s=image.shape
            p = image[s[0]//2,s[1]//2]
            b=p[0]
            g=p[1]
            r=p[2]
            filewriter.writerow([filename,s[0],s[1],s[2],b,g,r])
    
def partB():
    path="../Images/cat.jpg"
    image = cv2.imread(path)
    c = image.copy()
    c[:, :,0]=0
    c[:, :,1]=0
    path="../Generated/"
    cv2.imwrite(os.path.join(path,'cat_red.jpg'),c)

def partC():
    path="../Images/flowers.jpg"
    image = cv2.imread(path)
    flower = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    flower[...,3]=127
    path="../Generated/"
    cv2.imwrite(os.path.join(path,'flowers.png'),flower)
    # print(flower.shape)

def partD():
    pass

partA()
partB()
partC()
partD()
