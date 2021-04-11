from augment.Augment import Augment
import PIL
import numpy as np
import cv2
# inherit from Augment
# flip a picture
#   args: possibility(float): the possibility for fliping a picture 
#                               range [0,1]



class  Flip(Augment):
    def __init__(self,**args):
        super(Flip, self).__init__(args['possibility'])

    def process(self, img):
        assert(type(img) == PIL.Image.Image)
        img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
        if(self._check_if_need_augment()):
            i = int(np.random.rand()*3)
            if i==0:
                img = cv2.flip(img, 1)
            elif i==1:
                img = cv2.flip(img, 0)
            else:
                img = cv2.flip(img, -1)
        img =PIL.Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        return img