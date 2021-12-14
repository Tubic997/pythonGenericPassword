import string
from random import *

print("Vaša automatski generisana šifra je:")

characters = string.ascii_letters + string.digits + string.hexdigits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

password = "".join(choice(characters)for x in range(randint(10,20)))

print(password)