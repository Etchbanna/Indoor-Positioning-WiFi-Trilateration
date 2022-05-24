import math
import numpy
from ap_distance import ap_distance
from scan_APs import scanAP_rssi
import subprocess

rssi1,rssi2,rssi3=scanAP_rssi('KARIM','Hisham','Abdelrahman')


LatA =857
LongA = 2169
r1 = ap_distance(rssi1,2400)
LatB = 1149
LongB = 783
r2 =  ap_distance(rssi2,2400)
LatC = 3191
LongC = 1559
r3 = ap_distance(rssi3,2400)

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

print(trilaterate(LatA,LongA,LatB,LongB,LatC,LongC,r1,r2,r3))









