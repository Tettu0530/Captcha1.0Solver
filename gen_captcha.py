import json
import os
import random
import string
import sys
import time

from captcha.image import ImageCaptcha


class InjusticeValue(Exception):
    pass


cap = ImageCaptcha(fonts=["Arialbd.ttf"])

def rand_gen(n: int):
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

if __name__ == "__main__":
    k = []
    i = int(input("How many images do you want to make?: "))
    delay = float(input("Please input delay: "))
    try:
        for n in range(1, i):
            data = rand_gen(5)
            f_name = f"{data}.png"
            cap.write(data, f"img/{f_name}")
            print(f"Successfully generated {f_name}!")
            time.sleep(delay)
    except TypeError:
        raise InjusticeValue("Illegal value detected.")