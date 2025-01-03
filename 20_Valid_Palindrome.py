class Solution:
    def isValid(self, s: str) -> bool:
        openBracketStack = []

        for char in s:
            if char in ["(", "[", "{"]:
                openBracketStack.append(char)
            elif len(openBracketStack) <= 0:
                return False
            elif char == ")" and openBracketStack.pop() != "(":
                return False
            elif char == "]" and openBracketStack.pop() != "[":
                return False
            elif char == "}" and openBracketStack.pop() != "{":
                return False

        if len(openBracketStack) > 0:
            return False

        return True
