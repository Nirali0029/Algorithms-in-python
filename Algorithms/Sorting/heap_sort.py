def heapify(a,n,i):
  lr=i
  l=2*i+1
  r=2*i+2
  if l<n and a[i]<a[l]:
    lr=l
  if r<n and a[lr]<a[r]:
    lr=r
  if lr!=i:
    a[lr],a[i]=a[i],a[lr]
    heapify(a,n,lr)

def heap_sort(a):
  n=len(a)
  for i in range(n//2-1,-1,-1):
    heapify(a,n,i)

  for i in range(n-1,0,-1):
    a[i],a[0]=a[0],a[i]
    heapify(a,i,0)

a=[2,7,4,6,1,8,5]
heap_sort(a)
print(a)
