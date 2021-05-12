def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range (p,r):
        if A[j]<=x:
            i=i+1
            t= A[i]
            A[i]=A[j]
            A[j]=t
    t= A[i+1]
    A[i+1]=A[r]
    A[r]=t
    return i+1

A=[5,2,9,7,4,3,1,8,10]
quicksort(A,0,len(A)-1)
print(A)
            
