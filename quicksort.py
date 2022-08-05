arr = [2,5,3,1,4]
pivot = arr[-1]
def quicksort(arr):
  if(len(arr) >2):
    lessers = []
    greaters = []
    for i in range(0, len(arr)-1):
      if(arr[i] > pivot):
        greaters.append(arr[i])
      elif(arr[i] < pivot):
        lessers.append(arr[i])
    arr1 = lessers
    arr2 = greaters
    return quicksort(arr1).join''quicksort(arr2)
  else:
    return arr
    
print(quicksort(arr))
  