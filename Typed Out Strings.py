s = "ab##" 
t = "c#d#"

def naiveTypedStrings(s, t):
	list1 = []
	for i in s:
		if i.isalpha():
			list1.append(i)
		elif i == "#":
			if len(list1) > 0:
				list1.pop()
	s = "".join(list1)
	list1.clear()
	for i in t:
		if i.isalpha():
			list1.append(i)
		elif i == "#":
			if len(list1) > 0:
				list1.pop()
	t = "".join(list1)

	if(s == t):
		return True
	else:
		return False

def typedStrings(S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1        
        ci = 0
        cj = 0
        
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    i -= 1
                    ci +=1
                elif ci > 0:
                    i -= 1
                    ci -= 1
                else:
                    break  
                    
            while j >= 0:
                if T[j] == "#":
                    j -= 1
                    cj +=1
                elif cj > 0:
                    j -= 1
                    cj -= 1
                else:
                    break
                    
            if i < 0: return j < 0            
            if j < 0: return i < 0                
            if S[i] != T[j]: return False
            i -= 1
            j -= 1             

        return True

print(typedStrings(s, t))
