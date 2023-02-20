height = int(input("What is the height of the tree? "))

tree_height = 1
tree_width = 1
space = (height - 1)
lower_space = (height - 1)

x = "#"

while True:
    if height <= 1:
        print("Okay, no tree!")
        break
    elif tree_height == (height + 1):
        print((" " * lower_space) + x)
        break
    if height > 1:
        print((" " * space) + (x * tree_width))
        tree_width += 2
        tree_height += 1
        space -= 1