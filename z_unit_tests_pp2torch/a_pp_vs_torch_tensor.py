import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

import paddle
import paddle.nn as nn2
import paddle.nn.functional as F2

import imageio.v3 as iio
from skimage.transform import resize

im = iio.imread('imageio:chelsea.png')
im = resize(im, (512, 512))
print("im.shape: ", im.shape)

im_p = paddle.to_tensor(im)
im_p = paddle.transpose(im_p, perm=[2,0,1])
im_p = paddle.unsqueeze(im_p, axis=0)
print("im_p.shape: ", im_p.shape)

im_t = torch.from_numpy(im).permute(2,0,1).unsqueeze(0)
print("im_t.shape: ", im_t.shape)

