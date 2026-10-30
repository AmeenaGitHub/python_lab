# 7 - Sorting, merging, frequency counting, and identifying common or unique elements 

text = "apple banana apple cherry banana apple date"
words = text.split()

w_c = {}
for word in words:
    w_c[word] = w_c.get(word, 0) + 1

print("Dictionary Operations")
print("Word Frequencies:", w_c)

extra = {"berry": 2, "banana": 1}
merged_c = w_c.copy()
for key, value in extra.items():
    merged_c[key] = merged_c.get(key, 0) + value

print("Merged Frequencies:", merged_c)

sorted_by_freq = dict(sorted(merged_c.items(), key=lambda item: item[1], reverse=True))
print("Sorted by Frequency:", sorted_by_freq)

sorted_by_keys = dict(sorted(merged_c.items()))
print("Sorted by Keys:", sorted_by_keys)


a = {"Anjana", "Arun", "Salim", "Bhavana"}
b = {"Salim", "Bhavana", "Meera", "John"}

print("\nSet Operations")
print("A =", a)
print("B = ", b)

common = a.intersection(b) #a & b
print("A intersection B:", common)

only_inA = a.difference(b) #a - b
print("A - B:", only_inA)

non_overlapping = a.symmetric_difference(b) #a ^ b
print("Symmetric difference:", non_overlapping)

all = a.union(b) #`a or a | b
print("A U B:", all)
print("Sorted:", sorted(all))