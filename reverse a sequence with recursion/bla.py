def swap(array,a,b):
    temp = array[a]
    array[a]= array[b]
    array[b] = temp

def reverse(S, start, stop):
    if start<stop-1:
        swap(S, start, stop-1)
        reverse(S, start+1, stop-1)

arr = [4,3,6,2,8,9,5]
print(arr)
reverse(arr,0, len(arr))
print(arr)
        