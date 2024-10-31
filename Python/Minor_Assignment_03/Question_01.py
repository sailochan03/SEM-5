def three_largest_digits(num):
   digits = list(map(int, str(num)))

   if len(digits) < 2:
      first = max(digits)
      print(f"{first}")
   elif len(digits) < 3:
      first = max(digits)
      digits.remove(first)
      second = max(digits)
      print(f"{first}, {second}")
   else:
      first = max(digits)
      digits.remove(first)
      second = max(digits)
      digits.remove(second)
      third = max(digits)
      print(f"{first}, {second}, {third}")

      

num = int(input("Enter a number: "))
three_largest_digits(num)