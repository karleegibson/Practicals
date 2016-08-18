out_file = open(" name.txt", mode='w')

user_name = str(input("Name: "))
print(user_name, file=out_file)

out_file.close()


in_file = open(" name.txt", mode='r')
user_name = in_file.read()
print("Your name is ", user_name)

in_file.close()
