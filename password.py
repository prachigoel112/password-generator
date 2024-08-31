import random
import string
passwordlen=15
charvalues=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(passwordlen):
  password+=random.choice(charvalues)

print("your random password is: ", password)