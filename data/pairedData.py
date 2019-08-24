import torch
from torch.utils.data import Dataset
from PIL import Image
from os import listdir, walk
from os.path import join
from random import randint
from data.basicFunction import CheckImageFile, ImageTransform, MaskTransform

class GetPariedData(Dataset):
    def __init__(self, dataRoot, maskRoot, imgPrefix, maskPrefix, loadSize, cropSize):
        super(GetPariedData, self).__init__()

        