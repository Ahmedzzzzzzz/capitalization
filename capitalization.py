num = int(input("type a number: "))

odds = [x for x in range(num) if x % 2 != 0 ]
evens = [x for x in range(num) if x % 2 == 0]

print("odds:", odds)
print("evens:", evens)


fruits = input("type fruit names with space: ").split()

new_fruits = [f.capitalize() for f in fruits]

print("new fruits:", new_fruits)
