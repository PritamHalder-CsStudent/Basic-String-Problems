# Determine whether the Expression is balanced or not.
# An expression is balanced if:

# Each opening bracket has a corresponding closing bracket of the same type.
# Opening brackets must be closed in the correct order.

# Example 1:
''' Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.'''

# Example 2:
''' Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.'''

# Approach :
# 1. create a empty stack 
# 2. Traverse the string:
        #  if you find a opening backet "({["  push(append) into the stack
        #  if you find the closing backet ")}]" :
                # if stack is empty --> not balanced
                # pop top element of the stack --> check if it matches the correct opening bracket.
                # if not match --> not balanced
                
# 3. After traversal :
        # If stack is empty --> Balanced 
        # else not Balanced                  


def balance_parenthesis(s):
    stack=[]
    pairs={ ')':'(' , '}':'{' , ']':'[' }
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1]!=pairs[ch]:  # not stack--> the stack is empty.stack[-1]-->gives top elements of the stack
                return False
            stack.pop()  # remove top element of the stack 
    if not stack:
        return True
    return False

print(balance_parenthesis("[{()]"))
                
                