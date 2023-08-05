import random
import string

def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase + ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str