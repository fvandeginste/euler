import numpy as np
import scipy.linalg as sc
#from numpy import linalg as LA

from math import sqrt
def _ifactor(n):
    t , j = [], 2
    while n > 1:
        if (n % j) == 0:
            t.append(j)
            n //= j
        else:
            j += 1
    return t
 

def decomp(z):
    x=_ifactor(z)
    #print(x)
    l=[]
    # compteur pour repartir sur a et b les multiplicateurs
    for c in range(0,pow(2,len(x)+1)):
        a=1
        b=1
     # pour chaque multiplicateur
        for i in range(len(x)):
            #print(c,i,pow(2,i),pow(2,i)&c)
            if c & pow(2,i) > 0:
                a=a*x[i]
            else:
                b=b*x[i]
        #print("c",c)
        if (a,b) not in l:
            l.append((a,b))
    return l

print(str(sqrt(729)))
exit
allRac=[]
compteur=0
power10=2
pour=pow(10,power10)
racDelta=27
#while True:
Delta=racDelta*racDelta
for s in (-racDelta,racDelta):
    #print(D)
    racTho2s=12
#    while True:
    Tho2s=racTho2s*racTho2s
#    print ("racDelta",racDelta,"Tho2s",Tho2s,"racTho2s",racTho2s)
    for t in (-racTho2s,racTho2s):
        aplusd=t*t-2*s
        a=33
        d=aplusd-a
        bc=a*d-Delta
        print("d",d,"bc",bc)
        for couple in decomp(bc):
            (b,c)=couple
            compteur+=1
            #print(compteur,racDelta,racTho2s,couple,(a,b,c,d))
            if (a+s)/t>0 and b/t>0 and c/t>0 and (d+s)/t>0:
                if( a+s) %t == 0 and b % t == 0 and c % t == 0 and (d+s) % t == 0:
                    r = np.matrix([[(a+s)/t,b/t], 
                                        [c/t, (d+s)/t] 
                                        ])
                    print(a,b,c,d,r)
                    print("m",np.dot(r,r))
                    allRac.append(r)
 
        racTho2s+=1
#                if racTho2s>pour:
#                    break
racDelta+=1
#    if racDelta>pour:
#        break
print (len(allRac),compteur)
#print(allRac)
#            print("r",r)
#            print("m",np.dot(r,r))