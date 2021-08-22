from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMIN = env.list("ADMIN")
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов

PG_HOST = env.str("PG_HOST")  # Тоже str, но для айпи адреса хоста
PG_USER = env.str("PG_USER")
PG_PASS = env.str("PG_PASS")

AMPLITUDE_API_KEY = env.str("AMPLITUDE_API_KEY")
AMPLITUDE = "ON"