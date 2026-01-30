# Problem 30: Calculate area of circle
# Find and fix the error

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = input("Enter radius: ")
r = float(r)  # convert string to float
print(f"Area of the Circle: {area_of_circle(r)}")

