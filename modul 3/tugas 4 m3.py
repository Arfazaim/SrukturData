def binary_search(data, target_id):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] == target_id:
            return mid
        elif data[mid] < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Sample data (assumed to be sorted)
data = [1001, 1002, 1003, 1004, 1005]

# Target ID to search
target_id = 1007

# Perform binary search
result_binary = binary_search(data, target_id)

if result_binary != -1:
    print("ID", target_id, "found at index", result_binary)
else:
    print("ID", target_id, "not found")
