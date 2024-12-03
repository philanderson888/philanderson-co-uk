date = "Thursday 14/07/22"
print(date)

first_names = ["BlueRay", "Upchuck", "Lojack", "Gizmo", "Do-rag"]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)

print("All 20 names using a for loop is: " + str(full_names))

# Thursday 14/07/22
# All 20 names using a for loop is: 
# ['BlueRay Zzz', 'BlueRay Burp', 'BlueRay Dogbone', 'BlueRay Droop', 
# 'Upchuck Zzz', 'Upchuck Burp', 'Upchuck Dogbone', 'Upchuck Droop', 
# 'Lojack Zzz', 'Lojack Burp', 'Lojack Dogbone', 'Lojack Droop', 
# 'Gizmo Zzz', 'Gizmo Burp', 'Gizmo Dogbone', 'Gizmo Droop', 
# 'Do-rag Zzz', 'Do-rag Burp', 'Do-rag Dogbone', 'Do-rag Droop']