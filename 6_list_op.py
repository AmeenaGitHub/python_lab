# 6 

friends = ["Anjana", "Anjana", "Arun", "Salim", "Bhavana"]
lucky_numbers = [4, 8, 18, 36, 23, 10]
friends.sort()                 
lucky_numbers.sort()           
print("Sorted friends:", friends)
print("Sorted numbers:", lucky_numbers)
friends.extend(lucky_numbers)  
friends.append("John")         
friends.insert(1, "Meera")     
print("After extensions:", friends)
print("Index of Anjana:", friends.index("Anjana"))  
all_indices = [index for index, name in enumerate(friends) if name == "Anjana"]
print("All occurences (index): ", all_indices)
print("Count of Anjana:", friends.count("Anjana")) 
print("First element:", friends[0])        
print("Last element:", friends[-1])     
friends[1] = "Mike"           
print("Updated index 1:", friends[1])

starting_with_A = [name for name in friends if isinstance(name, str) and name.startswith("A")]
print("Filtered (Starts with A):", starting_with_A)
even_num = [num for num in friends if isinstance(num, int) and num % 2 == 0]
print("Filtered (Even numbers):", even_num)
uppercase_friends = [item.upper() for item in friends if isinstance(item, str)]
print("Manipulated (Uppercase names):", uppercase_friends)
friends.remove("Bhavana")      
friends.pop()                  
print("Before clear:", friends)
friends.clear()               
print("After clear:", friends)