import datetime


def currency_rates_advanced(req, curr):
    if (4 <= len(curr) or len(curr) < 3) or req.find(curr) == -1 or curr.isalpha() != True or curr.find(' ') != -1:
        print('Incorrect currency abbreviation!!!  Try next time, please')
    elif curr in req:
        nom = req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1):(
                req.find('Nominal', ((req.find('Nominal', req.find(curr))) + 1)) - 2)]
        price = round(float((req[(req.find('Value', req.find(curr)) + len('Value') + 1):(
                req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.')), 2)

        a = req[req.find('"', req.find('Date')) + 1: req.find('"', req.find('Date')) + 11].split('.')
        date_today = datetime.date(int(a[2]), int(a[1]), int(a[0]))
        out = f'сегодня {date_today} курс {nom} {curr} = {price} рублей'
        print(out)

