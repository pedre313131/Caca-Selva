print("Caça Selva")
inicio = input("Deseja Iniciar? S/N: ")
if inicio == "s":
    print("Você achou 2 caminhos:")
    print("Direita")
    print("Esquerda")
    caminho1 = input("Qual Você Deseja Ir?: ")
    if caminho1 == "direita":
        print("Você achou mais 2 caminhos")
        print("Continuar")
        print("Direita")
        caminho2 = input("Qual Você Deseja Ir?: ")
        if caminho2 == "direita":
            urso = input("Você Achou 1 Urso, Deseja Caça-lo? S/N: ")
            if urso == "s":
                print("Você Caçou o Urso, E Conseguiu Comida Por 1 Semana. Parabens")
            if urso == "n":
                print("Você Não Caçou O Urso, Ele Te Comeu, Você Morreu")
        if caminho2 == "continuar":
            passaro = input("Você Achou 1 Passarinho, Deseja Caça-lo? S/N: ")
            if passaro == "s":
                print("Você Não Consegui Caça-lo Pois Ele Era Muito Fofinho, Mas Ele Te Comeu Sobrenaturalmente")
            if passaro == "n":
                print("Você Não o-caçou")
    if caminho1 == "esquerda":
        topeira = input("Você Achou 1 Topeira, Deseja Caça-lo? S/N: ")
        if topeira == "s":
            print("Você Tentou Caçar A Topeira, Mas Ela Era Do One Piece, Com Seu Time, Usou A Fruta Da Bomba E Te Matou")
        if topeira == "n":
            print("Você Não Caçou Ela.")
if inicio == "n":
    print("Obrigado Por Ter Vindo!")
