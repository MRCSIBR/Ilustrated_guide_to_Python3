
friends = ['Alice', 'Bob', 'Charlie', 'David']

common_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas']

"""

To find common names between the two lists, we can convert both lists into sets and use set operations. 

The intersection() method can be used to find the elements that are common to both sets. Here's an example:

"""

friends_set = set(friends)
common_names_set = set(common_names)
common_set = friends_set.intersection(common_names_set)

print(common_set)
