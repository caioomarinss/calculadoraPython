import tkinter as tk #importacao da biblioteca para criar as telas

telaSimples = tk.Tk() #criacao de uma tela

resultado = tk.Label(telaSimples, text="Resultado: ") #crio um texto embaixo da calculadora para dizer "resultado:" para que o resultado da conta nao fique sozinho.
resultado.grid(row=5, column=4) #posiciono ele na linha 5 e coluna 4

equation = tk.StringVar() #cria uma variavel do tipo StringVar, ela é usada para armazenar textos dinamicos que podem ser atualizados na tela automaticamente
equation.set("0") #seta o valor da variavel como 0
display = tk.Label(telaSimples, textvariable=equation) #cria um texto na janela, que mostra o valor da variavel "equation" que recebe o valor da variavel "resultado" que é o resultado das operacaoes
display.grid(row=5, column=5) #posiciono o texto na linha 4 e na coluna 5.

texto = tk.Label(telaSimples, text="Calculadora!") #adionando um nome a tela
texto.grid(row=0, column=0, columnspan=4) #mostra esse nome na tela na primeira linha e na primeira coluna, o columnspan no valor 4 define que o texto vai ficar centralizado entre 4 colunas

vez = 1 #crio uma variavel para definir a vez das variaveis n1 e n2 para saber quem vai receber o valor quando o botao for clicado

def valorN(valor): #define a funcao valorN que quando chamada recebe o parametro "valor", "valor" recebe o numero que for passado da seguinte forma: valorN(0), quer dizer que "valor" é 0.
    global n1, n2, vez #coloco essas variaveis no escopo global para poderem ser utilizadas em todo o codigo
    if vez == 1:
        n1 = valor  #se tiver na vez 1, o n1 que vai receber o valor do botao
        vez = 2 #troco o vez para que o segundo clique no botao seja o valor de n2
    elif vez == 2: #se a vez for 2, o que quer dizer que n1 ja recebeu um valor, entao agora o valor do botao clicado vai para n2
            n2 = valor #n2 recebe o valor do botao clicado
            vez = 1 #volto o valor da vez para 1, se o usuario cliar novamente no botao agora ira redefinir o valor de n1 e se clicar mais uma vez, ira redefinir o valor de n2 e etc

def valorOperacao(op): #define a funcao valorOperacao que quando chamada recebe o parametro "op" que recebe o valor da seguinte forma: valorOperacao('+'), quer dizer que "op" é '+'
    global operacao
    operacao = op #a variavel operacao recebe "op" que é a operacao escolhida

def igual(): #define a funcao igual que quando chamada verifica qual o valor da variavel "operacao" e dependendo desse valor faz a conta que o usuario pediu
    global n1, n2, operacao
    if operacao == '+': #se o usuario escolheu o botao "+" ele vai receber uma conta de soma, e etc
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        resultado = n1 / n2
    equation.set(str(resultado)) #a variavel "equation" recebe o valor de "resultado", para que apareca o valor do resultado da operacao na janela

tk.Button(telaSimples, text="0", command=lambda: valorN(0)).grid(row=1, column=0) #crio um botão com texto "0" que ao ser clicado vai dar o valor para o parametro "valor", n1 ou n2 irá receber o conteudo de "valor".
tk.Button(telaSimples, text="1", command=lambda: valorN(1)).grid(row=1, column=1)
tk.Button(telaSimples, text="2", command=lambda: valorN(2)).grid(row=1, column=2)
tk.Button(telaSimples, text="+", command=lambda: valorOperacao('+')).grid(row=1, column=3) #cria um botão com texto "+" que ao ser clicado vai dar o valor para o parametro "op", operacao ira receber esse valor
tk.Button(telaSimples, text="3", command=lambda: valorN(3)).grid(row=2, column=0)
tk.Button(telaSimples, text="4", command=lambda: valorN(4)).grid(row=2, column=1)
tk.Button(telaSimples, text="5", command=lambda: valorN(5)).grid(row=2, column=2)
tk.Button(telaSimples, text="-", command=lambda: valorOperacao('-')).grid(row=2, column=3)
tk.Button(telaSimples, text="6", command=lambda: valorN(6)).grid(row=3, column=0)
tk.Button(telaSimples, text="7", command=lambda: valorN(7)).grid(row=3, column=1)
tk.Button(telaSimples, text="8", command=lambda: valorN(8)).grid(row=3, column=2)
tk.Button(telaSimples, text="x", command=lambda: valorOperacao('*')).grid(row=3, column=3)
tk.Button(telaSimples, text="9", command=lambda: valorN(9)).grid(row=4, column=0)
tk.Button(telaSimples, text="=", command=igual).grid(row=4, column=1)
tk.Button(telaSimples, text="/", command=lambda: valorOperacao('/')).grid(row=4, column=3)

telaSimples.mainloop() #Mostra a tela ate ela ser fechada


