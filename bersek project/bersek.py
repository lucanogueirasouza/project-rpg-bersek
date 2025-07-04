from time import sleep
from random import randint

personagem = None

def tempo():
    sleep(0.5)

def linha(): 
    print("-=-" * 10)

def comecar_jogo():
    print(
        "Bem-vindo ao RPG do Berserk.\n"
        )
    tempo()
    print(
        "Prepare-se para a batalha...\n"
        )
    tempo()
    escolha2 = input(
        "Deseja começar o jogo? (S/N): "
        ).strip().lower()
    if escolha2 == 's':
        tempo()
        print(
            "O destino espera por você...\n"
            )
        menu_principal()
    else:
        print(
            "Você fugiu do destino. Fim."
            )

def criarPersonagem(): 
    global personagem
    if personagem: 
        print(
            "Você já tem um personagem."
            )
    else: 
        nome = input(
            "Digite o nome do seu personagem: "
            ).strip().capitalize()

        espadachim = {
            "Nome": nome,
            "Classe": "Espadachim", 
            "Vida": 120, 
            "Vida Max": 120,
            "Forca": 15,
            "Precisao": 10,
            "Marca": False, 
            "Nivel": 1, 
            "EXP": 0,
        }

        assassino = {
            "Nome": nome,
            "Classe": "Assassino", 
            "Vida": 80, 
            "Vida Max": 80,
            "Forca": 20,
            "Precisao": 10,
            "Marca": False, 
            "Nivel": 1, 
            "EXP": 0,
        }

        arqueiro = {
            "Nome": nome,
            "Classe": "Arqueiro", 
            "Vida": 90, 
            "Vida Max": 90,
            "Forca": 15,
            "Precisao": 20,
            "Marca": False, 
            "Nivel": 1, 
            "EXP": 0,
        }

        escolha = int(input(
            "[1] - Espadachim (Vida Alta)\n" \
            "[2] - Assassino (Força Alta)\n" \
            "[3] - Arqueiro (Precisão Alta)\n" \
            "Escolha: "
        ))

        if escolha == 1: 
            personagem = espadachim
        elif escolha == 2: 
            personagem = assassino
        elif escolha == 3: 
            personagem = arqueiro
        else: 
            print(
                "Opção inválida."
                )
            personagem = None

def mostrar_status(): 
    global personagem
    linha()
    if not personagem: 
        print(
            "Você não tem um personagem criado. Crie um!"
            )
    else: 
        for chave, valor in personagem.items():
            if chave == "Marca":
                if valor:
                    print(
                        "Maldição: Você ESTÁ amaldiçoado!"
                        )
                else:
                    print(
                        "Maldição: Você NÃO está amaldiçoado."
                        )
            else:
                print(
                    f"{chave}: {valor}"
                    )
    linha()

def ganhar_xp(personagem, exp):
    print(
        f"Você ganhou {exp} EXP. Parabéns!"
        )
    personagem['EXP'] += exp
    while personagem['EXP'] >= 100:
        subir_nivel(personagem)

def subir_nivel(personagem):
    personagem['EXP'] -= 100
    personagem['Nivel'] += 1
    personagem['Vida Max'] += 20
    personagem['Vida'] = personagem['Vida Max']
    print(
        "Parabéns! Você subiu de nível!"
        )

    if personagem['Classe'].lower() == 'espadachim':
        personagem['Forca'] += 3
        personagem['Precisao'] += 1
    elif personagem['Classe'].lower() == 'assassino':
        personagem['Forca'] += 2
        personagem['Precisao'] += 2
    elif personagem['Classe'].lower() == 'arqueiro':
        personagem['Forca'] += 1
        personagem['Precisao'] += 3

def batalha():
    global personagem
    if not personagem:
        print(
            "Crie um personagem antes de lutar."
            )
        return None

    nivel_personagem = personagem["Nivel"]

    inimigo = { 
        "Vida": 50 * nivel_personagem,
        "Forca": 10 * nivel_personagem,
        "Experiencia": 30 * nivel_personagem,
    }

    print("\n--- Inimigo ---")
    for chave, valor in inimigo.items():
        print(
            f"{chave}: {valor}"
            )
    linha()

    contador = 0
    perdeu = None

    while personagem["Vida"] > 0 and inimigo["Vida"] > 0: 
        escolha = int(input("[1] - Atacar\n[2] - Tentar fugir\nEscolha: "))

        if escolha == 1:
            dano = personagem["Forca"] + (personagem["Precisao"] // 4)
            inimigo["Vida"] -= dano
            print(
                f"Você causou {dano} de dano. Vida do inimigo: {inimigo['Vida']}"
                )
            contador += 1
            if contador >= 2:
                dano_extra = (personagem["Forca"] // 2) + (personagem["Precisao"] // 4)
                inimigo["Vida"] -= dano_extra
                print(
                    f"Ataque adicional! Você causou {dano_extra} de dano extra. Vida do inimigo: {inimigo['Vida']}"
                    )

            if inimigo["Vida"] > 0:
                dano_inimigo = inimigo["Forca"]
                personagem["Vida"] -= dano_inimigo
                print(
                    f"O inimigo atacou! Você perdeu {dano_inimigo} de vida. Vida atual: {personagem['Vida']}"
                    )

        elif escolha == 2: 
            classe = personagem["Classe"]
            sucesso = False

            if classe == "Assassino":
                sucesso = True
            elif classe == "Arqueiro":
                sucesso = randint(1,100) <= 30
            elif classe == "Espadachim":
                sucesso = randint(1,100) <= 20

            if sucesso:
                print(
                    "Você conseguiu fugir!"
                    )
                return None
            else:
                print(
                    "Falha na fuga! O inimigo ataca!"
                    )
                dano = inimigo["Forca"]
                personagem["Vida"] -= dano
                print(
                    f"Você recebeu {dano} de dano. Vida atual: {personagem['Vida']}"
                    )
                if personagem["Vida"] <= 0:
                    print(
                        "Você foi derrotado..."
                        )
                    perdeu = True
                    break

    if personagem["Vida"] <= 0:
        perdeu = True

    if perdeu == True: 
        chance_marca = 25
        if randint(1,100) <= chance_marca: 
            print(
                "Você não foi amaldiçoado."
                )
            personagem["Marca"] = False
        else: 
            print(
                "Você foi amaldiçoado!"
                )
            personagem["Marca"] = True

    elif inimigo["Vida"] <= 0:
        print(
            "Você venceu a batalha!"
            )
        ganhar_xp(personagem, inimigo["Experiencia"])

        chance_espada = 10
        if randint(1,100) <= chance_espada: 
            print(
                "VOCÊ ENCONTROU A ESPADA DO BERSEKER!!"
                )
            personagem["Forca"] += 5
        else: 
            print(
                "Não foi dessa vez que você encontrou a espada. Lute e tente novamente."
                )

def menu_principal():
    while True:
        print(
            "\n[1] Criar Personagem\n[2] Mostrar Status\n[3] Batalhar\n[0] Sair"
            )
        opcao = input("Escolha: ")
        if opcao == '1':
            criarPersonagem()
        elif opcao == '2':
            mostrar_status()
        elif opcao == '3':
            batalha()
        elif opcao == '0':
            print(
                "Saindo do jogo..."
                )
            break
        else:
            print(
                "Opção inválida."
                )
            
comecar_jogo()