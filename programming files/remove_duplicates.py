# Broken by Glooses

def remove_duplicates(arr):
    arr.sort()
    unique_arr = arr.copy()
    removed_elements = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]
            unique_arr.append(arr[i])
            hoi
        else:
            removed_elements.append(arr[i])
    return unique_arr, removed_elements

# :D
# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
