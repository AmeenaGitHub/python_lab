# 8 - Accepts comma separated numbers, display generated list and tuple, total num of elements, first and last element and the list in rev order.

num = input("Enter comma-separated numbers: ")
num_list = [int(i.strip()) for i in num.split(',')]
num_tuple = tuple(num_list)

print("List :", num_list)
print("Tuple :", num_tuple)
print("Total number of elements:", len(num_list))
print("First element:", num_list[0])
print("Last element:", num_list[-1]) #negative indexing-counts backward
print("List in reverse order:", num_list[::-1]) #slicing [start:stop:step] 