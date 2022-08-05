arr2 = [4,5,9,22,30,32,47]
values = [1,2,3,5,8,42,65536,91,684,98]
colors= ['purple', 'orange', 'green', 'grey', 'red', 'yellow']
def linearsearch(arr, goal):
  for i in range(0, len(arr)):
    if arr[i] == goal:
     print(i+ 1)
def binarysearch(arr, goal):
  steps = 0
  low = 0
  high = len(arr) - 1
  mid = int((low + high)/2)
  while low <= high:
    steps +=1
    if arr[mid] > goal:
      high = mid -1
      mid = int((low + high)/2)
    elif arr[mid]< goal:
      low = mid + 1
      mid = int((low + high)/2)
    elif arr[mid] == goal:
      break
      
  print('position is:', mid + 1,)
  print('Steps:', steps)
x = int(input('What to search for: '))
binarysearch(values,x)
