import string
import random

class PasswordGenerator(object):
  def __init__(self):
    self.special_chars = list("!@#$%^&*()_+")
  
  def generate_password(self, length, special_chars=0, digits=0, uppercase=0, lowercase=0):
    password = []
    pool = ""
    count = special_chars + digits + uppercase + lowercase

    if count > length:
      raise ValueError("The sum of special_chars, digits, uppercase and lowercase must be less than or equal to length")

    if special_chars > 0:
      password.extend(random.sample(self.special_chars, special_chars))
      pool += "".join(self.special_chars)
    if digits > 0:
      password.extend(random.sample(string.digits, digits))
      pool += string.digits
    if uppercase > 0:
      password.extend(random.sample(string.ascii_uppercase, uppercase))
      pool += string.ascii_uppercase
    if lowercase > 0:
      password.extend(random.sample(string.ascii_lowercase, lowercase))
      pool += string.ascii_lowercase

    length = length - (special_chars + digits + uppercase + lowercase)

    for i in range(length):
      password.extend(random.sample(pool, 1))

    # shuffle again because we want to make sure that the password is not in the same order as when we appended it
    random.shuffle(password)
    return ''.join(password)

p = PasswordGenerator()
print(p.generate_password(10, special_chars=1, digits=1, uppercase=1, lowercase=1))
