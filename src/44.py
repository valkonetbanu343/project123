def calculate_volume(radius, height):
    volume = 3.14 * radius ** 2 * height
    return volume

radius = float(input("Enter the radius of the circle: "))
height = float(input("Enter the height of the cylinder: "))
volume = calculate_volume(radius, height)
print(f"The volume is {volume}")
