class destructor:
	def __init__(self):
		print("hello moto")
	def __del__(self):
		print("terminated")
obj = destructor()
del obj
