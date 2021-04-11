from augment.Augment import Augment
import PIL
import cv2
import random
import numpy as np

# inherit from Augment
# add gasuss noise to the image
#   args:
#           mean(float): mean grey value of Gaussian noise
#                           range [0,1]
#           var(float): standard deviation of Gaussian noise
#           possibility(float): the possibility for fliping a picture 
#                               range [0,1]

class GasussNoise(Augment):
    def __init__(self,**args):
        self.mean=args['mean']
        self.var=args['var']
        super(GasussNoise, self).__init__(args['possibility'])
    
    def process(self, img):
        assert(type(img) == PIL.Image.Image)
        img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
        image = np.array(img/255, dtype=float)
        noise = np.random.normal(self.mean, self.var ** 0.5, image.shape)
        out = image + noise
        if out.min() < 0:
            low_clip = -1.
        else:
            low_clip = 0.
        out = np.clip(out, low_clip, 1.0)
        out = np.uint8(out*255)
        out =PIL.Image.fromarray(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
        return out