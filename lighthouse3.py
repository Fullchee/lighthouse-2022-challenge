layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]
for i, row in enumerate(layout):
    if row[0] == "E" and row[1] == "e":
        print(i, 0)
    if row[-1] == "E" and row[-2] == "e":
        print(i, -1)
        
row = layout[3]
row.pop()
row.insert(len(row), "O")

print(layout)

