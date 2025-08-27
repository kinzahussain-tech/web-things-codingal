def isPalindrome(string):
	left_position = 0
	right_position = len(string) - 1
	
	while right_position >= left_position:
		if not string[left_position] == string[right_position]:
			return False
		left_position += 1
		right_position-= 1
	return True

print("Is this a Palindrome?") 
print(isPalindrome('civic'))
