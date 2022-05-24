import math
import numpy
from ap_distance import ap_distance

LatA = 10
LongA = -5
r1 = ap_distance(-32,2400)
LatB = 30
LongB = 31
r2 =  ap_distance(-50,2400)
LatC = -10
LongC = 20
r3 = ap_distance(-72,2400)

def trilaterate(x1,y1,x2,y2,x3,y3,r1,r2,r3):
    A = 2*x2 - 2*x1
    B = 2*y2 - 2*y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2*x3 - 2*x2
    E = 2*y3 - 2*y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
    MyLat = (C*E - F*B) / (E*A - B*D)
    MyLong = (C*D - A*F) / (B*D - A*E)

    return MyLat,MyLong






