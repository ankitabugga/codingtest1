#Write a Python function to count the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage:
my_list = [1, 6, 3, 6, 4, 6, 5]
element_to_count = 6
count = count_occurrences(my_list, element_to_count)
print(count)


# Output: 3
