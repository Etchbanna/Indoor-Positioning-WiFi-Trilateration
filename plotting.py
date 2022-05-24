import matplotlib.pyplot as plt
from trilateration import *
import numpy as np
from PIL import Image

im = plt.imread("https://i.ibb.co/j8KSrdk/0-5dl-Or-U5n-GQs-Cu-ZVo.png")
fig, ax = plt.subplots()
im = ax.imshow(im, extent=[0, 5000, 0, 3000])
ax.spines['top'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.set_xticks([])
ax.set_yticks([])
plt.plot(857,2168,'ro')
plt.plot(1149,783,'ro')
plt.plot(3191,1559,'ro')

plt.plot(trilaterate(LatA,LongA,LatB,LongB,LatC,LongC,r1,r2,r3),'ro')


plt.show()