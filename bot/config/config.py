import os
from dotenv import load_dotenv
import json

load_dotenv()


class Settings():
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    POINTS = json.loads(os.getenv("POINTS", "[700, 900]"))
    SWIPE_POINTS = json.loads(os.getenv("SWIPE_POINTS", "[2500, 3000]"))
    AUTO_PLAY_PUZZLE = os.getenv("AUTO_PLAY_PUZZLE", "False")

    USE_REF = os.getenv("USE_REF", 'False')
    REF_ID = os.getenv("REF_ID", '')
    
    USE_RANDOM_DELAY_IN_RUN = os.getenv("USE_RANDOM_DELAY_IN_RUN", "True")
    RANDOM_DELAY_IN_RUN = json.loads(os.getenv("RANDOM_DELAY_IN_RUN", "[5, 30]"))

    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", 'False')


settings = Settings()
