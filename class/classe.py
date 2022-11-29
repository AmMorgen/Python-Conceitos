#estrutura de uma classe python
#por convenção nome em letra maiuscula
class Lampada:
    #metodo construtor
    def __init__(self, voltagem, cor):
        self.voltagem =voltagem
        self.cor =cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite,saldo):
        self.numero= numero
        self.limite=limite
        self.saldo=saldo

class Produto:
    #atributo de classe
    imposto = 1.05
    contador = 1
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador +1
        self.name = nome
        self.descricao=descricao
        self.valor=(valor* Produto.imposto)
        Produto.contador = self.id

class Usuario:
    def __init__(self, nome, email,senha):
        self.nome= nome
        self.email=email
        self.senha=senha



#atributos publicos eatributos privados
class Acesso:

    #exemplo com atributos privados
    #observe o undescore isso se chama mangling
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha
    
    def mostra_senha(self):
        print(self.__senha)
    def mostra_email(self):
        print(self.__email)

#exemplo
'''user = Acesso('user@gmail.com', '123456')
user.mostra_email()
user.mostra_senha()'''

#atributos de class -> são atributos declarados diretamente na classe
#atributos de instancia são os que tem o self
#atributos dinamicos são atributos de instancia criados em tempo de execução
#Atributos dinamicos serão exclusivos da classe que o criou

p1 = Produto('PS4', 'VideoGame', 2300)
p2 = Produto('xbox','Videogame', 4500)
print(p1.id)
print(p2.id)
#criando o atributo
p2.peso = '3kg'