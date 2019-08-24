from PIL import Image
from torchvision.transforms import Compose, RandomCrop, ToTensor, ToPILImage, Resize, RandomHorizontalFlip

def CheckImageFile(filename):
    return any(filename.endswith(extention) for extention in ['.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG', '.bmp', '.BMP'])

def ImageTransform(loadSize, cropSize):
    return Compose([
        Resize(size=loadSize, interpolation=Image.BICUBIC),
        RandomCrop(size=cropSize),
        RandomHorizontalFlip(p=0.5),
        ToTensor(),
    ])

def MaskTransform(cropSize):
    return Compose([
        Resize(size=cropSize, interpolation=Image.NEAREST),
        ToTensor(),
    ])