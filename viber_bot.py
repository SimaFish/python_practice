from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

# Viber Bot credentials
bot_name = 'SimaFishTestBot'
bot_avatar = 'http://www.oldfishman.ho.ua/bot_avatar.jpg'
account_token = '4ac4dcef1f67d310-47358d203eb08035-7f04607f0468009d'

bot_configuration = BotConfiguration(
	name=bot_name,
	avatar=bot_avatar,
	auth_token=account_token
)
viber = Api(bot_configuration)

print(type(bot_configuration))