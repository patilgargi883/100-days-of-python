# Take input for both lists
list1 = list(map(int, input("Enter elements of first list (space-separated): ").split()))
list2 = list(map(int, input("Enter elements of second list (space-separated): ").split()))

# Merge and remove duplicates using set
merged_list = list(set(list1 + list2))

print("Merged list without duplicates:", merged_list)
