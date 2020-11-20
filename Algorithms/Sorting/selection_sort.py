def selection(a):
  n=len(a)
  for i in range(n):
    min=i
    for j in range(i,n):
      if a[j]<a[min]:
        min=j
    if i!=min:
      a[i],a[min]=a[min],a[i]
  return a

a=[2,7,4,6,1,8,5]
print(selection(a))
