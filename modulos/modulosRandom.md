Gera um numero pseudo aleatorio entre 0 e 1 ->random.random()

Função uniform() -> gera um numero pseudo aleatorio entre um tervalo especificado
    from random import uniform
    
    for i in range(10):
        print(uniform(3, 7)) -> o numero final não é incluido ou seja

Função randint() -> Gera um numero inteiro pseudo aleatorio entre um intervalo especificado
    from random import randint
    
    #usa bastante em rede neurais
    for i in range(10):
        print(randint(3, 55), end=', ')

Função choice() - > Mostra um valor aleatorio interavel
Isso aqui é bemmmm interessante
    from random import choice
    jogadas = ['pedra','papel', 'tesoura']
    print(choice(jogadas))

Função shuffle() - > tem a função de embaralhar dados
    from random import shuffle
    cartas = ['K', 'Q', 'J', 'A', '2', '3','4', '5','6','7']
    print(cartas)
    shuffle(cartas)
    print(cartas)