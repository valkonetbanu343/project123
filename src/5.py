import random
def get_random_code():
  code = ''
  while len(code) < 8:
    code += str(random.randint(0,9))
  return code