def insertion_sort(arr) :
    n = len(arr);
    
    for i in range(n) :         # Time complexity = O(n^2)
        min_idx = i;
        for j in range(i+1,n):
            if(arr[j] < arr[min_idx]) :
                min_idx = j;
        
        swap = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = swap;
    
    
    
    for i in range(len(arr)) :
        print(arr[i]);
     
       
#insertion sort 
arr = [53,6,23,90,12,4,95];
insertion_sort(arr);
#printing the array after sorting the entire array

"""
#------------------------first iteration--------------------------
min_idx = 0
j = 1 to n
arr[1] < arr[0] (6 < 53) true then 
 min_idx = 1
 
arr[2] < arr[1] (23 < 6) false then skip the inner cond wala part

arr[3] < arr[1] (90 < 6) false 

arr[4] < arr[1] (12 < 6) false

arr[5] < arr[1] (4 < 6) true then 
{
    min_idx = 5 
}

arr[6] < arr[1] (95 < 6) false

after inner loop first traversal we gonna swap the ith index element and min_idx wala element

so we swap the arr[i] = 53 and arr[min_idx] = 6 and after that arr updated to [6,53,23,90,12,4,95]

#------------------------first iteration complete --------------------------
"""