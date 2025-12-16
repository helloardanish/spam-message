from logging_config import get_logger
import time
from key_control import KeyControl
import pyperclip as ppc
import random
import string

logger = get_logger()

class App:
    def __init__(self):
        logger.info("App Operation Initiated")

        self.message = "Ku"
        self.kc_obj = KeyControl()
        self.repeat = 10

    def start(self):
        time.sleep(5)  # time to focus the target window
        ppc.copy(self.message)
        self.loop_type(self.repeat)

    def loop_type(self, n: int = 10):
        for i in range(n):
            logger.info(f"Paste and enter ({i+1}/{n})")
            # self.kc_obj.paste()        # Ctrl+V / Cmd+V
            time.sleep(0.01)
            # self.kc_obj.type(self.random_message())
            # self.kc_obj.type(self.random_website())
            self.kc_obj.type(self.generate_indian_number())
            time.sleep(0.01)
            self.kc_obj.press_enter() # parentheses


    def random_message(self, length=6):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def random_website(self):
        length = random.randint(4, 9)  # domain length constraint
        domain = ''.join(random.choices(string.ascii_lowercase, k=length))
        tld = random.choice([".com", ".net", ".org", ".io"])
        return f"https://www.{domain}{tld}"

    def generate_indian_number(self):
        country_code = "+91"
        prefixes = ["9", "8", "7", "6"]  # valid starting digits for Indian mobiles

        first_digit = random.choice(prefixes)
        remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))

        return f"{country_code}{first_digit}{remaining_digits}"


