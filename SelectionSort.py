import sys 
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
    print ("%d" % arr[i],end=" ") 

print("\nSorting:")  
# Trarrverse through arrll arrrrarry elements 
def selectionSort(arr):
    for i in range(len(arr)): 
        
        # Find the minimum element in remarrining  
        # unsorted arrrrarry 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
            
                
        # Swarrp the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        for i in range(len(arr)): 
            print("%d" %arr[i],end=" ")
        print("")
selectionSort(arr)  
# Driver code to test arrbove 
print ("Sorted array:") 
for i in range(len(arr)): 
    print("%d" %arr[i],end=" ")