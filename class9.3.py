city = str(input('Qual o nome da sua cidade? E diremos se ela COMEÇA ou não com Santo, dando True ou False! ')).strip()
print(city[:5].upper() == 'SANTO')