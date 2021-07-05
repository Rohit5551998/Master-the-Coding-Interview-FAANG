import re
def isPalindrome(self, s: str) -> bool:
  s = re.sub('[^A-Za-z0-9]','', s).lower()
  if len(s) <= 1:
    return True
  l = 0
  r = len(s) - 1 
  while(l < r):
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True