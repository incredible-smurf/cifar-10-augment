from augment.Augment import Augment
import PIL
import random


# inherit from Augment
# rotate an image at a specific angle
class Spin(Augment):
    def __init__(self, **args):
        super(Spin, self).__init__(args['possibility'])
        self.angle = args['angle']

    def process(self, img):
        assert(type(img) == PIL.Image.Image)
        if(self._check_if_need_augment()):
            img = img.rotate(self.angle)
        return img
