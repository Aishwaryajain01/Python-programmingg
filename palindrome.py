# Method 1: String Slicing
def is_palindrome_slicing(s):
    return s == s[::-1]

# Method 2: Two-Pointer Technique
def is_palindrome_two_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Method 3: Recursion
def is_palindrome_recursion(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursion(s[1:-1])

# Method 4: Using a Stack
def is_palindrome_stack(s):
    stack = list(s)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return s == reversed_s

# Method 5: Using the reversed() Function
def is_palindrome_reversed(s):
    return list(s) == list(reversed(s))

# Example usage
if __name__ == "__main__":
    test_strings = ["madam", "racecar", "hello", "level", "noon", "python", "radar"]

    for s in test_strings:
        print(f"Testing '{s}':")
        print(f"  Slicing: {is_palindrome_slicing(s)}")
        print(f"  Two-Pointer: {is_palindrome_two_pointer(s)}")
        print(f"  Recursion: {is_palindrome_recursion(s)}")
        print(f"  Stack: {is_palindrome_stack(s)}")
        print(f"  Reversed: {is_palindrome_reversed(s)}")
        print()  # Print a newline for better readability
