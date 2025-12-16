import os
from dotenv import load_dotenv

load_dotenv()

# Required credentials
MANIFOLD_API_KEY = os.getenv("MANIFOLD_API_KEY")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# Trading parameters
MAX_BET = float(os.getenv("MAX_BET", 50))
KELLY_FRACTION = float(os.getenv("KELLY_FRACTION", 0.25))
MIN_EDGE = float(os.getenv("MIN_EDGE", 0.05))

# Hard constraint (contest requirement)
TARGET_CREATOR = "MikhailTal"

if MANIFOLD_API_KEY is None:
    raise EnvironmentError("MANIFOLD_API_KEY not found in environment")
