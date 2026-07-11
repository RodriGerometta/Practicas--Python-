"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

import os

os.system("cls")


def main(): 
    s = "(])"
    isValid(s)


def isValid(s: str) -> bool: 
    open = []
    for bracket in s:
        if bracket == "(" or bracket == "{" or bracket == "[":
            open.append(bracket)
        elif bracket == ")" or bracket == "}" or bracket == "]":
            if open == []:
                print("False")
                return False
            elif bracket == ")" and open[-1] == "(":
                open.pop(-1)
            elif bracket == "]" and open[-1] == "[":
                open.pop(-1)
            elif bracket == "}" and open[-1] == "{":
                open.pop(-1)
            else:
                print("False")
                return False
    
    if open == []:
        print("True")
        return True
    else:
        print("False")
        return False
    
# def isValid(self, s: str) -> bool:
#         stack = []
#         pairs = {")": "(", "]": "[", "}": "{"}

#         for bracket in s:
#             if bracket in pairs:  # es un bracket que cierra
#                 if stack == [] or stack[-1] != pairs[bracket]:
#                     return False
#                 stack.pop()
#             else:  # es un bracket que abre
#                 stack.append(bracket)

#         return stack == []


if __name__ == "__main__":
    main()
