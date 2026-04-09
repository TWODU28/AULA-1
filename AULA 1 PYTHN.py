meme_dict = { "CRINGE": "Algo vergonhoso ou constrangedor", "STALKEAR": "Investigar a vida de alguém online","HATER" : "pessoa que está constantemente criticando os outros" , "TMJ" : " é uma abreviação de 'tamo junto', usada para expressar apoio, amizade e solidariedade.", 'FELCA': 'UM CHATO E SEM FAMILIA' }
             
word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys(): 
    print(meme_dict[word])
    # O que devemos fazer se a palavra for encontrada?
else: 
    print("essa palavra ainda não existe entao vá reclamar com o FELCA")
    # O que devemos fazer se a palavra não for encontrada?
