validation = input("Enter your username: ")

real = "Rey"

def valid(u):
	if u != real:
		print('Username Incorrect')
	else:
		print('Hi,' + u)

valid(validation)
