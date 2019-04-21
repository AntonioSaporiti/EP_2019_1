# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Antonio Saporiti, antonios2@al.insper.edu.br
# - aluno B: Breno Marti, brenopm@al.insper.edu.br
# - aluno C: Fernando Bichuette, fernandoba2@al.insper.edu.br
#
import random

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "bibliotecaria": "Falar com a bibliotecária",
            }
        },
        "bibliotecaria": {
                "titulo": "Uma alma misteriosa",
                "descricao": "Voce está atrás de livros sagrados."
                            " Esses livros são capazes de acelerar seu aprendizado"
                            " em programação e, consequentemente, dão-te mais tempo"
                            " para realização do trabalho."
                            " Voce pede as coordenadas de localização desses livros à"
                            " bibliotecária."
                            " No entanto, ela começou a trabalhar na instituição semana"
                            " passada e não sabe ao certo em qual das duas seções estão"
                            " os livros",
                            
                "opcoes": {
                       "inicio": "Falar com a bibliotecária",
                       "secao 1": "Entrar na seção de Programação em C",
                       "secao 2": "Entrar na seção de Programação em Python",
            }
        },
        "secao 1": {
                "titulo": "A Seção Traiçoeira",
                "descricao": "A ala está mal iluminada e sua visão começa a embaçar."
                            " Voce consegue ver um esboço de uma figura ao final da seção."
                            " A figura que parecia ser da bibliotecaria começa a"
                            " sofrer mutações e se transforma no temido comedor de"
                            " programadores e arranca parte do seu cérebro fora.",
                "opcoes": {
                        "secao 2": "Voce só tem uma saída."
                                    " Corra para a Seção 2!!!",
                        }
                },
        "secao 2": {
                "titulo": "O Olimpo da Sabedoria",
                "descricao": "Voce chegou onde precisava."
                            " Aqui voce vai aprender a lidar com a linguagem em Python"
                            " e ganhar tempo para o seu trabalho!"
                            " Em salas como essa, voce ganha tempo que será acumulado"
                            " para realização do seu trabalho"
                            " Voce acaba de ganhar 1 dia" ,
                "opcoes": {
                        "bibliotecaria": "Voltar a falar com a Bibliotecaria.",
                        "auditorio": "Avançar para o auditório.",
                    },
#                "tempo": 1,
                },
                "auditorio":{
                "titulo":"Um poder oculto",
                "descricao":"Nessa sala, voce sente um poder estranho emanando"
                            " de todos os lados, na parede está escrito: gewoon"
                            " praten en je zal zijn."
                            " Traduzindo do holandês... basta falar e la vc estara.",
                            #holandes para "basta falar e la vc estara"
                "opcoes":{ "salao pereira telles": "kj",
                        #criar o teletransporte para a sala escolha(salao pereira telles)
                        }
                },
        "salao pereira telles": {
                "titulo": "O salão das escolhas",
                "descricao": "Neste salão, serão dadas oportunidades..."
                            " Elas podem se repetir..."
                            " Escolha sabiamente para que o processo de saida não caia em"
                            " um loop infinito!",
                "opcoes": {
                        "auditorio": "Retornar ao auditório",
                        "cafeteria": "Avançar para a cafeteria",
                        "laboratorio": "Avançar para o laboratório",
                        #Outra opção
                        }
                },
        "cafeteria": {
                "titulo": "A cafeteria fantasma",
                "descricao": "Um espaço peculiar. Poucos sabem de sua existência,"
                            " mas é vital para que voce se mantenha no jogo."
                            " Aqui voce consegue ganhar mais vida",
                "opcoes": {
                        "laboratorio": "Seguir adiante para o lab",
                        "salao pereira telles": "Retornar ao salão das oportunidades",
                        "saldo vidas": "20",# nao consegui add isso como chave ao dicionario
                },
            }
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
    
    hp=100
    
    dano=random.randint(0,100)
    
    game_over = False
    while not game_over and hp > 0:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print("-"*len(cenario_atual["descricao"]))
    

#Tentativa de fazer o contador de hit points

#        TempoRestante = cenario_atual['tempo']
        
        
#        for v in TempoRestante.items():
#            print("Seu tempo adicional é {0}".format(v))
        
    
        
        
        
        opcoes = cenario_atual['opcoes']
    
        for k,v in opcoes.items():
            print("{0}: {1}".format(k,v))
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
            
        
            
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            
            
            escolha = input("Faça sua escolha: ")
                        
            if escolha in ['professor']: 

                hp = hp - 10
                print("Você tem",hp, 'de vida')   


                hp = hp - dano
                print('Voce recebeu',dano,'de dano, agora voce tem',hp,'de vida')   
            
            if escolha in ["secao 1"]:
                hp=hp - dano
                print ('Voce recebeu',dano,'de dano, agora voce tem',hp,'de vida')
            
            elif dano==100:
                print("Seu dano foi de 100, voce morreu")
                game_over= True
                
            if escolha in ['cafeteria']: #PROBLEMA - está add vida antes do cara escolher a opçao
                hp = hp + 20
                print ("Seu saldo de vida é: ", hp)

            if escolha in opcoes:
                nome_cenario_atual = escolha
            
            elif len(escolha) != 0 and escolha not in opcoes:
                print("Essa opção não existe!")
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
    
    
    
    
    