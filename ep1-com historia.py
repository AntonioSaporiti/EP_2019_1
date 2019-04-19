# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Antonio Saporiti, antonios2@al.insper.edu.br
# - aluno B: Breno Marti, brenopm@al.insper.edu.br
# - aluno C: Fernando Bichuette, fernandoba2@al.insper.edu.br
#
def carregar_cenarios():
    print ('#######################')
    print ('###### O Começo #######')
    print ('#######################')
    cenarios = {
        "inicio": {
            "titulo": "Saguao da Sangue",
            "descricao": "Voce chegou nas antigas ruinas de Casermir, um antigo templo Elfico que guarda reliquias mais antigas que do a propria existencia do homem.\nCom sua espada besta í heimi voce entra no saguao do templo em busca de seus tesouros",
            "opcoes": {
                "andar pelo Saguao": "Você explora o Saguao em busca de reliquias ",
                "ir para as masmorras": "Você desce as escadas para conhecer a assombrosa masmorra do Templo"
            }
        },
        "andar pelo Saguao": {
            "titulo": "O misterioso Altar de guð",
            "descricao": "Enquanto explorava o Saguao você encontrou o Altar de guð um antigo deus elfico que era adorado no templo.\nAtraz do altar você encontrou um mecanismo secreto que abre uma passagem para uma escada que o leva para uma sala secreta na torre do templo ",
            "opcoes": {
                "Explorar a sala": "Você decide entrar na sala secreta.\nEnquanto subia pela escada da sala você escuta um grito no alto da torre  ",
                "Ir para os Jardins": "Você decide ignorar as escadas e vai para os jardins do templo"
            }
        },
        "Explorar a sala": {
            "titulo": "O monstro da torre do sacrificio ",
            "descricao": "Voce sobe as escadas correndo para saber de quem era aquele grito que vinha do alto da torre que estava abandonada a seculos  . "
                         "Voce chega no ultimo degrau da escada e se depara com um Troll que guarda um velho báu. "
                         "Ele diz que o báu contem um pergaminho com a localização de um artefato muito poderoso e que ele da o pergaminho se ele acertar a seguinte charada."
                         "O que matamos todos os dias, mas nunca somos presos.",
            "opcoes": {
                "Voce responde a charada"           #criar um sistema de resposta (fome) se voce errar game over 
                "Voce luta com o Troll":"Voce decide lutar contra o Troll para pegar o pergaminho" 
                    }
        },
        "Ir para os Jardins":{
            "titulo": " A Fonte da juventude",
            "descricao": "Você encontra uma fonte no jardim, ao tomar um gole de agua da fonte você se sente mais jovem e mais disposto.\nVocê encontrou a fonte da juventude."
                         "Ao tentar encher o sua muringa com a agua da fonte uma bruxa aparece."
                         "Ela diz que a fonte é dela e, que nenhum mortal pode pegar agua milagrosa e que voce deve dar meia volta e sair do templo",   
            "opcoes":{
                "lutar":"Voce descide lutar com a bruxa",
                "dar no pé":"Voce da meia volta e sai do templo"   #game over
            }
            
        },    
            
        "ir para as masmorras": {
            "titulo": "As masmorras de Casemir",
            "descricao": "Voce entra na masmorra do templo."
                         "Lá voce ve esqueletos de varias especies: homens, anoes, golens ate mesmo de outros elfos"
                         "Voce vê uma luz no fundo da caverna",
            "opcoes": {
                "Game over": "Voce ve toda aquela morte, e concorda que não vale a pena morrer para isso",     #game over
                "A luz": "Voce descide explorar mais a masmorra e saber o que é aquela luz"
            }
        },
        "A luz":{
           "titulo":"O executor",     
           "descricao": "Voce adentra mais profundo a masmorra em busca de respostas"
                        "Ao chegar no fundo da masmorra voce ve um Lich, um mostro corrompido de aspecto fantasmagorico que protege o lugar"
                        "Ele te ordena que saia do templo de mãos vazias.\nSe nao fosse obedecido ele te mataria ",
           "opcoes":{
                "Voce da meia volta": "Voce da meia volta e sai do templo de mãos vazias",
                "Voce luta":"Voce decide lutar com o Lich"  
                 }                             
                
        },   
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
