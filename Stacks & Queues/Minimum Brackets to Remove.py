s = "lee(t(c)o)de)"

def minRemoveToMakeValid(s):
	res = list(s)
	stack = []
	for i in range(0, len(res)):
		if (res[i] == "("):
			stack.append(i)
		elif (res[i] == ")" and len(stack) > 0):
			stack.pop()
		elif (res[i] == ")" and len(stack) == 0):
			res[i] = ""
		
	while(len(stack) > 0):
		currInd = stack.pop()
		res[currInd] = ""

	return ("".join(res))

print(minRemoveToMakeValid(s))