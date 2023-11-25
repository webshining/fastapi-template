from environs import Env

env = Env()
env.read_env()

PORT = env.int('PORT', 4000)
HOST = env.str('HOST', "127.0.0.1")

DB_NAME = env.str('DB_NAME', default=None)
DB_USER = env.str('DB_USER', default=None)
DB_PASS = env.str('DB_PASS', default=None)
DB_HOST = env.str('DB_HOST', default=None)
DB_PORT = env.int('DB_PORT', default=None)


DATABASE_URI = env.str('DATABASE_URI', default='sqlite+aiosqlite:///database.sqlite3')
if DB_HOST and DB_PORT and DB_USER and DB_PASS and DB_NAME:
    DATABASE_URI = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
