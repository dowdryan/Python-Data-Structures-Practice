def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    mapping = {')': '(', '}':  '{', ']': '['}
    stack = []
    for char in parens:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
            else:
                return True
    return not stack
                
