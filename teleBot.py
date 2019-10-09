import telebot
import pyowm

token_bot_Shevnin="902452228:AAFxwaA2yilyGl7JppE3pwoe8545SDJ88Ns"
API_key_Shevnin='7c83d4d6fc0856c7a2ed516b47ebbabd'

token_bot_Sim="971477626:AAHYok-sna2mJ-UnkEYGGLlyNhcZBZ_1h-o"
API_key_Sim='9262eaa5e82b734436f39f3e9c42f0bd'

bot = telebot.TeleBot(token_bot_Shevnin)
owm = pyowm.OWM(API_key_Shevnin, language='ru')
def t_9(string):
    city = string
    with open("citys.txt", 'r', encoding='utf8') as citys:
        towns_list = []
        index_list = []
        maximum = 0
        for line in citys:
            towns_list.append(str(line))
            city1 = 0
            city2 = 0
            index = 0
            for i in city:
                if city[city1] == line[city2]:
                    index += 1
                    city1 += 1
                    city2 += 1
            index_list.append(index)

        for i in range(len(index_list)):
            if maximum < index_list[i]:
                maximum = index_list[i]
                index = i
        towns_list = [line.rstrip() for line in towns_list]
        string_ret = towns_list[index]

        return string_ret

@bot.message_handler(content_types=['text'])
def send_weather(message):
    #answer = "Добро пожаловать в weatherbot, напиши название города в котором ты находишься \n"
    inputs = message.text.lower()
    inputs = inputs.title()
    print(inputs)
    inputs = t_9(inputs)
    observation = owm.weather_at_place(inputs)
    status = observation.get_weather()
    wind = status.get_wind()["speed"]
    humidity = status.get_humidity()
    temp = status.get_temperature('celsius')["temp"]
    if status.get_detailed_status() =="ясно":
        emoji = "☀"
    elif status.get_detailed_status() =="слегка облачно":
        emoji = "🌤️"
    elif status.get_detailed_status() =="облачно":
        emoji = "🌥️"
    elif status.get_detailed_status() == "пасмурно":
        emoji = "☁"
    elif status.get_detailed_status() == "гроза":
        emoji = "🌩️"
    elif status.get_detailed_status() == "дождь":
        emoji = "🌧️"
    elif status.get_detailed_status() == "снег":
        emoji = "🌨️"
    else:
        emoji = "🌦️"

    answer = "В городе " + inputs + " сейчас: "+status.get_detailed_status() + emoji +"\n"
    answer += "Температура в районе: " + str(round(temp)) + "℃"+"\n"
    answer += "Скорость ветра: " + str(wind) + "м/с"+"\n"
    answer += "Влажность: " + str(humidity) + "%"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop = True)
