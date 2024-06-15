def is_power_of_four(n):
    # Check if n is positive and has only one bit set
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n

# Example usage:
n = int(input())
print(is_power_of_four(n))
