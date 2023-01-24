from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Hosting ip manzili
BACKEND_URL = env.str("BACKEND_URL")  # BACKEND_URL manzili
ADMIN_TOKEN = env.str("ADMIN_TOKEN")  # Admin tokeni

CHANNELS = ['-1001437339488']  # channels
