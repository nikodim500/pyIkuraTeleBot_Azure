
from bottle import route, view, run, request
import telegram
#TOKEN = '225635767:AAGEvQKd4Cj8wNN24wM5hpd8FlgiJPmky0A'  #IkuraBot
TOKEN = '468664268:AAEtyHluK_EpOyoWANgB8X74YxGf5TpvKXY'  #IkuraJrBot
APPNAME = 'pyikuratelebot.azurewebsites.net'
@route('/setWebhook')
def setWebhook():
    bot = telegram.Bot(TOKEN)
    botWebhookResult = bot.setWebhook(webhook_url='https://{}.azurewebsites.net/botHook'.format(APPNAME))
    return str(botWebhookResult)
@route('/botHook', method='POST')
def botHook():
    bot = telegram.Bot(TOKEN)
    update = telegram.update.Update.de_json(request.json, bot)
    bot.sendMessage(chat_id=update.message.chat_id, text=getSum(update.message.text, update.message.from_user.username))
    return 'OK'
def getSum(query, userName):
    try:
        splittedBySum = query.split('+')
        if len(splittedBySum) != 2:
            raise ValueError('Too complicated stuff')
        return str(int(splittedBySum[0]) + int(splittedBySum[1]))
    except:
        return  "I'm sorry, {}. I'm afraid I can't do that".format(userName)