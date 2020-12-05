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
    print ("% d" % arr[i],end=" ") 

print("\nSorting:")
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
        
        for i in range(len(arr)): 
            print ("% d" % arr[i],end=" ") 
        print('')
  
insertionSort(arr)
# Driver code to test above  
print("Sorted list:")
for i in range(len(arr)): 
    print ("% d" % arr[i],end=" ") 
  
# This code is contributed by Mohit Kumra 