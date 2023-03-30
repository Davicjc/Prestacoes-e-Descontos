# inportaçao de bibliotecas
import tkinter as tk

# _________________________________________________________________
# criaçao da janela "1.0"

# Cria uma janela
janela = tk.Tk()

# Define o título da janela
janela.title("Davicjc Progama")

# Define o tamanho da janela
janela.geometry("390x250")

# Define se a janela pode ser redimensionada
janela.resizable(False, False)

# Define a cor de fundo da janela
janela.configure(background="black")

# _________________________________________________________________
# exebiçao do programa na janela "1.0"

# explicaçao do programa
explicaçao_label = tk.Label(
    janela, text="Este programa calcula o valor de cada prestação e o valor com desconto", fg="white", bg="black")
explicaçao_label.pack()

# pegar o valor do produto que sofre a açaõ do desconto
valor_label = tk.Label(
    janela, text="Digite o valor total do produto:", fg="white", bg="black")
valor_label.pack()

valor_entry = tk.Entry(janela, width=30, fg="white", bg="gray")
valor_entry.pack()

# pegar o valor da prestaçao
prestacoes_label = tk.Label(
    janela, text="Quantas prestações?", fg="white", bg="black")
prestacoes_label.pack()

prestacoes_entry = tk.Entry(janela, width=30, fg="white", bg="gray")
prestacoes_entry.pack()

# pegar o valor do desconto
desconto_label = tk.Label(
    janela, text="Digite o desconto:", fg="white", bg="black")
desconto_label.pack()

desconto_entry = tk.Entry(janela, width=30, fg="white", bg="gray")
desconto_entry.pack()

# Cria um widget de resposta para exibir o resultado
resultado_label = tk.Label(janela, text="", fg="white", bg="black")
resultado_label.pack()

# Cria um widget de resposta para exibir o resultado
resultado1_label = tk.Label(janela, text="", fg="white", bg="black")
resultado1_label.pack()

# _________________________________________________________________
# funçao dos calculos "1.0"


def calculo():

    # _________________________________________________________________
    # verificaçao de campos vazios "1.1"

    if prestacoes_entry.get() == "" or desconto_entry.get() == "" or valor_entry.get() == "":
        resultado_label.config(text="Por favor, preencha todos os campos!")
    else:

        # _________________________________________________________________
        # Transforma os valores em inteiros  "1.0"

        prestaçao = int((prestacoes_entry.get()))
        desconto = int((desconto_entry.get()))
        valor = int((valor_entry.get()))

    # _________________________________________________________________
    # calculo do valor de cada prestação "0.5"

        compra = valor / prestaçao
        resultado1_label.config(
            text="O valor de cada prestação é: R$ {:.2f}".format(compra, valor))

    # _________________________________________________________________
    # calculo do valor com desconto "0.5"

        descont = desconto / 100
        valor_com_desconto = valor * descont
        valor_com_desconto = valor - valor_com_desconto
        resultado_label.config(
            text="O valor com desconto é: R$ {:.2f}.".format(valor_com_desconto))

# _________________________________________________________________
# botao para calcular "1.0"


# Cria um botão para calcular o resultado
calculo_botao = tk.Button(janela, text="Calculo",
                          command=calculo, fg="green", bg="gray")
calculo_botao.pack()

# _________________________________________________________________
# criador do programa "-.-"

# criado por Davicjc
davi_label = tk.Label(janela, text="By Davicjc, Beta1.2",
                      fg="white", bg="black")

textver = text = "'Ver betas'"
verbot_label = tk.Label(janela, text=textver,
                        cursor="hand1", bg="black", fg="Blue")
davi_label.pack()
verbot_label.pack()

# _________________________________________________________________
# botao para ver a versao do programa "1.1"

# Serve para chamar a função "versao" quando o botão for clicado
verbot_label.bind("<Button-1>", lambda event: versao())

# tela de versao do programa em labels


def versao():

    # separaçao de versoes
    spac_label = tk.Label(janela, text="________", bg="black", fg="white")
    spac2_label = tk.Label(janela, text="________", bg="black", fg="white")

    # versao 0.5
    text05 = "Beta 0.5\n-Calculo do valor de cada prestação.\n-Calculo do valor com desconto."
    vers05_label = tk.Label(janela, text=text05, fg="red", bg="black")

    # versao 1.0
    text1 = "Beta 1.0\n-Foi adicionado a interface grafica.\n-Otimiçao de codigo para interface."
    vers1_label = tk.Label(janela, text=text1, fg="gray", bg="black")

    # versao 1.1
    text11 = "Beta 1.1\n-Foi adicionado o botao para ver a versao do programa.\n-Melhora nas cores.\n-Correçao de bugs.\n-Melhor organizaçao do codigo."
    vers11_label = tk.Label(janela, text=text11, fg="purple", bg="black")

    # versao 1.2
    text12 = "Beta 1.2\n-Foi adicionado a funçao de verificar campos vazios.\n-Melhora na organizaçao do codigo.\n-Adicionado o botao retrair / Modo escuro ativo.\n-Janela com tamanho fixo."
    vers12_label = tk.Label(janela, text=text12, fg="yellow", bg="black")

    # objetivo da criaçao do programa
    text12 = "-Criada a partir de pedidos do professor da faculdade.\n-Primeira versão do código foi escrita em Portugol.\n-Posteriormente, ela foi convertida e refeita do zero por mim em 'PY'."
    objt_label = tk.Label(janela, text=text12, fg="green", bg="black")

# organizaçao dos labels
    spac_label.pack()
    vers05_label.pack()
    vers1_label.pack()
    vers11_label.pack()
    vers12_label.pack()
    spac2_label.pack()
    objt_label.pack()

# tamanho da janela
    janela.geometry("390x640")

# Botao para retrair a versao
    def retrair():
        vers05_label.pack_forget()
        vers1_label.pack_forget()
        vers11_label.pack_forget()
        vers12_label.pack_forget()
        retrair_botao.pack_forget()
        spac_label.pack_forget()
        spac2_label.pack_forget()
        objt_label.pack_forget()
        janela.geometry("390x250")

# Botao para retrair a versao
    retrair_botao = tk.Button(janela, text="Retrair",
                              command=retrair, fg="red", bg="gray")
    retrair_botao.pack()


# _________________________________________________________________
# loop da janela "1.0"
# Inicia o loop da janela
janela.mainloop()
