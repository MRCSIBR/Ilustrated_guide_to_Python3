"""
Union: The union of two sets is a set that contains all the elements from both sets, without any duplicates.

Intersection: The intersection of two sets is a set that contains only the elements that are common to both sets.

Difference: The difference between two sets is a set that contains only the elements that are in one set but not the other.

Symmetric difference: The symmetric difference between two sets is aset that contains only the elements that are in one set or the other, 
but not both.
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
