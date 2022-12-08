import math
import numpy

ordinary=[2,5,7,9,6,7]
own_name= [4,16,11,9,8]


grand_mean = 0
for val in ordinary:
    grand_mean += val
for val in own_name:
    grand_mean += val

grand_mean = grand_mean / (len(ordinary)+len(own_name))
print('grand mean=' , grand_mean)

m_ordinary=0
for val in ordinary:
    m_ordinary += val

m_ordinary = m_ordinary / len(ordinary)
print ('m_odinary' , m_ordinary)

m_own_name=0
for val in own_name:
    m_own_name += val

m_own_name = m_own_name / len(own_name)
print('m_own_name=' ,m_own_name)

print ('for ordinary')
ss_ordinary=0
for val in ordinary:
    print((val-m_ordinary)**2)
    ss_ordinary += (val-m_ordinary)**2
print("ss_ordinary=" , ss_ordinary)

print('for own name')
ss_own_name = 0
for val in own_name:
    print((val-m_own_name)**2)
    ss_own_name += (val-m_own_name)**2
print("ss_own_name=" , ss_own_name)


print ('for ordinary')
ss_total= 0
for val in ordinary:
    print((val-grand_mean)**2)
    ss_total += (val-grand_mean)**2

print ('for own name')

for val in own_name:
    print((val-grand_mean)**2)
    ss_total += (val-grand_mean)**2

print('ss_total=', ss_total)

ss_between= 0
for num in range(len(ordinary)+1):
    ss_between += (m_ordinary-grand_mean)**2

for num in range(len(own_name)+1):
    ss_between += (m_own_name-grand_mean)**2

print('ss_between=', ss_between)

ss_within = ss_own_name + ss_ordinary

print('ss_within=' ,ss_within)

print(.501/(math.sqrt((1-.501**2)/(11-2))))