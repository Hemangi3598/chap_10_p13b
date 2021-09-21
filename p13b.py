#p3) write into a file
import os
filename = input("enter file name to write ninto ")
if os.path.exists(filename):
	f = None
	try:
		with open(filename, "a") as f:
		data = input(" enter data to written ") 
		f.write(data + "\n")
	except Exception as e:
		print("issue", e)
else:
	print(filename ," does not exists ")