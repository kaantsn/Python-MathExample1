import math

# Bir dairenin alanını hesaplayan fonksiyon
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Bir üçgenin hipotenüsünü hesaplayan fonksiyon
def calculate_triangle_hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

# Bir sayının faktöriyelini hesaplayan fonksiyon
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Örnek kullanım
radius = 5
a = 3
b = 4
num = 6

circle_area = calculate_circle_area(radius)
triangle_hypotenuse = calculate_triangle_hypotenuse(a, b)
factorial = calculate_factorial(num)

print("Dairenin Alanı:", circle_area)
print("Üçgenin Hipotenüsü:", triangle_hypotenuse)
print("Faktöriyel:", factorial)
