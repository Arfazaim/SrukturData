def q_sort(a,low,high):
    if low<high:
        pivotpos=partition(a,low,high)
        q_sort(a,low,pivotpos-1)
        q_sort(a,pivotpos+1,high)
        
def partition(a,low,high):
    # Set pivot value as the first element
    pivotvalue = a[low]

    # Initialize pointers for up and down
    up=low+1
    down=high

    # Set flag to indicate when partitioning is complete
    done=False

    # Continue until partitioning is complete
    while not done:
        # Move up pointer until it reaches an element greater than pivot
        while up<=down and a[up]<=pivotvalue:
            up+=1

        # Move down pointer until it reaches an element less than pivot
        while down<=up and a[down]>=pivotvalue:
            down-=1

        # If pointers have crossed, partitioning is complete
        if down<up:
            done=True
        else:
            # Swap elements at up and down pointers
            temp=a[up]
            a[up]=a[down]
            a[down]=temp

    # Swap pivot element with element at down pointer
    temp=a[low]
    a[low]=a[down]
    a[down]=temp

    # Return index of pivot element
    return down
    
print("Masukkan Data:")
a=[int(x) for x in input().split()]
high=len(a)
q_sort(a,0,high-1)
print("Data yang telah diurutkan:",a)