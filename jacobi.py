'''
27 x + 6 y – z = 85 ….. (1a)
6 x + 15 y + 2 z = 72 ….. (1b)
x + y + 54 z = 110 ….. (1c)
'''
def f1(y, z): 
    return (85-6*y+1*z)/27
def f2(x, z): 
    return (72-6*x-2*z)/15
def f3(x, y): 
    return (110-1*x-1*y)/54
x0 = 0
y0 = 0
z0 = 0
hitung = 1
e = 0.00001
kondisi = True
print('\nCount\tx\ty\tz\n')
x = 0
while kondisi == True:
    x1 = f1(y0,z0)
    y1 = f2(x0, z0)
    z1 = f3(x0, y0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (hitung, x1, y1, z1))
    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)
    hitung += 1
    x0 = x1
    y0 = y1
    z0 = z1
    x += 1
    kondisi = e1 > e and e2 > e and e3 > e
    print('\nSolusi: x=%0.3f, y=%0.3f dan z = %0.3f\n' % (x1, y1, z1))
