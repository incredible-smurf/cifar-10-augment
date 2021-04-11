import abc
import PIL
import random
class Augment():
    #the possibility for change the image
    def __init__(self,possibility=0.1): 
        self.possibility = possibility


    #this is the way for process images
    #   Args:img (type:PIL.Image.Image)
    #   return : proceed img(type:PIL.Image.Image)
    @abc.abstractclassmethod
    def process(self,img):
        pass

    def _check_if_need_augment(self) :
        x = random.uniform(0,1) 
        return x<self.possibility
