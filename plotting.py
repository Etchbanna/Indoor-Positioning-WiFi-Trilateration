from trilateration import *
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np
#create Circle
def createCircle(x,y,r):
    circle=plt.Circle((x,y),radius=r, fill=False, color='blue')

    return circle
def showShape(patch):
    #get current access
    ax = plt.gca()
    ax.add_patch(patch)

    # plt.axis('scaled')                

# url = r"https://i.ibb.co/j8KSrdk/0-5dl-Or-U5n-GQs-Cu-ZVo.png"
url = r"https://i.ibb.co/ZLKPb0N/roomplan.png"
pic= plt.imread(url)
        # print(pic.shape)
fig =plt.figure()
ax = fig.subplots()
# ax.imshow(pic)
ax.imshow(pic, extent=[0, 6, 0, 5])
        
c1=createCircle(LatA,LongA,r1)
showShape(c1)

c2=createCircle(LatB,LongB,r2)
showShape(c2)
c3=createCircle(LatC,LongC,r3)
showShape(c3)
plt.plot(LatA,LongA,'ko',markersize=1.5)
plt.plot(LatB,LongB,'ko',markersize=1.5)
plt.plot(LatC,LongC,'ko',markersize=1.5)
lat,long=trilaterate(LatA,LongA,LatB,LongB,LatC,LongC,r1,r2,r3)

plt.plot(lat,long,'ro',markersize=2)
ax = plt.gca()
ax.set_xlim([0, 6])
ax.set_ylim([0, 5])
# plt.axis('scaled')                
print(lat,long)


plt.show()




# plt.show()