from datetime import datetime
from time import sleep

class Anuncio:
    def __init__(self, nome, cliente, data_inicio, data_fim, invest_dia):
        self.nome = nome
        self.cliente = cliente
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.invest_dia = invest_dia
    
class AnuncioRelatorio:
    def __init__(self, valor_total_investido, qtd_max_vizu, qtd_max_cliques, qtd_max_comps, cliente, tempo_inicio, tempo_fim):
        self.valor_total_investido = valor_total_investido
        self.qtd_max_vizu = qtd_max_vizu
        self.qtd_max_cliques = qtd_max_cliques
        self.qtd_max_comps = qtd_max_comps
        self.cliente = cliente
        self.tempo_inicio = tempo_inicio
        self.tempo_fim = tempo_fim
        

def cadastrar():
    print('--------------------------------------------------------------------')
    print("\n######################  CADASTRO DE ANÚNCIO  ####################### \n")
    print('--------------------------------------------------------------------')
    nome = input("Nome do anúncio: ")
    cliente = input("Cliente: ")
    data_inicio_f = input("Data de Inicio [dd/mm/aaaa]: ")
    data_inicio = datetime.strptime(data_inicio_f, "%d/%m/%Y")
    data_fim_f = input("Data de Fim [dd/mm/aaaa]: ")
    data_fim = datetime.strptime(data_fim_f, "%d/%m/%Y")
    investimento = float(input("Valor do investimento diário: "))

    novo_anuncio = Anuncio(nome=nome, cliente=cliente, data_inicio=data_inicio, data_fim=data_fim, invest_dia=investimento)

    print("\nCADASTRO CONCLUÍDO COM SUCESSO!\n")

    return novo_anuncio


def filtrar_por_cliente(array_anuncios, d, cliente):

    c = 0

    for i in array_anuncios:
        if(i.cliente == cliente):
            print("Nome do anuncio: " + i.nome)
            print("Cliente: " + i.cliente)
            print("")
            print("Data de inicio: ")
            print(i.data_inicio)
            print("")
            print("Data de fim: ")
            print( i.data_fim)
            print("")
            print("Investimento diário: ")
            print(i.invest_dia)
            print("")
            print("Valor total investido: ")
            print(d[c].valor_total_investido)
            print("")
            print("Maximo de vizualizações: ")
            print(d[c].qtd_max_vizu)
            print("")
            print("Maximo de cliques: ")
            print(d[c].qtd_max_cliques)
            print("")
            print("Maximo de compartilhamentos: ")
            print(d[c].qtd_max_comps)
            print("------------------------------------------------------")

            c += 1

def filtrar_por_tempo(array_anuncios, d, tempo_inicio, tempo_fim):
    
    c = 0

    for i in array_anuncios:
        if(i.data_inicio >= tempo_inicio and i.data_fim <= tempo_fim):
            
            print("Nome do anuncio: " + i.nome )
            print("Cliente: " + i.cliente )
            print("")
            print("Data de inicio: ")
            print(i.data_inicio )
            print("")
            print("Data fim: ") 
            print(i.data_fim)
            print("")
            print("Investimento por dia: " )
            print(i.invest_dia)
            print("")
            print("Valor total investido: " )
            print(d[c].valor_total_investido)
            print("")
            print("Maximo de vizualizações: ")
            print(d[c].qtd_max_vizu)
            print("")
            print("Maximo de cliques: ")
            print(d[c].qtd_max_cliques)
            print("")
            print("Maximo de compartilhamentos: ")
            print(d[c].qtd_max_comps)
            print("--------------------------------------------------------------------")

            c += 1
        
def calculadora(anuncio):
    dias = dias_total(anuncio.data_inicio, anuncio.data_fim)
    valor_total_investido = dias * anuncio.invest_dia
    investimento_inteiro = (int(valor_total_investido)) 
    vizu = investimento_inteiro * 30

    qtd_max_cliques = 0
    qtd_max_comps = 0
    cont = 0

    cliques = (int)(int(vizu* 0.12))
    qtd_max_cliques += cliques

    comps = (int)(int(cliques * 0.15) + 4)

    qtd_max_comps += comps

    novas_vizu = 40 * comps

    vizu += novas_vizu

    while cont < 3:
        
        cliques = (int)(int(novas_vizu/100) * 12)
        qtd_max_cliques += cliques

        comps =(int)(int(cliques * 0.15) + 4)
        qtd_max_comps += comps

        novas_vizu = 40 * comps
        cont += 1
        vizu += novas_vizu

    relatorio = AnuncioRelatorio(valor_total_investido=valor_total_investido, qtd_max_vizu=vizu, 
    qtd_max_cliques=qtd_max_cliques,
    qtd_max_comps=qtd_max_comps, 
    cliente=anuncio.cliente, 
    tempo_inicio=anuncio.data_inicio, 
    tempo_fim=anuncio.data_fim)

    return relatorio   

def dias_total(data_inicio, data_fim):
    dias_totais = (data_fim - data_inicio).days

    return dias_totais

def menu():

    AnuncioArray = []
    RelatorioArray = []

    while True:

        print ("--------------------------------------------------------------------")
        print ("************************** BEM VINDO *******************************")
        print("  [1] CADASTRAR   |   [2] PROCURAR RELATÓRIO   |       [3] SAIR      ")
        print("---------------------------------------------------------------------")
        opcao = input("INFORME A OPÇÃO DESEJADA: ")

        if opcao == "1":

            novo_anuncio = cadastrar()
            relatorio_do_anuncio = calculadora(novo_anuncio)
            AnuncioArray.append(novo_anuncio)
            RelatorioArray.append(relatorio_do_anuncio)

        if opcao == "2":

            print("--------------------------------------------------------------------")
            print("\n#######################  FILTRAR ANÚNCIO  ########################## \n")
            print("         [1] INTERVALO DE TEMPO      |      [2] CLIENTE             ")
            print("--------------------------------------------------------------------")
            opcao_filtro = input("OPÇÃO DESEJADA : ")
            print("--------------------------------------------------------------------")

            if (opcao_filtro == '1'):
                data_inicio_f = input("Data Inicio [dd/mm/aaaa]: ")
                tempo_inicio = datetime.strptime(data_inicio_f, "%d/%m/%Y")
                data_fim_f = input("Data Fim [dd/mm/aaaa]: ")
                tempo_termino = datetime.strptime(data_fim_f, "%d/%m/%Y")
                print("--------------------------------------------------------------------")
                filtrar_por_tempo(AnuncioArray, RelatorioArray, tempo_inicio, tempo_termino)

            if (opcao_filtro == '2'):
                nome_cliente = input("Nome do cliente: ")
                print("--------------------------------------------------------------------")
                filtrar_por_cliente(AnuncioArray, RelatorioArray, nome_cliente)

            else:
                pass

        if opcao == '3':
            print(" ----------------------------------------------------------------------")
            print("|                  SAINDO DO SISTEMA... ATÉ LOGO!                     |")
            print("-----------------------------------------------------------------------")
            break
    sleep(2)

menu()