def reverse_string_without_special_chars(s):
    # Convert the string to a list for easy character manipulation
    char_list = list(s)
    left, right = 0, len(char_list) - 1

    while left < right:
        # Skip non-alphabetic characters from the left
        while left < right and not char_list[left].isalpha():
            left += 1
        # Skip non-alphabetic characters from the right
        while left < right and not char_list[right].isalpha():
            right -= 1

        # Swap the characters
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    # Convert the list back to a string
    reversed_string = ''.join(char_list)
    return reversed_string

# Example usage
input_str = input()
output_str = reverse_string_without_special_chars(input_str)

print(f"{output_str}")
