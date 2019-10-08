colors = ['blue', 'red', 'green']
color_to_add = input("enter the color you want to add ")
colors.append(color_to_add)
print(*colors, sep=', ')