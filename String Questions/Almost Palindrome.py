string = "abcdecba" 

def validPalindrome(s, left, right):
	while(left < right):
		if (s[left] != s[right]):
			return False
		left += 1
		right -= 1
	return True

def almostPalindrome(s):
	left, right = 0, len(s) - 1
	while(left < right):
		if (s[left] != s[right]):
			return (validPalindrome(s, left+1, right) or validPalindrome(s, left, right-1))
		left += 1
		right -= 1
	return True

print(almostPalindrome(string))