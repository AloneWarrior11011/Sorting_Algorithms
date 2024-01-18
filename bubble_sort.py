
def bubbleSort(arr) :
    n = len(arr);
    
    for i in range (n-1) : 
        for j in range (0,n-i-1) :
            if(arr[j] > arr[j+1]) :
                swap = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = swap;
                
    
    for i in range(n) :
        print(arr[i]);
        
# From here we're passing array to the bubble_sort function.
arr = [23,52,54,10,32,7,1];
bubbleSort(arr);

