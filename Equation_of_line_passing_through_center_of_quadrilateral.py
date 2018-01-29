from numpy import ones, vstack;from numpy.linalg import lstsq;
print('Enter Coordinates for A, B, C and D such that quadrilateral ABCD has the base AB')
Ax=float(input('Enter Ax '));
Ay=float(input('Enter Ay '));
Bx=float(input('Enter Bx '));
By=float(input('Enter By '));
Cx=float(input('Enter Cx '));
Cy=float(input('Enter Cy '));
Dx=float(input('Enter Dx '))
Dy=float(input('Enter Dy '))
points=[((Ax+Bx)/2,(Ay+By)/2),((Cx+Dx)/2,(Cy+Dy)/2)]
x,y=zip(*points)
a=1;b=1
try:
    a=(x[0]-x[1])/(y[0]-y[1])
except:
    b=(y[0]-y[1])/(x[0]-x[1])
if a==0:
    print('Line is x= {m}'.format(m=x[0]))
elif b==0:
    print('Line is y= {m}'.format(m=y[0]))
else:
    A=vstack([x,ones(len(x))]).T
    m,c=lstsq(A,y)[0]
    print("Line is y={m}x+{c}".format(m=m,c=c))
