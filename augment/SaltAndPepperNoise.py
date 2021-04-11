#椒盐噪声
from augment.Augment import Augment
import PIL
import cv2
import random
import numpy as np
# inherit from Augment
# add salt and pepper noise to the image
#   args:
#           ratio(float):the ration for adding salt and pepper noise
#                           range [0,1]
#           possibility(float): the possibility for fliping a picture 
#                               range [0,1]
class SaltAndPepperNoise(Augment):
    def __init__(self,**args):
        super(SaltAndPepperNoise, self).__init__(args['possibility'])
        self.ratio=args['ratio']

    def process(self, img):
        assert(type(img) == PIL.Image.Image)
        img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
        output = np.zeros(img.shape,np.uint8)
        thres = 1 - self.ratio
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                rdn = random.random()
                if rdn < self.ratio:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = img[i][j]
        output =PIL.Image.fromarray(cv2.cvtColor(output,cv2.COLOR_BGR2RGB))
        return output
    

