side_x = int(input("provide first side of rectangle :"))
side_y = int(input("provide second side of rectangle:"))

field = side_x * side_y

print(f"The field is small. Your field is{field}") if field < 20 else print(f"Your field is big. Your field is: {field}")