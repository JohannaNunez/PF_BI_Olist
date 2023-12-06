import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from dotenv import dotenv_values

env_config = dotenv_values(".env")

DB_CONNECTION_STRING = env_config.get("DB_CONNECTION_STRING")
API_TOKEN = env_config.get("API_TOKEN")