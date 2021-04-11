import abc
import PIL
import random
class Augment():
    def __init__(self,possibility=0.1): 
        self.possibility = possibility

    @abc.abstractclassmethod
    def process(self,img):
        pass

    def _check_if_need_augment(self) :
        x = random.uniform(0,1) 
        return x<self.possibility
