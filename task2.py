list1 = list(range(1, 11))
print("Original list:", list1)
list2 = list1[:5].copy()
print("Extracted first five elements:", list2)
list2 = list2[::-1]
print("Reversed extracted elements:", list2)