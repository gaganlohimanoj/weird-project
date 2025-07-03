import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAGG')
def insertionsort(a):
    n=len(a)
    for i in range (1,n):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
            print(a)
x=[34,46,43,27]
print("before sorting:",x)
insertionsort(x)
print("aftre sorting:",x)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.plot(x,x,label="actual time")
plt.title("Insertionsort-Time complexity is o(n^2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.legend()
plt.show()