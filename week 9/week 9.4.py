def christmasDiscount(n):
  discount = 0
  for digit in str(n):
      if int(digit) in [2, 3, 5, 7]:
         discount += int(digit)
  return discount
