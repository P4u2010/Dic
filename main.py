meme_dict = {
            "CRINGE": "algo que es embarazoso",
            "LOL": "algo gracioso",
            "AFK": "fuera del teclad0",
            "EZ": "la partida fue muy facil",
            "GG": "Fue buena partida",
            "BOOMER": "Muy viejo y no entiende a los jovenes",
            "BASADO": "Tienes a tu disposicion, toda la verdad"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("no se encontro la llave")
