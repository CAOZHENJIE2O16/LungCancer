#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:49:36 2017

@author: changlongjiang
"""
import numpy as np
import matplotlib.pyplot as plt
output_path = "/Volumes/Python&Dragon/LUNA/subset1_images"
imgs = np.load(output_path+'images_0.npy')
masks = np.load(output_path+'masks_0.npy')


for i in range(len(imgs)):
    print ("image %d" % i)
    fig,ax = plt.subplots(2,2,figsize=[8,8])
    ax[0,0].imshow(imgs[i],cmap='gray')
    ax[0,1].imshow(masks[i],cmap='gray')
    ax[1,0].imshow(imgs[i]*masks[i],cmap='gray')
    plt.show()
    raw_input("hit enter to cont : ")