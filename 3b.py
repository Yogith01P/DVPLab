from difflib import SequenceMatcher
S1=input("Enter the first string:")
S2=input("Enter the second string:")
print(SequenceMatcher(None,S1,S2).ratio())