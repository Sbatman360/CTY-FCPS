arr = [35,9,3,4,6,2,3,4,5,2,3]
def selection(arr):
  new = []
  for j in range(len(arr)):
    min = arr[0]
    for i in range(len(arr)):
      if arr[i] < min:
        min = arr[i]
    arr.remove(min)
    new.append(min)
  return new

def bubble(arr):
  noswap = 0
  while(noswap < len(arr) - 1):
    noswap = 0
    for i in range(0, len(arr)-1 ):
      if(arr[i] > arr[i+1]):
        arr[i], arr[i+1] = arr[i+1], arr[i]
      else:
        noswap += 1
  return arr
print(bubble(arr))
        
    
    
   
  
    
  