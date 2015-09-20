validation = input("Enter your username: ")

real = "vyns"

def valid(u):
	if u != real:
		print('Username Incorrect')
	else:
		print('Hi,' + u)

valid(validation)
