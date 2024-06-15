def count_non_repeated_digits(n):
  """Counts the number of non-repeated digits in a given number.

  Args:
    n: The integer number to analyze.

  Returns:
    The count of non-repeated digits in the number.
  """

  digit_counts = {}
  for digit in str(n):
    digit_counts[digit] = digit_counts.get(digit, 0) + 1

  non_repeated_count = 0
  for count in digit_counts.values():
    if count == 1:
      non_repeated_count += 1

  return non_repeated_count
ts=int(input()) 
# Example usage:
print(count_non_repeated_digits(ts)) 
