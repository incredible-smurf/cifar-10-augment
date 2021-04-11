import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from data_loader import *
from augment.Spin import *



def imshow(img):
    img=img/2+0.5
    npimg=img.numpy()
    plt.imshow(np.transpose(npimg,(1,2,0)))
    plt.show()

# dataiter=iter(trainloader)
# images,labels=dataiter.next()
#
# imshow(torchvision.utils.make_grid(images))
# print(''.join('%5s' % classes[labels[j]] for j in range(4)))

if __name__ == '__main__':
    #the ways for augment
    augment_ways = Spin(angle=77,possibility=1)
    #if no dataset, change the parameter download to true to download the dataset
    trainset=CIFAR10(root=r'C:\Users\Administrator\Desktop\cifar-10-python',train=True,download=True,augment=augment_ways)
    testset=CIFAR10(root=r'C:\Users\Administrator\Desktop\cifar-10-python',train=False,download=True,augment=augment_ways)
    trainloader=torch.utils.data.DataLoader(trainset,batch_size=4,shuffle=True,num_workers=0)
    testloader = torch.utils.data.DataLoader(testset, batch_size=10,shuffle=False, num_workers=0)

    dataiter=iter(testloader)
    images,labels=dataiter.next()

    classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    print('ok') 
    print(' '.join('%5s' % classes[labels[j]] for j in range(10)))
    imshow(torchvision.utils.make_grid(images))
