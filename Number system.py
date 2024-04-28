def decimal_to_binary(decimal):
 return bin(decimal)[2:]
def binary_to_decimal(binary):
 return int(binary, 2)
def decimal_to_octal(decimal):
 return oct(decimal)[2:]
def octal_to_decimal(octal):
 return int(octal, 8)
def decimal_to_hexadecimal(decimal):
 return hex(decimal)[2:]
def hexadecimal_to_decimal(hexadecimal):
 return int(hexadecimal, 16)
print("Select conversion:")
print("1. Decimal to Binary")
print("2. Binary to Decimal")
print("3. Decimal to Octal")
print("4. Octal to Decimal")
print("5. Decimal to Hexadecimal")
print("6. Hexadecimal to Decimal")
while True:
 choice = input("Enter choice (1/2/3/4/5/6): ")
 if choice in ('1', '2', '3', '4', '5', '6'):
  num = input("Enter the number: ")
 if choice == '1':
  print("Binary:", decimal_to_binary(int(num)))
 elif choice == '2':
  print("Decimal:", binary_to_decimal(num))
 elif choice == '3':
  print("Octal:", decimal_to_octal(int(num)))
 elif choice == '4':
  print("Decimal:", octal_to_decimal(num))
 elif choice == '5':
  print("Hexadecimal:", decimal_to_hexadecimal(int(num)))
 elif choice == '6':
  print("Decimal:", hexadecimal_to_decimal(num))
 break
else:
 print("Invalid Input")
