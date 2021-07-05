string = "abcbda"

def naiveLongestSubstring(s):
	if (len(s) <= 1):
		return len(s)
	longest = 0
	for left in range(0, len(s)):
		if (longest > len(s) - left - 1):
			break
		seen = set({})
		curr = 0
		for right in range(left, len(s)):
			if (s[right] not in seen):
				seen.add(s[right])
				curr += 1
				if (curr > longest):
					longest = curr
			else:
				break
	return longest

def longestSubstring(s):
	if (len(s) <= 1):
		return len(s)
	longest = 0
	left = 0
	seenChars = {}
	for right in range(0, len(s)):
		# See current char
		currChar = s[right]
		# Check if it is already seen
		prevChar = seenChars.get(currChar, None)
		# Check if value is greater than left
		if(prevChar is not None and prevChar >= left):
			#If yes set value to last position + 1
			left = seenChars[currChar] + 1
		#Add new char or update existing
		seenChars[currChar] = right
		#Find longest
		longest = max(longest, right - left + 1)
	
	return longest

print(longestSubstring(string))


