
#%%


import numpy as np
import math

n0 = 1
nlayer = 1.5
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi


for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayer)/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/nlayer)*math.sin(sigmalayer)],
                   [(1j*nlayer)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    pay = (n0*m1[0][0] - nsub*m1[1][1] + nsub*n0*m1[0][1] - m1[1][0])
    payda = ( n0*m1[0][0] + nsub*m1[1][1] + nsub*n0*m1[0][1] + m1[1][0])

    r_s = pay/payda 

    print(r_s.imag)

# %%

import numpy as np
import math

n0 = 1
nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayerL)/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    pay = (n0*m1[0][0] - nsub*m1[1][1] + nsub*n0*m1[0][1] - m1[1][0])
    payda = ( n0*m1[0][0] + nsub*m1[1][1] + nsub*n0*m1[0][1] + m1[1][0])

    r_s = pay/payda 

    print(r_s.imag)

for k in range(0,101):
    laythic = k
    sigmalayer = (twopi*laythic*1e-9*nlayerH)/lamda

    m2 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m3 = np.matmul(m2,m1)


    pay = (n0*m3[0][0] - nsub*m3[1][1] + nsub*n0*m3[0][1] - m3[1][0])
    payda = ( n0*m3[0][0] + nsub*m3[1][1] + nsub*n0*m3[0][1] + m3[1][0])

    r_s = pay/payda 

    print(r_s.imag)


# %%

import numpy as np
import math

n0 = 1
nlayerL = 1.5
nlayerH = 2.4
nsub = 1.56028
lamda = 500e-9
twopi = 2*math.pi

for i in range(0,101):
    laythic = i
    sigmalayer = (twopi*laythic*1e-9*nlayerL)/lamda

    m1 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    pay = (n0*m1[0][0] - nsub*m1[1][1] + nsub*n0*m1[0][1] - m1[1][0])
    payda = ( n0*m1[0][0] + nsub*m1[1][1] + nsub*n0*m1[0][1] + m1[1][0])

    r_s = pay/payda 

    print(r_s.imag)

for k in range(0,101):
    laythic = k
    sigmalayer = (twopi*laythic*1e-9*nlayerH)/lamda

    m2 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m3 = np.matmul(m2,m1)


    pay = (n0*m3[0][0] - nsub*m3[1][1] + nsub*n0*m3[0][1] - m3[1][0])
    payda = ( n0*m3[0][0] + nsub*m3[1][1] + nsub*n0*m3[0][1] + m3[1][0])

    r_s = pay/payda 

    print(r_s.imag)


for l in range(0,101):
    laythic = l
    sigmalayer = (twopi*laythic*1e-9*nlayerL)/lamda

    m4 = np.array([[math.cos(sigmalayer),(1j/nlayerL)*math.sin(sigmalayer)],
                   [(1j*nlayerL)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m5 = np.matmul(m4,m3)

    pay = (n0*m5[0][0] - nsub*m5[1][1] + nsub*n0*m5[0][1] - m5[1][0])
    payda = ( n0*m5[0][0] + nsub*m5[1][1] + nsub*n0*m5[0][1] + m5[1][0])

    r_s = pay/payda 

    print(r_s.imag)

for t in range(0,101):
    laythic = t
    sigmalayer = (twopi*laythic*1e-9*nlayerH)/lamda

    m6 = np.array([[math.cos(sigmalayer),(1j/nlayerH)*math.sin(sigmalayer)],
                   [(1j*nlayerH)*math.sin(sigmalayer),math.cos(sigmalayer)]])

    m7 = np.matmul(m6,m5)


    pay = (n0*m7[0][0] - nsub*m7[1][1] + nsub*n0*m7[0][1] - m7[1][0])
    payda = ( n0*m7[0][0] + nsub*m7[1][1] + nsub*n0*m7[0][1] + m7[1][0])

    r_s = pay/payda 

    print(r_s.imag)




# %%
