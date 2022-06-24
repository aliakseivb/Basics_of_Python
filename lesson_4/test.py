req = '>AMD</<Nominal>100</Nominal><Value>13,0515</Value>>SEK<Nominal>10</Nominal><Value>52,4351</Value>'
curr = 'SEK'
print(req.find(curr))
# первый символ номинала
print(req[req.find('Value', req.find(curr)) + len('Value') + 1])
print(req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)
print(req[req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 3])
print(round(float((req[(req.find('Value', req.find(curr)) + len('Value') + 1):(req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.')), 2))
d = float((req[(req.find('Value', req.find(curr)) + len('Value') + 1):(req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.'))
d = round(d, 2)
print(d)
nom = req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1):(req.find('Nominal', ((req.find('Nominal', req.find(curr)))+1))-2)]
# price = round(float(req[(req.find('Value', req.find(curr)) + len('Value') + 1):(req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.'), 2)

# ищем первый идекс валюты
print(req.find(curr), 'индекс валюты')
# индекс первого номинала
print(req.find('Nominal', req.find(curr)))
# первая цифра
print(req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1)])
# индекс первого символа второго номинала
print(req.find('Nominal', ((req.find('Nominal', req.find(curr)))+1)))

# print(req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1):(req.find('Nominal', ((req.find('Nominal', req.find(curr)))+1))-2)])

nom = req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1):(req.find('Nominal', ((req.find('Nominal', req.find(curr)))+1))-2)]

# price = round(float((req[(req.find('Value') + len('Value') + 1):(
#         req.find('Value', req.find('Value') + len('Value') + 1) - 2)]).replace(',', '.')), 2)

# price = round(float(req[(req.find('Value', req.find(curr)) + len('Value') + 1):
#                         (req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.'), 2)

# out = f'курс {curr} на данный момент: {nom} {curr} = {price} рублей'
# print(out)
