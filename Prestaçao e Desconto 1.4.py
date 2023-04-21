# Para melhor visualizaçao do codigo, use o programa "Notepad++" ou "Visual Studio Code"
# E de preferencia use o tema "Dracula" para melhor visualizaçao do codigo
# Tambem minimize todos os "DEFs" para melhor visualizaçao do codigo
# _________________________________________________________________

# inportaçao de bibliotecas
import tkinter as tk
import webbrowser

# _________________________________________________________________
# criaçao da janela "1.0"

# Cria uma janela
janela = tk.Tk()

# Define o título da janela
janela.title("Davicjc Progama")

# Define o tamanho da janela
janela.geometry("390x140")

# Define se a janela pode ser redimensionada
janela.resizable(False, False)

# Define a cor de fundo da janela
janela.configure(background="gray")


# _________________________________________________________________
# Funçao para exibir o lobby

def Loby():
    # ___________________________________________________________________
    # Lobby do programa

    lobby_label = tk.Label(
        janela, text="Bem vindo a calculadora de Prestações e Descontos", fg="white", bg="gray")
    lobby_label.config(font=("Arial", 13))
    lobby_label.pack()

    txtL = "Esse programa foi criado por Davicjc para testar e relembrar conceitos de\nprogramação em Python e tambem como trabalho para a faculdade.\n\nO programa é algo basico, porem pode ser util para relembrar\nconceitos de programação em Python."
    text_label = tk.Label(janela, text=txtL, fg="white", bg="gray")
    text_label.pack()

    # _________________________________________________________________
    # Apagar o lobby e exibir o programa

    def blk():
        cor_label.place_forget()
        lobyB_botao.place_forget()
        loby_botao.place_forget()
        text_label.pack_forget()
        lobby_label.pack_forget()
        Bcalculo()

    def Wit():
        cor_label.place_forget()
        lobyB_botao.place_forget()
        loby_botao.place_forget()
        text_label.pack_forget()
        lobby_label.pack_forget()
        Wcalculo()

    # _________________________________________________________________
    # Escolha de cor

    loby_botao = tk.Button(janela, text="Iniciar",
                           fg="white", bg="black", cursor="hand2", command=blk)
    loby_botao.place(x=90, y=110)

    lobyB_botao = tk.Button(janela, text="Iniciar",
                            fg="black", bg="white", cursor="hand2", command=Wit)
    lobyB_botao.place(x=260, y=110)

    cor_label = tk.Label(janela, text="<-Escolha o Tema->",
                         fg="white", bg="gray")
    cor_label.place(x=138, y=110)
Loby()

# Verçao Preta do programa

def Bcalculo():

    # _____________________________________________________________________
    # Utiliza o método pack_forget para esconder todos os widgets de texto e botões

    def limpar_tela():
        explicaçao_label.pack_forget()
        valor_label.pack_forget()
        valor_entry.pack_forget()
        prestacoes_label.pack_forget()
        prestacoes_entry.pack_forget()
        desconto_label.pack_forget()
        desconto_entry.pack_forget()
        resultado_label.pack_forget()
        resultado1_label.pack_forget()
        calculo_botao.pack_forget()
        davi_label.place_forget()
        verbotb_label.place_forget()
        Rzt_label.place_forget()
        janela.geometry("390x140")
        janela.configure(background="gray")
        Loby()

    Rzt_label = tk.Label(janela, text=">Temas",
                           fg="red", bg="black", cursor="hand1")
    Rzt_label.place(x=340, y=245)

    Rzt_label.bind("<Button-1>", lambda event: limpar_tela())

    # _________________________________________________________________
    # exebiçao do programa na janela "1.0"

    # Define a cor de fundo da janela
    janela.configure(background="black")

    # Define o tamanho da janela
    janela.geometry("390x270")

    # explicaçao do programa
    explicaçao_label = tk.Label(
        janela, text="Este programa calcula o valor de cada prestação e o valor com desconto\n'Usar apenas numeros!'\n", fg="white", bg="black")
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
        janela, text="Digite o desconto em % :", fg="white", bg="black")
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

        if valor_entry.get() == "" and prestacoes_entry.get() == "" and desconto_entry.get() == "":
            resultado_label.config(text="Por favor, preencha todos os campos!")
            resultado1_label.config(text="")

        else:
            if valor_entry.get() == "":
                resultado_label.config(text="Por favor, preencha o campo 'VALOR'!")
            else:
                valor = int((valor_entry.get()))
            
            if prestacoes_entry.get() == "":
                resultado1_label.config(text="Não foi possivel calcular o valor das prestações!") 
            else:
                prestaçao = int((prestacoes_entry.get()))
                compra = valor / prestaçao
                resultado1_label.config(
                    text="O valor de cada prestação é: R$ {:.2f}".format(compra, valor))

            if desconto_entry.get() == "":
                resultado_label.config(text="Não foi possivel calcular o valor com o desconto!")
            else:
                desconto = int((desconto_entry.get()))
                descont = desconto / 100
                valor_com_desconto = valor * descont
                valor_com_desconto = valor - valor_com_desconto
                resultado_label.config(
                    text="O valor com desconto aplicado é: R$ {:.2f}.".format(valor_com_desconto))

    # _________________________________________________________________
    # botao para calcular "1.0"

    # Cria um botão para calcular o resultado
    calculo_botao = tk.Button(janela, text="Calculo",
                              command=calculo, fg="green", bg="gray", cursor="hand2")
    calculo_botao.pack()

    # _________________________________________________________________
    # criador do programa "-.-"

    # criado por Davicjc
    davi_label = tk.Label(janela, text=">By Davicjc - 1.4",
                          fg="white", bg="black", cursor="hand1")

    textver = text = ">Ver betas"
    verbotb_label = tk.Label(janela, text=textver,
                            cursor="hand1", bg="black", fg="Blue")
    davi_label.place(x=147, y=245)
    verbotb_label.place(x=0, y=245)

    # _________________________________________________________________
    # botao para ver a versao do programa "1.1"

    # Serve para chamar a função "versao" quando o botão for clicado
    verbotb_label.bind("<Button-1>", lambda event: Bversao())

    #Serve para chamar a função "Davi" quando o botão for clicado
    davi_label.bind("<Button-1>", lambda event: Davi())

    def Davi():
        webbrowser.open("https://github.com/Davicjc/")

    # tela de versao do programa em labels

    def Bversao():
        
        # limpa a tela
        explicaçao_label.pack_forget()
        valor_label.pack_forget()
        valor_entry.pack_forget()
        prestacoes_label.pack_forget()
        prestacoes_entry.pack_forget()
        desconto_label.pack_forget()
        desconto_entry.pack_forget()
        resultado_label.pack_forget()
        resultado1_label.pack_forget()
        calculo_botao.pack_forget()
        davi_label.place_forget()
        verbotb_label.place_forget()
        Rzt_label.place_forget()

        # versao 0.5
        text05 = "Beta 0.5\n- Cálculo do valor de cada prestação.\n- Cálculo do valor com desconto."
        vers05_label = tk.Label(janela, text=text05, fg="red", bg="black")

        # versao 1.0
        text1 = "Beta 1.0\n- Foi adicionada a interface gráfica.\n- Otimização de código para a interface."
        vers1_label = tk.Label(janela, text=text1, fg="gray", bg="black")

        # versao 1.1
        text11 = "Beta 1.1\n- Foi adicionado o botão para ver a versão do programa.\n- Melhoria nas cores.\n- Correção de bugs.\n- Melhor organização do código."
        vers11_label = tk.Label(janela, text=text11, fg="purple", bg="black")

        # versao 1.2
        text12 = "Beta 1.2\n- Foi adicionada a função de verificar campos vazios.\n- Melhoria na organização do código.\n- Adicionado o botão retrair / Modo escuro ativo.\n- Janela com tamanho fixo."
        vers12_label = tk.Label(janela, text=text12, fg="yellow", bg="black")

        # Versao 1.3
        text13 = "V 1.3\n- Temas 'preto e branco'.\n- Novo Lobby ao entrar no programa.\n- Melhora da visualização do codigo.\n- Versões em aba separada."
        vers13_label = tk.Label(janela, text=text13, fg="green", bg="black")

        # Versao 1.4
        text14 = "V 1.4\n- Pode calcular apenas prestação ou o desconto separadamente.\n- Modificação na escrita do front-end."
        vers14_label = tk.Label(janela, text=text14, fg="blue", bg="black")

    # organizaçao dos labels
        vers05_label.pack()
        vers1_label.pack()
        vers11_label.pack()
        vers12_label.pack()
        vers13_label.pack()
        vers14_label.pack()

    # tamanho da janela
        janela.geometry("390x430")

    # Botao para retrair a versao
        def retrair():
            vers05_label.pack_forget()
            vers1_label.pack_forget()
            vers11_label.pack_forget()
            vers12_label.pack_forget()
            retrair_botao.pack_forget()
            vers13_label.pack_forget()
            vers14_label.pack_forget()
            explicaçao_label.pack()
            valor_label.pack()
            valor_entry.pack()
            prestacoes_label.pack()
            prestacoes_entry.pack()
            desconto_label.pack()
            desconto_entry.pack()
            resultado_label.pack()
            resultado1_label.pack()
            calculo_botao.pack()
            davi_label.place(x=147, y=245)
            verbotb_label.place(x=0, y=245)
            Rzt_label.place(x=340, y=245)
            janela.geometry("390x270")

    # Botao para retrair a versao
        retrair_botao = tk.Button(janela, text="Retrair",
                                  command=retrair, fg="red", bg="gray", cursor="hand2")
        retrair_botao.pack()

# Verçao Branca do programa

def Wcalculo():

    # _____________________________________________________________________
    # Utiliza o método pack_forget para esconder todos os widgets de texto e botões

    def limpar_tela():
        explicaçao_label.pack_forget()
        valor_label.pack_forget()
        valor_entry.pack_forget()
        prestacoes_label.pack_forget()
        prestacoes_entry.pack_forget()
        desconto_label.pack_forget()
        desconto_entry.pack_forget()
        resultado_label.pack_forget()
        resultado1_label.pack_forget()
        calculo_botao.pack_forget()
        davi_label.place_forget()
        verbotw_label.place_forget()
        Rzt_label.place_forget()
        janela.geometry("390x140")
        janela.configure(background="gray")
        Loby()

    Rzt_label = tk.Label(janela, text=">Temas",
                           fg="red", bg="white", cursor="hand1")
    Rzt_label.place(x=340, y=245)

    Rzt_label.bind("<Button-1>", lambda event: limpar_tela())

    # _________________________________________________________________
    # exebiçao do programa na janela "1.0"

    # Define o tamanho da janela
    janela.geometry("390x270")

    # Define a cor de fundo da janela
    janela.configure(background="white")

    # explicaçao do programa
    explicaçao_label = tk.Label(
        janela, text="Este programa calcula o valor de cada prestação e o valor com desconto\n'Usar apenas numeros!'\n", fg="black", bg="white")
    explicaçao_label.pack()

    # pegar o valor do produto que sofre a açaõ do desconto
    valor_label = tk.Label(
        janela, text="Digite o valor total do produto:", fg="black", bg="white")
    valor_label.pack()

    valor_entry = tk.Entry(janela, width=30, fg="black", bg="gray")
    valor_entry.pack()

    # pegar o valor da prestaçao
    prestacoes_label = tk.Label(
        janela, text="Quantas prestações?", fg="black", bg="white")
    prestacoes_label.pack()

    prestacoes_entry = tk.Entry(janela, width=30, fg="black", bg="gray")
    prestacoes_entry.pack()

    # pegar o valor do desconto
    desconto_label = tk.Label(
        janela, text="Digite o desconto em % :", fg="black", bg="white")
    desconto_label.pack()

    desconto_entry = tk.Entry(janela, width=30, fg="black", bg="gray")
    desconto_entry.pack()

    # Cria um widget de resposta para exibir o resultado
    resultado_label = tk.Label(janela, text="", fg="black", bg="white")
    resultado_label.pack()

    # Cria um widget de resposta para exibir o resultado
    resultado1_label = tk.Label(janela, text="", fg="black", bg="white")
    resultado1_label.pack()

    # _________________________________________________________________
    # funçao dos calculos "1.0"

    def calculo():

        # _________________________________________________________________
        # verificaçao de campos vazios "1.1"

        if valor_entry.get() == "" and prestacoes_entry.get() == "" and desconto_entry.get() == "":
            resultado_label.config(text="Por favor, preencha todos os campos!")
            resultado1_label.config(text="")

        else:
            if valor_entry.get() == "":
                resultado_label.config(text="Por favor, preencha o campo 'VALOR'!")
            else:
                valor = int((valor_entry.get()))
            
            if prestacoes_entry.get() == "":
                resultado1_label.config(text="Não foi possivel calcular o valor das prestações!") 
            else:
                prestaçao = int((prestacoes_entry.get()))
                compra = valor / prestaçao
                resultado1_label.config(
                    text="O valor de cada prestação é: R$ {:.2f}".format(compra, valor))

            if desconto_entry.get() == "":
                resultado_label.config(text="Não foi possivel calcular o valor com o desconto!")
            else:
                desconto = int((desconto_entry.get()))
                descont = desconto / 100
                valor_com_desconto = valor * descont
                valor_com_desconto = valor - valor_com_desconto
                resultado_label.config(
                    text="O valor com desconto aplicado é: R$ {:.2f}.".format(valor_com_desconto))

    # _________________________________________________________________
    # botao para calcular "1.0"

    # Cria um botão para calcular o resultado
    calculo_botao = tk.Button(janela, text="Calculo",
                              command=calculo, fg="green", bg="gray", cursor="hand2")
    calculo_botao.pack()

    # _________________________________________________________________
    # criador do programa "-.-"

    # criado por Davicjc
    davi_label = tk.Label(janela, text=">By Davicjc - 1.3",
                          fg="black", bg="white", cursor="hand1")

    textver = text = ">Ver betas"
    verbotw_label = tk.Label(janela, text=textver,
                            cursor="hand1", bg="white", fg="Blue")
    davi_label.place(x=147, y=245)
    verbotw_label.place(x=0, y=245)

    # _________________________________________________________________
    # botao para ver a versao do programa "1.1"

    # Serve para chamar a função "versao" quando o botão for clicado
    verbotw_label.bind("<Button-1>", lambda event: Wversao())

    #Serve para chamar a função "Davi" quando o botão for clicado
    davi_label.bind("<Button-1>", lambda event: Davi())

    def Davi():
        webbrowser.open("https://github.com/Davicjc/")


    # tela de versao do programa em labels

    def Wversao():

        # limpa a tela
        explicaçao_label.pack_forget()
        valor_label.pack_forget()
        valor_entry.pack_forget()
        prestacoes_label.pack_forget()
        prestacoes_entry.pack_forget()
        desconto_label.pack_forget()
        desconto_entry.pack_forget()
        resultado_label.pack_forget()
        resultado1_label.pack_forget()
        calculo_botao.pack_forget()
        davi_label.place_forget()
        verbotw_label.place_forget()
        Rzt_label.place_forget()

        # versao 0.5
        text05 = "Beta 0.5\n- Cálculo do valor de cada prestação.\n- Cálculo do valor com desconto."
        vers05_label = tk.Label(janela, text=text05, fg="red", bg="white")

        # versao 1.0
        text1 = "Beta 1.0\n- Foi adicionada a interface gráfica.\n- Otimização de código para a interface."
        vers1_label = tk.Label(janela, text=text1, fg="gray", bg="white")

        # versao 1.1
        text11 = "Beta 1.1\n- Foi adicionado o botão para ver a versão do programa.\n- Melhoria nas cores.\n- Correção de bugs.\n- Melhor organização do código."
        vers11_label = tk.Label(janela, text=text11, fg="purple", bg="white")

        # versao 1.2
        text12 = "Beta 1.2\n- Foi adicionada a função de verificar campos vazios.\n- Melhoria na organização do código.\n- Adicionado o botão retrair / Modo escuro ativo.\n- Janela com tamanho fixo."
        vers12_label = tk.Label(janela, text=text12, fg="orange", bg="white")
      
        # Versao 1.3
        text13 = "V 1.3\n- Temas 'preto e branco'.\n- Novo Lobby ao entrar no programa.\n- Melhora da visualização do codigo.\n- Versões em aba separada."
        vers13_label = tk.Label(janela, text=text13, fg="green", bg="white")

        # Versao 1.4
        text14 = "V 1.4\n- Pode calcular apenas prestação ou o desconto separadamente.\n- Modificação na escrita do front-end."
        vers14_label = tk.Label(janela, text=text14, fg="blue", bg="white")

    # organizaçao dos labels
        vers05_label.pack()
        vers1_label.pack()
        vers11_label.pack()
        vers12_label.pack()
        vers13_label.pack()
        vers14_label.pack()

    # tamanho da janela
        janela.geometry("390x430")

    # Botao para retrair a versao
        def retrair():
            vers05_label.pack_forget()
            vers1_label.pack_forget()
            vers11_label.pack_forget()
            vers12_label.pack_forget()
            retrair_botao.pack_forget()
            vers13_label.pack_forget()
            vers14_label.pack_forget()
            explicaçao_label.pack()
            valor_label.pack()
            valor_entry.pack()
            prestacoes_label.pack()
            prestacoes_entry.pack()
            desconto_label.pack()
            desconto_entry.pack()
            resultado_label.pack()
            resultado1_label.pack()
            calculo_botao.pack()
            davi_label.place(x=147, y=245)
            verbotw_label.place(x=0, y=245)
            Rzt_label.place(x=340, y=245)
            janela.geometry("390x270")

    # Botao para retrair a versao
        retrair_botao = tk.Button(janela, text="Retrair",
                                  command=retrair, fg="red", bg="gray", cursor="hand2")
        retrair_botao.pack()

# _________________________________________________________________


# Inicia o loop da janela
janela.mainloop()
