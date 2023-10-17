def linear_search(data, target_id):
    for i, id in enumerate(data):
        if id == target_id:
            return i  # Found, return the index
    return -1  # Not found

# Sample data
data = [1001, 1002, 1003, 1004, 1005]

# Target ID to search
target_id = 1009

# Perform linear search
result_linear = linear_search(data, target_id)

if result_linear != -1:
    print("ID", target_id, "found at index", result_linear)
else:
    print("ID", target_id, "not found")