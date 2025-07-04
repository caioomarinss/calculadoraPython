import tkinter as tk #importacao da biblioteca para criar a interface grafica

janela = tk.Tk() #criacao da janela principal

textoResultado = tk.Label(janela, text="Resultado: ") #criacao de um texto na janela para informar o resultado ao usuario
textoResultado.grid(row=5, column=1, columnspan=3) #posiciono ele na parte inferior da janela

resultadoOperacao = tk.StringVar() #criacao de uma variavel do tipo StringVar, ela é usada para armazenar textos dinamicos que podem ser atualizados na tela automaticamente conforme o valor

textoResultadoOperacao = tk.Label(janela, textvariable=resultadoOperacao) #criacao de um texto na janela para mostrar o valor da variavel "resultadoOperacao" que recebe o valor da variavel "resultado"
textoResultadoOperacao.grid(row=5, column=4) #posiciono o texto na linha 5 e na coluna 4, ao lado do texto "Resultado:" criado na linha 5 deste codigo

vez = 1 #criacao de uma variavel para definir a vez das variaveis n1 e n2, para definir qual vai receber o valor quando o botao for clicado

def valorNumero(vN): #define a funcao valorNumero, que quando chamada recebe o parametro "vN" que recebe o numero que for passado da seguinte forma: valorNumero(0), significa que "vN" recebe 0
    global n1, n2, vez #variaveis no escopo global, podem ser utilizadas em todo o codigo
    if vez == 1:
        n1 = vN  #se vez é igual a 1, n1 recebera o valor do botao clicado
        vez = 2 #a vez se alterna para que n2 receba o valor do proximo botao clicado
    elif vez == 2: #se vez é igual a 2, significa que n1 ja recebeu um valor, entao a vez alterna para que n2 receba o proximo valor
            n2 = vN #n2 recebe o valor do botao clicado
            vez = 1 #o valor da vez volta para 1, o valor de n1 sera substituido caso o usuario clique novamente no botao

def valorOperacao(vO): #define a funcao valorOperacao, que quando chamada recebe o parametro "vO" que recebe a operacao escolhida da seguinte forma: valorOperacao('+'), significa que "vO" recebe '+'
    global operacao
    operacao = vO #a variavel "operacao" recebe "vO" que é igual a operacao escolhida

def calcular(): #define a funcao calcular, que quando chamada verifica qual o valor da variavel "operacao" e dependendo desse valor, realiza uma determinada operacao escolhida pelo usuario
    global n1, n2, operacao
    if operacao == '+': #se o usuario apertou o botao "+" ele vai receber uma operacao de soma, e etc
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        resultado = n1 / n2
    resultadoOperacao.set(str(resultado)) #a variavel "resultadoOperacao" recebe o valor de "resultado", agora o resultado da operacao ira aparecer na parte inferior da janela gracas a linha 8 do codigo

tk.Button(janela, text="0", command=lambda: valorNumero(0)).grid(row=4, column=1) #criacao dos botãoes com texto dos numeros que ao serem clicados vao dar o valor para o parametros "vN",
tk.Button(janela, text="1", command=lambda: valorNumero(1)).grid(row=3, column=0) #n1 e n2 irao receber o conteudo do parametro "vN"
tk.Button(janela, text="2", command=lambda: valorNumero(2)).grid(row=3, column=1)
tk.Button(janela, text="3", command=lambda: valorNumero(3)).grid(row=3, column=2)
tk.Button(janela, text="4", command=lambda: valorNumero(4)).grid(row=2, column=0)
tk.Button(janela, text="5", command=lambda: valorNumero(5)).grid(row=2, column=1)
tk.Button(janela, text="6", command=lambda: valorNumero(6)).grid(row=2, column=2)
tk.Button(janela, text="7", command=lambda: valorNumero(7)).grid(row=1, column=0)
tk.Button(janela, text="8", command=lambda: valorNumero(8)).grid(row=1, column=1)
tk.Button(janela, text="9", command=lambda: valorNumero(9)).grid(row=1, column=2)

tk.Button(janela, text="+", command=lambda: valorOperacao('+')).grid(row=1, column=3) #criacao dos botoes com texto das operacoes que ao serem clicados vao dar o valor para o parametro "vO",
tk.Button(janela, text="-", command=lambda: valorOperacao('-')).grid(row=2, column=3) #a variavel "operacao" ira receber o conteudo do parametro "vO"
tk.Button(janela, text="x", command=lambda: valorOperacao('*')).grid(row=3, column=3)
tk.Button(janela, text="/", command=lambda: valorOperacao('/')).grid(row=4, column=3)
tk.Button(janela, text="=", command=calcular).grid(row=4, column=2)

janela.mainloop() #Mostra a janela ate ela ser fechada