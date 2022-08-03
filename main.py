from find import find_index
import calculator as calc

# calculator
print(calc.add(1, 3))
print(calc.subtract(10, 3))
print(calc.divide(81, 9))
print(calc.multiply(6, 6))

# find
courses = ['History', 'Math', 'Physics']
print(find_index(courses, 'Physics'))