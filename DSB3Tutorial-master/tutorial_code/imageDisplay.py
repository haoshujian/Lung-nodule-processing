# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:43:56 2018

@author: Kent Hao
"""
from os.path import join as pjoin
import matplotlib.pyplot as plt
import numpy as np

subset_name = "subset0"
output_path = pjoin("E:/", "Luna16/", "tutorial/","subset0/")
imgs = np.load(output_path+'images_subset0_0001_0023.npy')
lungmasks = np.load(output_path+'lungmask_subset0_0001_0023.npy')
masks = np.load(output_path+'masks_subset0_0001_0023.npy')
# =============================================================================
# for i in range(len(imgs)):
#     print ("image %d" % i)
#     fig,ax = plt.subplots(3,2,figsize=[8,8])
#     ax[0,0].imshow(imgs[i],cmap='gray')
#     ax[1,0].imshow(lungmasks[i],cmap='gray')
#     ax[1,1].imshow(imgs[i]*lungmasks[i],cmap='gray')
#     ax[2,0].imshow(masks[i],cmap='gray')
#     ax[2,1].imshow(imgs[i]*masks[i],cmap='gray')
#     plt.show()
# =============================================================================
for i in range(len(imgs)):
    print ("image %d" % i)
    fig = plt.subplots(figsize=[8,8])
    plt.imshow(imgs[i],cmap='gray')
    plt.show()
    fig = plt.subplots(figsize=[8,8])
    plt.imshow(imgs[i]*masks[i],cmap='gray')
    plt.show()
    