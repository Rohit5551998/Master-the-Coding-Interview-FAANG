parenthesis = {
	'(': ')',
	'[': ']',
	'{': '}'
}

def isValid(s):
	if (len(s) == 0):
		return True

	stack = []
	for i in range(0, len(s)):
		if (s[i] in parenthesis):
			stack.append(s[i])
		else:
			if len(stack) > 0:
				leftBracket = stack.pop()
				correctBracket = parenthesis[leftBracket]
				if (s[i] != correctBracket):
					return False
			else:
				return False
	return (len(stack) == 0)