import os
from dataclasses import dataclass


import dotenv

@dataclass
class Tg_bot:
    token: str


dotenv.load_dotenv()

config = Tg_bot(token=os.getenv('Token_bot'))