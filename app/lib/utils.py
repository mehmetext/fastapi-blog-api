import random
import string


def random_word(length: int) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))
