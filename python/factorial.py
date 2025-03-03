def factorial(num):
	# USING FOR-LOOP
	answer = 1
	for x in range(num, 0, -1):
		answer *= x
	return answer

	# USING RECURSION
    # if num == 0 or num == 1:
    #     return 1
    # return num * factorial(num - 1)
