side_x = int(input("provide first side of rectangle :"))
side_y = int(input("provide second side of rectangle:"))

field = side_x * side_y

if field < 20:
    print(f"The field is small. Your field is{field}")
elif field >= 20 and field < 40:
    print(f"Your field is big. Your field is: {field}")
else:
    print(f"Your field is veery big. Your field is: {field}")