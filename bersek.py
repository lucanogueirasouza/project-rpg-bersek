from time import sleep

personagem = None

def tempo():
    sleep(0.5)

def linha(): 
    print("-=-" * 10)

def comecar_jogo():
    print("Bem-vindo ao RPG do Berserk.\n")
    tempo()
    print("Prepare-se para a batalha...\n")
    tempo()
    escolha2 = input("Deseja começar o jogo? (sim ou não): ").strip().lower()
    if escolha2 == 'sim':
        tempo()
        print("O destino espera por você...\n")
        menu_principal()  # Chama o menu do jogo
    else:
        print("Você fugiu do destino. Fim.")

def criarPersonagem(): 
    global personagem
    if personagem: 
        print("Você já tem um personagem.")
    else: 
        nome = str(input("Digite o nome do seu personagem: ")).strip().capitalize()

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
            print("Opção inválida.")
            personagem = None

def mostrar_status(): 
    global personagem
    linha()
    if not personagem: 
        print("Você não tem um personagem criado. Crie um!")
    else: 
        for chave, valor in personagem.items():
            if chave == "Marca" and valor == True:
                print("Maldição: Você ESTÁ amaldiçoado!")
            elif chave == "Marca" and valor == False:
                print("Maldição: Você NÃO está amaldiçoado.")
            else:
                print(f"{chave}: {valor}")
    linha()
    
def ganhar_xp(personagem, exp):
    print(f"voce ganhou {exp} exp parabens")
    personagem['exp'] += exp
    if personagem['exp'] >= exp:
        subir_nivel(personagem)

def subir_nivel(personagem):
    personagem['exp'] -= 100
    personagem['level'] += 1
    personagem['vida Max'] += 20

    if personagem['vida'] == personagem['vida max']:
        print('parabens voce subil de nivel uhul👌')

    if  personagem['classe'] == 'espadachim':
        personagem['forca'] += 3
        personagem['precisao'] += 1

    elif personagem['classe'] == 'assassino':
         personagem['forca'] += 2
         personagem['precisao'] += 2

    elif personagem['classe'] == 'arqueiro':
         personagem['forca'] += 1
         personagem['precisao'] += 3
