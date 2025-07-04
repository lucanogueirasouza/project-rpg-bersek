from time import sleep 

def tempo():
    sleep(0.5)

def comecar_jogo():
    print("Bem-vindo ao rpg do bersek.\n")
    tempo()
    print("\nPrepare-se para a batalha...\n")
    tempo()
    escolha2 = input("Deseja começar o jogo? (sim ou não): ").strip().lower()
    if escolha2 == 'sim':
        tempo()
        print("O destino espera por você...\n")
    else:
        print("Você fugiu do destino. Fim.")
comecar_jogo()
