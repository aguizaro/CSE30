def quickSort(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[ first]
   leftmark = first+1
   rightmark = last
   done = False
   count= 0
   while not done:
       while leftmark <= rightmark and alist[ leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[ rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           count+=1
           print(f'{count}: {alist[leftmark]}, {alist[rightmark]}')
           alist[ leftmark], alist[ rightmark] = alist[ rightmark],alist[ leftmark]       
   count+=1
   print(f'{count}: {alist[leftmark]}, {alist[rightmark]}')
   alist[ first], alist[ rightmark] = alist[ rightmark], alist[ first]
   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist,0,len(alist)-1)
print(alist)