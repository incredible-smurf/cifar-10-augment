from augment.Augment import Augment
import PIL
import random
class Spin(Augment):
    def __init__(self,**args):
        super(Spin,self).__init__(args['possibility'])
        self.angle=args['angle']
    
    def process(self,img):
        assert(type(img)==PIL.Image.Image)
        print(img,'1')
        if(self._check_if_need_augment()):
            img = img.rotate(self.angle)
        print(img,'2')
        return img

    


