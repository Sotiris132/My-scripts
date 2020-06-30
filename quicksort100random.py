# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# Driver code to test above 
arr = [291, 80, 43, 226, 206, 204, 36, 112, 17, 137, 284, 298, 133, 300, 38, 107, 299, 183, 8, 152, 56, 217, 179, 110, 61, 73, 232, 228, 221, 119, 285, 202, 192, 195, 57, 225, 239, 86, 66, 247, 144, 58, 91, 120, 169, 41, 82, 2, 76, 173, 39, 102, 234, 34, 97, 29, 264, 159, 10, 65, 109, 68, 191, 171, 213, 15, 210, 16, 209, 50, 111, 178, 3, 49, 260, 62, 263, 242, 261, 227, 31, 168, 200, 219, 128, 193, 254, 160, 24, 129, 170, 12, 106, 187, 166, 124, 126, 81, 79, 296] 
n = len(arr) 
quickSort(arr,0,n-1) 
print (arr)
