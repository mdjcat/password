import random
import string

print ("Hi, Welcome to Password Generator!")

# input the length of password
length = int(input("\nEnter the length of password:"))

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string. punctuation

# combine the data
all = lower + upper + num + symbols

# use random
temp = random.sample(all, length)

# create password
password = "".join(temp)

all = string.ascii_letters + string.digits + string.punctuation
password = "". join(random.sample(all, length))

print(password)