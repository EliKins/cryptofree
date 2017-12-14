import telebot
from telebot import types, logging
import requests

bot = telebot.TeleBot("418894977:AAFzUHXYKVlG6Vt1OIg26r4XL2KH5_p2tdk")

# Кнопки

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('1⃣ Начать 1⃣   ')
    bot.send_message(message.from_user.id, '👋 Приветствую {0}! Я чат-бот, который ознакомит тебя с Криптовалютой и научит зарабатывать огромные капиталы.\n\n'
                                           'В Чем моя уникальность ?\n\n'
                                           '- Ознакомлю с Криптовалютой\n'
                                           '- Пошагово обучу торговли на Биржах\n'
                                           '- Сформирую Ваш долгосрочный инвестиционный портфель\n'
                                           '- Предоставляю сигналы краткосрочных сделок\n'
                                           '- Буду курировать ваши действия /help'
                                           .format(message.from_user.first_name), reply_markup=user_markup)
    #bot.send_message(message.chat.id,wallet)
    #arh=wallet.archive_address('1P69cjBUWXT3qvGJCcLmqjXVqqCtWzKorQ')
    #print(str(stats))


@bot.message_handler(commands=['help'])
def handle_help(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать в Тех.Поддержку", url="https://telegram.me/cryptonowhelp")
    keyboard.add(url_button)
    bot.send_message(message.chat.id,
                     "Если все вышеперечисленное вам не помогло, обращайтесь в тех.поддержку", reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def handle_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('🅱 Биткоин', '🅰 Альткоины')
    user_markup.row('🎥 Видео 🎥', '💰 Кошельки 💰')
    user_markup.row('📈 Курсы 📈', '📑 Биржа 📑')
    user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎')
    user_markup.row('❗ Новости ❗', '☎ Контакты ☎')
    bot.send_message(message.from_user.id, "Вы вернулись в начальное меню.", reply_markup=user_markup)


@bot.message_handler(commands=['mvideo'])
def handle_mvideo(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('🎥 Видео инструкция')
    user_markup.row('🎥 Открытие Ilgamos в Украине')
    user_markup.row('🎥 Всё о биткоине')
    user_markup.row('🎥 Цельные советы')
    user_markup.row('🔙 Вернуться')
    bot.send_message(message.from_user.id, "Выберите видео информацию, которая вас интересует.",reply_markup=user_markup)

def get_btc(): #Показує реальний курс бітка
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    r = requests.get(url).json()
    price = r['ticker']['last']
    return str(price) + ' USD'

def get_ltc():  # Показує реальний курс бітка
   url = 'https://yobit.net/api/2/ltc_usd/ticker'
   r = requests.get(url).json()
   price = r['ticker']['last']
   return str(price) + ' USD'

def get_eth():  # Показує реальний курс бітка
   url = 'https://yobit.net/api/2/eth_usd/ticker'
   r = requests.get(url).json()
   price = r['ticker']['last']
   return str(price) + ' USD'

def get_dash():  # Показує реальний курс бітка
   url = 'https://yobit.net/api/2/dash_usd/ticker'
   r = requests.get(url).json()
   price = r['ticker']['last']
   return str(price) + ' USD'


        ##################################1
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text=='1⃣ Начать 1⃣':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('🅱 Биткоин', '🅰 Альткоины')
        user_markup.row('🎥 Видео 🎥', '💰 Кошельки 💰')
        user_markup.row('📈 Курсы 📈', '📑 Биржа 📑')
        user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎')
        user_markup.row('❗ Новости ❗', '☎ Контакты ☎')
        bot.send_message(message.from_user.id, 'О биткоине ', reply_markup=user_markup)
    elif message.text == '🅱 Биткоин': #1
            user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            user_markup.row('Особености')
            user_markup.row('Принцип роботы')
            user_markup.row('Международный Форум')
            user_markup.row('🔙 Вернуться "Главное меню"')
            bot.send_message(message.from_user.id, 'Что такое биткоин и в чём его особенность ? Биткойн (BTC, Bitcoin) \n'
                                                   '-  децентрализованная система цифровой валюты, которая использует одноименную '
                                                   'расчетную единицу. \n'
                                                   'Главной целью разработчиков биткоина  было создание новой системы полностью '
                                                   'необратимых сделок, где электронные платежи между  сторонами происходит без '
                                                   'вмешательства  банковских, налоговых, судебных и каких либо других \n'
                                                   'административных  органов. Соответственно никто не может заблокировать, оспорить или '
                                                   'принудительно совершить транзакцию. \n\n'
                                                   'Чтобы обеспечить успешное функционирование и защитить систему от '
                                                   'взломов  используются криптографические методы. Для прозрачности каждой сделки '
                                                   'информация о транзакциях не шифруется и всегда доступна.\n\n'
                                                   'Прогресс пошел настолько далеко , что теперь  Биткойн можно  использовать для обмена '
                                                   'на товары, услуги, и рассчитываться в магазинах вместо наличных денег.\n\n'
                                                   , reply_markup=user_markup)
    elif message.text=='Особености': #1.1
        bot.send_message(message.chat.id, "•	Bitcoin  можно  использовать без предоставления конфиденциальных данных. \n"
                                          "•	Пересылать в любом количестве, на любой адрес, в любую страну. Без запретов и "
                                          "лимитов.\n"
                                          "•	Использовать в качестве оплаты для онлайн и оффлайн покупок. Список организаций, "
                                          "принимающих биткоин, постоянно растет.\n"
                                          "•	Использовать в путешествиях, снижая потери на комиссиях и кросскурсах.\n"
                                          "•	Использовать в качестве инвестиций или способа сохранения капитала.\n"
                                          "•	Покупать или продавать, используя любую валюту. Узнать подробнее - команда /howtobuy \n"
                                          "У злоумышленников не получится напечатать Bitcoin  - количество монет заранее известно, 21 000 "
                                          "000 - и они появляются в сети строго по заранее известному алгоритму;\n\n"
                                          "Не выйдет уничтожить  Bitcoin  - все компьютеры, находящиеся в сети, заменяют единый центр, "
                                          "а  целостность цепочки блоков от разного вида атак защищена этой большой компьютерной "
                                          "сетью;\n\n"
                                          "Как бы вы не старались у вас не получиться изменить исходный код без согласия большей части "
                                          "сообщества - как условия появления количества монет, так любые другие правила;\n\n"
                                          "Невозможно заблокировать или арестовать -  Bitcoin контролирует только тот, кто имеет прямой "
                                          "доступ к кошельку. Чтобы арестовать кошелек Bitcoin, нужно сначала арестовать его хозяина.\n\n"
                                          "Также никак не получиться подделать или потратить дважды - в системе используются "
                                          "специальные криптографические ключи, которые подтверждаются цепочкой блоков – главной "
                                          "учетной книгой системы.\n\n")
    elif message.text=='Принцип роботы': #1.2
        bot.send_message(message.chat.id, "https://bitcoin.org – Официальный сайт\n")
        bot.send_message(message.chat.id, "Кратко о bitcoin (2 мин) : https://youtu.be/IdWgvOxjYi8 \n")
        bot.send_message(message.chat.id, "Техническая часть bitcoin (22 мин) - https://youtu.be/RuZ80TPUF_A \n\n")
    elif message.text=='Международный Форум': #1.3
        bot.send_message(message.chat.id, "Вам не придется больше искать ответы на свои вопросы у ненадежных источников, "
                                          "обратите внимание на  русский раздел крупнейшего криптовлаютного форума. \n\n"
                                          "Это поистине гигантская копилка коллективных знаний с 2010 года. Где вы можете найти "
                                          "ответы на все ваши вопросы.\n"
                                          "https://bitcointalk.org/index.php?board=10.0 \n\n")
    elif message.text=='🔙 Вернуться "Главное меню"': #1.6
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('🅱 Биткоин', '🅰 Альткоины')
        user_markup.row('🎥 Видео 🎥', '💰 Кошельки 💰')
        user_markup.row('📈 Курсы 📈', '📑 Биржа 📑')
        user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎')
        user_markup.row('❗ Новости ❗', '☎ Контакты ☎')
        bot.send_message(message.from_user.id, "Вы вернулись в начальное меню.", reply_markup=user_markup)
    elif message.text=='🅰 Альткоины': #2
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('❓ Сколько я мог заработать')
        user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Альткоины -  называют все остальные криптовалюты, которые надеются либо "
                                               "заменить биткоин, либо улучшить по меньшей мере хотя бы один из его параметров. \n"
                                               "В мире их больше 800 и они стремительно увеличивают свое \n"
                                               "количество.  https://coinmarketcap.com/currencies/views/all/ \n"
                                               "Чем нам интересны Альткоины ? На них можно заработать огромные проценты, как на начале "
                                               "с bitcoin. \n\n", reply_markup=user_markup)
    elif message.text=='❓ Сколько я мог заработать':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('📚 Посмотреть отзывы 📚')
        user_markup.row('Сколько я могу зароботать?')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, 'Вам интересно во сколько превратилась бы ваша 1000 дол, если бы вы приобрели в свое '
                                          'время популярные сейчас Криптовалюты? (фото). Еще не поздно, Присоединяйтесь к нам и '
                                          'позвольте сделать Вам большую прибыль.\n\n' , reply_markup=user_markup)
    elif message.text=='🎥 Видео 🎥': #2
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('🎥 Краткие Видео')
        user_markup.row('🎥 Большие Видео')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Мы собрали самые актуальные и интересные видео со всего мира.", reply_markup=user_markup)
    elif message.text=='🎥 Краткое Видео':
        bot.send_message(message.chat.id, 'Not')
    elif message.text=='🎥 Большое Видео':
        bot.send_message(message.chat.id,'Not')
    elif message.text=='💰 Кошельки 💰': #6
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('💰 Список холодных')
        user_markup.row('💰 Список горячих')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, 'На волне пристального внимания к криптовалютам создаются десятки новых '
                                               'проектов, включая криптокошельки. Хотя скептики указывают на недолговечность '
                                               'многих начинаний, ведь существуют лишь централизованные кошельки, а '
                                               '«централизованный» — слово, не совсем подходящее для блокчейна.\n'
                                               'Все кошельки делятся на «горячие» и «холодные».  «Горячие» кошельки это те к '
                                               'которым есть постоянный  онлайн доступ , а «Холодные» кошельки можно '
                                               'извлекать (например устанавливать на флешки ). \n\n',
                         reply_markup=user_markup)
    elif message.text=='💰 Список холодных':
        bot.send_message(message.chat.id, 'Одним из самыхпопулярных холодных кошельков является - electrum\n\n')
    elif message.text=='💰 Список горячих':
        keyboard = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="Holy Transaction", url="https://holytransaction.com")
        url_button2 = types.InlineKeyboardButton(text="Coins Bank", url="https://coinsbank.com")
        url_button3 = types.InlineKeyboardButton(text="Bit AC", url="http://www.bitac.net")
        url_button4 = types.InlineKeyboardButton(text="Bit GO", url="https://www.bitgo.com")
        keyboard.add(url_button1,url_button2,url_button3,url_button4)
        bot.send_message(message.chat.id, 'Представим вашему вниманию небольшой перечень «горячих» кошельков.\n\n'
                                          'По мнению многих специалистов -  Holy Transaction наиболее надежный и '
                                          'удобный для начинающих веб-кошелек . Он поддерживает 9 криптовалют, '
                                          'двухфакторную аутентификацию: «горячий» и «холодный» доступ, а '
                                          'помощь в интеграции API с достойной поддержкой.\nПрактически '
                                          'бесплатен — очень низкие тарифы на обмен и мгновенный перевод.\n\n'
                                          'Coinomi - второй по популярности сервис. Бесплатен, основан на открытом '
                                          'коде, имеет внушительный список из 43 криптовалют, инструмент обмена и '
                                          'бэкап в HD wallet; полностью анонимный и мультиязычный (включая русский '
                                          'язык). Ключи хранит пользователь, а доступ к кошельку осуществляется по '
                                          'ключевому слову.\n\n\n'
                                          'CoinsBank — новый, но любопытный сервис. Он позиционирует себя как '
                                          'криптобанк и выпускает чипованные предоплаченные карты Visa в разных '
                                          'вариантах. Предлагает свою трейдинговую платформу, мобильные '
                                          'приложения и решения для электронной торговли.\nСудя по активной работе с '
                                          'рублями (помимо долларов и британских фунтов) и сотрудничеству с Qiwi, '
                                          'проект развивают наши соотечественники.\n\n\n'
                                          'BITAC -запущенный в марте 2016 года мультивалютный криптокошелек: 15 '
                                          'валют, судя по данным в личном кабинете, хвалят за неплохие курсы обмена и '
                                          'реферальную программу, дающую до 50% отчислений. Как сказано на сайте, '
                                          'проект создан Биткойн-энтузиастами и специалистами по информационной '
                                          'безопасности (видимо, UI-дизайнеров среди них не оказалось).\nПредлагает '
                                          'мгновенный обмен, Android-приложение, API, двухфакторную аутентификацию '
                                          'и оперативную техподдержку.\n\n\n'
                                          'BitGo -биткойн-кошелек BitGo дает клиентам возможность проведения '
                                          'мгновенных Биткойн-платежей через блокчейн-хранилище. По данным '
                                          'компании, в месяц сервис обрабатывает около 300 тысяч транзакций на '
                                          'общую сумму в 1 млрд долларов США. Высокая скорость проведения операций '
                                          'обеспечивается за счет использования собственной разработки компании — '
                                          'BitGo Instant, позволяющей принимать Биткойн-транзакции еще до того, как '
                                          'они будут официально подтверждены в блокчейне. Аутентификация '
                                          'пользователей осуществляется через криптотокены в соответствии с '
                                          'положениями альянса «быстрой онлайн идентификации» FIDO (Fast IDentity '
                                          'Online). \n\n',reply_markup=keyboard)
    elif message.text=='📈 Курсы 📈': #7
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('Web-сервисы')
        user_markup.row('Мобильные сервисы')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, 'Цена на все Криптовалюты абсолютно разная и не стабильная. Поэтому, вам постоянно нужно '
                                               'быть в курсе всех событий на рынке, так как на разнице в курсе можно заработать \n'
                                               'Сумасшедшие деньги.\n\n'
                                               'Курсы самых известных валют: \n'
                                               'BTC - {0}\n'
                                               'LTC - {1}\n'
                                               'ETH - {2}\n'
                                               'DASH - {3}\n'.format(get_btc(),get_ltc(),get_eth(),get_dash()), reply_markup=user_markup)
    elif message.text== 'Web-сервисы':
        bot.send_message(message.chat.id, 'Обратите внимание на список самых популярные Веб-сервисов, которые позволят вам всегда '
                                          'быть в курсе дела, быть в ТРЕНДЕ! \n\n')
        bot.send_message(message.chat.id,'https://coinmarketcap.com/ - Мониторинг всех Бирж\n\n')
        bot.send_message(message.chat.id,'https://poloniex.com/exchange#btc_bts - Биржа\n\n')
        bot.send_message(message.chat.id,'https://bittrex.com/Home/Markets - Биржа\n\n')
    elif message.text =='Мобильные сервисы': #9
        bot.send_message(message.chat.id, 'IOS Iphone|Ipad\n\n'
                                          '1.	Blockfolio - https://appsto.re/ua/n2ptbb.i (советуем)\n'
                                          '2.	Bitcoin Ticker -  https://appsto.re/ru/dZvpA.i  (советуем)\n'
                                          '3.	Polo (мобильная биржа Poloniex) - https://appsto.re/ua/D93Jjb.i \n'
                                          '4.	Polofolio https://appsto.re/ua/vd2lkb.i \n\n'
                                          'Android\n\n'
                                          '1.	Blockfolio - https://play.google.com/store/apps/details?id=com.blockfolio.blockfolio\n'
                                          '2.	Bitcoin Ticker -  https://play.google.com/store/apps/details?id=st.brothas.mtgoxwidget \n'
                                          '3.	Polo (мобильная биржа Poloniex) https://play.google.com/store/apps/details?id=jonathan.veg.poloniextracker \n\n')
    elif message.text =='📑 Биржа 📑': #9
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('Большие международные')
        user_markup.row('Украина','Россия')
        user_markup.row('Казахстан')
        user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "В мире есть множество Крипто-бирж но как в любой индустрии есть лидеры, с "
                                               "большими оборотами и клиентскими базами. Все биржи «условно» делятся на "
                                               "Большие, средние и малые. \n"
                                               "Перед новичком стоит выбор какую же биржу мне использовать для торгов ? Конечно "
                                               "нужно выбирать самые большие, надежные и стабильные биржи, от этого зависит "
                                               "скорость обработки ваших ордеров на покупку или продажу, сохранность и "
                                               "безопасность ваших монет.\n\n", reply_markup=user_markup)
    elif message.text == 'Большие международные':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('Poloniex(рекомендуем)')
        user_markup.row('Btc-e','Kraken')
        user_markup.row('Bittrex','Exmo')
        user_markup.row('🔙 Вернуться "Главное меню"' )
        bot.send_message(message.from_user.id, '.', reply_markup=user_markup)
    elif message.text=='Украина':
        bot.send_message(message.chat.id, 'Биржи такого формата рекомендуем использовать только для Ввода или Вывода \n'
                                          'Криптовалюты на Гривну. \n\n'
                                          '1.	https://btc-trade.com.ua/\n'
                                          '2.	https://exmo.com \n'
                                          '3.	Список обменников работающих PrivatBant - BTC \n'
                                          'https://www.bestchange.ru/privat24-uah-to-bitcoin.html \n\n')
    elif message.text=='Россия':
        bot.send_message(message.chat.id, 'Биржи такого формата рекомендуем использовать только для Ввода или Вывода \n'
                                          'Криптовалюты на Рубль. \n\n'
                                          '1.	http://YoBit.Net\n'
                                          '2.	http://EXMO.com \n'
                                          '3.	Список обменников работающих СберБанк - BTC \n'
                                          'https://www.bestchange.ru/sberbank-to-bitcoin.html \n\n')
    elif message.text=='Казахстан':
        bot.send_message(message.chat.id, 'Биржи такого формата рекомендуем использовать только для Ввода или Вывода \n'
                                          'Криптовалюты на Рубль/Тенге. \n\n'
                                          '1.	https://1wm.kz\n'
                                          '2.	https://pmcash.kz/  \n'
                                          '3.	Список обменников работающих СберБанк - BTC\n'
                                          'https://www.bestchange.ru/sberbank-to-bitcoin.html \n\n')
    elif message.text =='💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎': #10
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('📚 Посмотреть отзывы 📚')
        user_markup.row('Сколько я могу зароботать?')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Мы удивим вас если Вы профессионал и обучим - если Новичек.\n\n"
                                               "Мы собрали для вас поток информации  из 16 проверенных источников. Наша "
                                               "команда постаралась объединить информацию со всего мира, от Запада до "
                                               "Востока. Также мы напрямую общаемся с Крупными игроками на биржах, "
                                               "Собственниками фондов и самых больших Майнинговых ферм. И теперь готовы "
                                               "делится этой информацией с Вами.\n\n"
                                               "Наш Чат-Бот\n\n"
                                               "- Пошагово научит торговли на Биржах\n"
                                               "- С формирует Ваш долгосрочный инвестиционный портфель\n"
                                               "- Предоставит сигналы краткосрочных сделок\n"
                                               "- Будет курировать ваши действия\n\n"
                                               "Будем делать Вам деньги или ознакомимся с Нашими отзывами ? \n\n", reply_markup=user_markup)
    elif message.text =='Сколько я могу зароботать?':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать 📄')
        user_markup.row('🔙 Вернуться')
        bot.send_message(message.from_user.id, "Вы заметили какими темпами развивается индустрия криптовалют и сколько "
                                               "людей заработали миллионы $ ? Как показывает практика результат с нашей "
                                               "помощью - Минимум 1000% за Год и Максимума не существует.\n\n"
                                               "      *Давайте предположим что средний результат будет\n 3000%/ год, при  вашей"
                                               "максимальной Активности.\n\n"
                                               "      Ваша сумма  Инвестиции                  Через год\n"
                                               "      1000$                                                            30 000$\n"
                                               "      5000$                                                            150 000$\n"
                                               "      10 000$                                                         300 000$\n"
                                               "      50 000$                                                         1 500 000$\n", reply_markup=user_markup)
    elif message.text== '🔙 Вернуться':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('📚 Посмотреть отзывы 📚')
        user_markup.row('Сколько я могу зароботать?')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Вы вернулись в меню '💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎' ", reply_markup=user_markup)
    elif message.text=='📚 Посмотреть отзывы 📚': #10.2
        bot.send_message(message.chat.id, "Предоставляем краткую подборку наших отзывов")
    elif message.text=='📄 Начать роботу 📄': #10.3
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к платному боту", url="https://telegram.me/ilgTestbot")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Для активации Всех параметров Вам нужно проплатить месячную подписку на нашем платном боте для "
                                               "использования нашего Полного функционала.\n Сколько вы готовы заплатить за "
                                               "информацию Которая поможет вам сделать от 1000% до 10 000% за Год ?\n Не "
                                               "упустите ваш реальный Шанс сделать Миллионером. \n\n"
                                               "Для перехода на нашего бота нажмите ссылку внизу\n\n\n", reply_markup=keyboard)
    elif message.text=='❗ Новости ❗':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Канал Crypto-Now Club", url="https://telegram.me/cryptonowclub")
        url_button1= types.InlineKeyboardButton(text="Сайт Crypto-Now Club", url="https://crypto-now.club")
        keyboard.add(url_button,url_button1)
        bot.send_message(message.chat.id,"Перейдя на наш канал, вы будете постоянно получать новые уведомления о криптобирже.\n"
                                         "Перейдя на наш сайт, вы изучите полностью всю информацию.", reply_markup=keyboard)
    elif message.text =='☎ Контакты ☎': #11
        bot.send_message(message.chat.id, 'Trali-Vali')




    print(bot.get_me())

    def log(message, answer):
        print("\n ---------------------")
        from datetime import datetime
        print(datetime.now())
        print("Сообщение от {0} {1}. (id={2}) \n Текст- {3}".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))



bot.polling(none_stop=True,interval=0)
