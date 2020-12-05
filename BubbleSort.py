# Python program for implementation of Bubble Sort 
arr = []
inputComp = False
while inputComp==False:
    try:
        x = int(input("Please enter a number to be sorted:"))
        arr.append(x)
        checker = input('Are you done? y/n')
        if checker=="y":
            inputComp = True
    except ValueError:
        print("not a number ,try again:")
        continue
print("To be sorted:")
for i in range(len(arr)): 
    print ("%d" %arr[i],end=" ") 

print("\nSorting:")
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
        for i in range(len(arr)): 
            print ("%d" %arr[i],end=" ")
        print("")
  
# Driver code to test above   
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i],end=" ")