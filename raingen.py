#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:02:02 2019

@author: Joakim Edlund
"""

import numpy as np
import cv2
import sys
import random
import math

degtorad = 0.01745329252
radtodeg = 1/degtorad;

# returns a list of lines
def rand_lines(w,h,a,l,nrs):
    lines=[]
    
    for i in range(nrs):
        # randomize starting and ending points for 2D lines
        sx = random.randint(0,w-1)
        sy = random.randint(0,h-1)
        
        le = random.randint(1,l)
        ang = a + random.randint(0,10)
        ex = sx + int(le * math.sin(ang * degtorad))
        ey = sy + int(le * math.cos(ang * degtorad))
        
        # move the endpoints inside the image frame
        if ex<0: ex = 0
        if ex>w-1: ex=w-1
        if ey<0: ey = 0
        if ey>w-1: ey=h-1
        
        # add line to list
        lines.append({'sx':sx,'sy':sy,'ex':ex,'ey':ey})
        
    return lines

def add_rain(img, angle, drop_length, drop_thickness, drop_nrs, blur=4, intensity = 100):
    # create placehplder for rain
    rain=np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype='uint16')
    
    # generate random lines
    lines=rand_lines(rain.shape[1],rain.shape[0],angle,drop_length,drop_nrs)
    
    # draw lines to the image
    for l in lines:
        cv2.line(rain,(l['sx'],l['sy']),(l['ex'],l['ey']),(intensity,intensity,intensity),drop_thickness)
    
    # add blur to the lines
    rain = cv2.blur(rain,(blur,blur))
    
    return rain+img
    
def print_usage():
    print('Usage:')
    print('raingen.py -i <inputfiles> -a <angle> -l <length> -t <thickness> -n <drop_nrs>')
    print('')
    print('Example:')
    print('python raingen.py -i imgs/*.jpg -a 10 -l 30 -t 2 -n 1000')
    print('')
    print('Output:')
    print('Generates rain to given images. Saves them in the same folder with _rain added to the end of the filename(s). If one or more parameters are not given, they will be randomized to reasonable values for each image.')
    print('')
    print('Parameters:')
    print('-i Can be given several filenames separated by comma or generated with wildcard *')
    print('-a Angle given as integer between -90 and 90')
    print('-l The max length of rain drops in pixels (the actual length is random up to length), should be matched somehow to the image resolution')
    print('-t Rain drop width')
    print('-n Number of raindrops to be added')
    print('-b blur filter size')
    print('-c grayscale intensity of rain streaks')
    print('')
    print('Generated images can be moved to a separate folder with:')
    print('mv ./*_rain.jpg ./rainy')

def main(argv):    
    input_files = []
    angle = 100
    length = -1
    thickness = -1
    drop_nrs = -1
    blur = 4
    intensity = 150
    
    # parse args
    for i,arg in enumerate(argv):
        if arg == '-i':
            n=1
            while True:
                try:
                    f=argv[i+n]
                except:
                    break    
                if(f[0] == '-'):
                    if not input_files:
                        print_usage()
                        sys.exit(2)
                    break
                input_files.append(f)
                n+=1
        elif arg == '-h':
            print_usage()
            sys.exit()
        elif arg == '-a':
            try:
                angle=int(argv[i+1])
            except:
                print("Angle must be an integer.")
                sys.exit(2)
            if(angle > 90 or angle <-90):
                print("Angle must be an integer between -90 and 90.")
                sys.exit(2)
        elif arg == '-l':
            try:
                length=int(argv[i+1])
            except:
                print("Length must be an integer.")
                sys.exit(2)
            if(length < 0):
                print("Length must be a positive value, drop length in px.")
                sys.exit(2)
        elif arg == '-t':
            try:
                thickness=int(argv[i+1])
            except:
                print("Thickness must be an integer.")
                sys.exit(2)
            if(thickness < 0):
                print("Thickness must be a positive value, drop width in px.")
                sys.exit(2)
        elif arg == '-n':
            try:
                drop_nrs=int(argv[i+1])
            except:
                print("Number of drops must be an integer.")
                sys.exit(2)
            if(drop_nrs < 0):
                print("Number of drops must be a positive value.")
                sys.exit(2)
        elif arg == '-b':
            try:
                blur=int(argv[i+1])
            except:
                print("Blur filter has to be an integer.")
                sys.exit(2)
            if(blur < 1 or blur > 10):
                print("Blur filter has to be between 1 and 10")
                sys.exit(2)
        elif arg == '-c':
            try:
                intensity=int(argv[i+1])
            except:
                print("Intensity has to be an integer.")
                sys.exit(2)
            if(intensity < 0 or intensity > 255):
                print("Intensity has to be between 0 and 255")
                sys.exit(2)

    # exit if no input files were given
    if not input_files:
        print_usage()
        sys.exit(2)
        
    # add rain to all images
    for file in input_files:
        # if one/some of the parameters were not given: randomize for each image
        if angle == 100:
            rangle = random.randint(-90,90)
        else:
            rangle=angle
        if length == -1:
            rlength = random.randint(10,30)
        else:
            rlength = length
        if thickness == -1:
            rthickness = random.randint(1,2)
        else:
            rthickness = thickness
        if drop_nrs == -1:
            rdrop_nrs = random.randint(500,2000)
        else:
            rdrop_nrs = drop_nrs
            
        print(file)
        
        # read image
        try:
            img = cv2.imread(str(file))    
        except:
            print("Could not open file")
            next
            
        # add rain
        rainy = add_rain(img,rangle,rlength,rthickness,rdrop_nrs,blur,intensity)
        
        #save rainy image
        cv2.imwrite(file[:-4]+'_rain'+'.jpg',rainy)

if(__name__ == "__main__"):
    main(sys.argv[1:])
