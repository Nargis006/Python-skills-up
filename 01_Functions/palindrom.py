user_input = input("Enter a string: ")  # "racecar"


def normalize_text(text):
    # Normalization cost for all methods below:
    # Time: O(n), Space: O(n) because replace/lower create new strings.
    return text.replace(" ", "").lower()


def is_palindrome(text):
    # Two-pointer method.
    # Method-only complexity after normalization:
    # Time: O(n), Space: O(1)
    # Best choice for very large strings/paragraphs because it uses constant extra memory.
    cleaned = normalize_text(text)
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_slice(text):
    # Reverse using slicing.
    # Method-only complexity after normalization:
    # Time: O(n), Space: O(n) because cleaned[::-1] creates a full copy.
    # Good readability, but less memory-efficient for large text.
    cleaned = normalize_text(text)
    # Slice format is: string[start:stop:step].
    # Here, cleaned[::-1] means:
    # start = beginning from the end (default when step is negative),
    # stop = go until before the start of the string,
    # step = -1 (move one character backward each time).
    # Result: a new reversed string copy.
    return cleaned == cleaned[::-1]


def is_palindrome_reversed(text):
    # Reverse using reversed() iterator.
    # Method-only complexity after normalization:
    # Time: O(n), Space: O(n) because join builds a new reversed string.
    # Similar performance profile to slicing for large text.
    cleaned = normalize_text(text)
    # reversed(cleaned) does not return a string; it returns an iterator
    # that yields characters from last to first.
    # "".join(...) consumes that iterator and combines chars into
    # one new reversed string so we can compare with cleaned.
    return cleaned == "".join(reversed(cleaned))


def is_palindrome_recursive(text):
    # Recursive method: compare ends, then recurse on middle.
    # Method-only complexity after normalization:
    # Time: O(n), Space: O(n) due to recursion call stack.
    # Usually worst for very large strings; may hit recursion depth limits.
    cleaned = normalize_text(text)

    def check(start, end):
        if start >= end:
            return True
        if cleaned[start] != cleaned[end]:
            return False
        return check(start + 1, end - 1)

    return check(0, len(cleaned) - 1)


# Performance note for large strings/paragraphs:
# 1) Prefer is_palindrome (two-pointer) for best memory behavior.
# 2) Slice/reversed are simpler but allocate extra O(n) memory.
# 3) Recursive is mainly educational, not ideal for huge inputs.


print("two_pointer:", is_palindrome(user_input))
print("slice:", is_palindrome_slice(user_input))
print("reversed:", is_palindrome_reversed(user_input))
print("recursive:", is_palindrome_recursive(user_input))
       
