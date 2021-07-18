from pylab import plot, show, arange

plot([1,2,3,5,4],[1,1,2,39,5],'.:')

def paco(x):
  return x*x + 2*x - 3
  
xs = arange(-5,6,0.001)
ys = []

for x in xs:
  ys.append(paco(x))
  
plot(xs,ys,'*-')
  
show()