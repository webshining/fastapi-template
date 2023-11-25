from environs import Env

env = Env()
env.read_env()

PORT = env.int('PORT', 4000)

POSTGRES_USER = env.str('POSTGRES_USER', default=None)
POSTGRES_PASS = env.str('POSTGRES_PASS', default=None)
POSTGRES_HOST = env.str('POSTGRES_HOST', default=None)
POSTGRES_PORT = env.int('POSTGRES_PORT', default=None)
POSTGRES_NAME = env.str('POSTGRES_NAME', default=None)

DATABASE_URI = env.str('DATABASE_URI', default='sqlite+aiosqlite:///database.sqlite3')
if POSTGRES_USER and POSTGRES_PASS and POSTGRES_HOST and POSTGRES_PORT and POSTGRES_NAME:
    DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}'
