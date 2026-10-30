# 5 - String processing operations
# 5.1 Character replacement, Counting character and word frequency

from collections import Counter
import string
og = "Apple have Apple color"
rep = og.replace("Apple", "Orange")
print("Original text: ", og)
print("Replaced text: ", rep)
ch_c = Counter(og.lower())
words = og.split()
w_c = Counter(words)
print("Word Frequency: ", dict(w_c))
print("Character Frequency: ", dict(ch_c))

# 5.2 String reversal  & Palindrome check

txt = input("Enter a string: ").lower()
print("Reverse = ", txt[::-1])
if txt == txt[::-1]:
    print(txt, "is Palindrome.")
else:
    print(txt, "is not Palindrome.")