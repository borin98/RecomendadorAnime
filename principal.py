import numpy as np

from rbm import RBM

"""

Função que cria uma RBM
    
    :return
        rbm = boltzman machine object

"""
def criaRBM() :

    # serão utilizados 6 animes de entrada e 3 tipos de filmes como output ( mecha, shonen/ação e comédia/romance/shoujo )
    rbm = RBM(num_visible = 6, num_hidden = 3)

    return rbm
"""

Função que cria a recomendação para o usuário

    :param
        
        rbm = Boltmanz machine
        usuario = usuário base
        anime = lista de animes que será recomendado para o usuário

"""
def recomendacao(rbm, usuario, animes) :

    # função que vai dizer qual neurónio foi ativado
    ativacao = rbm.run_visible(usuario)

    str = ""

    for i in range(ativacao.size) :

        if(ativacao[0][i] == 1) :

            if(i == 0) :

                str += "mecha, "

            elif(i == 1) :

                str += "shonen, "

            elif(i == 2) :

                str += "shoujo, "


    print("preferências do usuário : {}.".format(str[:len(str) - 2]))
    print("\n")

    # criação da recomendação
    reomend = rbm.run_hidden(ativacao)

    # recomendação para o próximo usuário

    str = ""
    for i in range(len(usuario[0])) :

        if (usuario[0,i] == 0 and reomend[0, i] == 1) :

            str += animes[i]
            str += ", "

    print("Animes que você poderia gostar : {}.\n".format(str[:len(str) - 2]))

def main() :

    # database exemplo
    df = np.array([[1, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0],
                   [1, 1, 1, 0, 0, 0],
                   [0, 0, 1, 1, 1, 1],
                   [0, 0, 1, 1, 0, 1],
                   [0, 0, 1, 1, 0, 1]])

    rbm = criaRBM()
    rbm.train(df, max_epochs = 30000)

    # lista de filmes
    animes = ["Neon Genesis Evangelion", "Gundam Unicorn",
              "Gintama", "Fire Force",
              "Wotakoi : love is hard for otakus", "Kaguya-sama : Love is war"  ]

    # vizualizando os pesos
    # olhar a partir da segunda linha = 1, pois linha = 0 é a unidade de bias de filmes e de cada neurônio de recomendação
    # os maiores valores serão os neurônios utilizados para reconhecer que tipo de filme ele é
    print("\nPesos da matriz : {}\n".format(rbm.weights))

    usuario = np.array([[1, 0, 0, 0, 0, 1]])
    usuario2 = np.array([[0, 0, 1, 0, 1, 0]])

    recomendacao(rbm, usuario, animes)

    print("------------ Recomendação usuário 2 ------------\n")
    recomendacao(rbm, usuario2, animes)

if __name__ == '__main__':
    main()