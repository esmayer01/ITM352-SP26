# Ethan Mayer
# Feb. 10, 2026

# Create a list with different values
my_list = [1, "hello", 3.14, True, "world", 42, None]

if len(my_list) < 5:
    print(f"Small list: This list has {len(my_list)} elements (fewer than 5)")
elif len(my_list) >= 5 and len(my_list) <= 10:
    print(f"Medium list: This list has {len(my_list)} elements (between 5 and 10)")
else:
    print(f"Large list: This list has {len(my_list)} elements (more than 10)")

# Test 1: Small list (< 5 elements)
list1 = [1, 2, 3]
if len(list1) < 5:
    print(f"Small list: This list has {len(list1)} elements (fewer than 5)")
elif len(list1) >= 5 and len(list1) <= 10:
    print(f"Medium list: This list has {len(list1)} elements (between 5 and 10)")
else:
    print(f"Large list: This list has {len(list1)} elements (more than 10)")

# Test 2: Medium list (5-10 elements)
list2 = [1, 2, 3, 4, 5, 6, 7]
if len(list2) < 5:
    print(f"Small list: This list has {len(list2)} elements (fewer than 5)")
elif len(list2) >= 5 and len(list2) <= 10:
    print(f"Medium list: This list has {len(list2)} elements (between 5 and 10)")
else:
    print(f"Large list: This list has {len(list2)} elements (more than 10)")

# Test 3: Large list (> 10 elements)
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if len(list3) < 5:
    print(f"Small list: This list has {len(list3)} elements (fewer than 5)")
elif len(list3) >= 5 and len(list3) <= 10:
    print(f"Medium list: This list has {len(list3)} elements (between 5 and 10)")
else:
    print(f"Large list: This list has {len(list3)} elements (more than 10)")

# List of test cases: [test_list, expected_category]
test_cases = [
    # Small lists (< 5 elements)
    ([], "Small"),                              # Edge case: empty list
    ([1], "Small"),                             # 1 element
    ([1, 2, 3, 4], "Small"),                    # Boundary: 4 elements
    
    # Medium lists (5-10 elements)
    ([1, 2, 3, 4, 5], "Medium"),                # Boundary: exactly 5
    ([1, 2, 3, 4, 5, 6, 7], "Medium"),          # 7 elements
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Medium"), # Boundary: exactly 10
    
    # Large lists (> 10 elements)
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "Large"),  # Boundary: 11 elements
    (list(range(20)), "Large"),                       # 20 elements
    (list(range(100)), "Large")                       # 100 elements
]

# Run tests
print("Running test cases:\n")
for test_list, expected in test_cases:
    length = len(test_list)
    
    if length < 5:
        result = "Small"
    elif 5 <= length <= 10:
        result = "Medium"
    else:
        result = "Large"
    
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"{status}: List with {length} elements → {result} (expected {expected})")