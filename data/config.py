from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
ADMINS_ID = env.list("ADMINS_ID")
MAIN_ADMIN = env("MAIN_ADMIN")

PGUSER = env("PGUSER")
PGPASSWORD = env("PGPASSWORD")
DB_NAME = env("DB_NAME")

IP = env("IP")
