#!/usr/bin/env python3
import sys
a= sys.argv[1]
b=int(a)-3500

if b < 1500:
    c=b*0.03
elif b>=1500 and b<4500 :
    c=b*0.1-105
elif b>=4500 and b<9000 :
    c=b*0.2-555
elif b>=9000 and b<35000 :
    c=b*0.25-1005
elif b>=35000 and b<55000 :
    c=b*0.3-2705
elif b>=55000 and b<80000 :
    c=b*0.35-5505
else:
    c=b*0.45-13505

print(format(c,".2f"))