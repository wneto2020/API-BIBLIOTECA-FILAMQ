import os
from dotenv import load_dotenv
load_dotenv()
info = {
    "EMAIL": os.environ.get("EMAIL"),
    "SENHA": os.environ.get("SENHA"),
    "URL_AMQP": os.environ.get("URL_AMQP"),
    "DATABASE": os.environ.get("DB_SQLITE")
}

