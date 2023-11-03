DICIONARIOS: Dicionarios são coleção de dados de diversos valores. ao contrario das listas e tuplas o index dos dicionarios não são valores inteiros mas sim valores chamados de chaves. Os dicionarios são bem parecido com os tads de c. Um tipo dicionario são delimitado por {}. Ao contrario das listas e tuplas os elementos dos dicionarios são desordenados, por isso vc não consegue usar tecnicas tipo o slice.
a três metodos que vão retornar list-like. São eles: .values(), .key(),.items() eles podem ser utlizados em loops.Como nas listas podemos utilizar o in ou not in. pode se usar o methodo get tbm(é o recomendavel)
get():
    O metodo get recebe dois parametros, uma chave e um valor. Caso não tenha um valor corres podentem se retorna uma de fallback

IMPORTANTE:
    Dicionarios podem ser aninhados. É um caracteristica interessante pensando na possibilidade de criar estruturas mais complexas. 