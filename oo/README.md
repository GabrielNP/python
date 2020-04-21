Estudo baseado no curso https://cursos.alura.com.br/course/python-3-intro-orientacao-objetos

# O paradigma de orientação a objetos
A ideia central do paradigma da Orientação a Objetos: dado e funcionalidade (comportamentos) andam juntos.

# Variáveis
Em Orientação a Objetos, as variáveis são denominadas referências

# Atributos
 e atributos são conteúdo da classe, as características.

# Função construtora
```
def __init__(self):
self é a referência que sabe encontrar o objeto construído em memória. 
```
# Coletor de lixo
Dentro da máquina virtual, na execução do Python, existe um processo que procura os objetos esquecidos. Os itens inutilizados serão apagados e o espaço livre em memória será reutilizado. No caso, o responsável por jogar fora esses objetos em desuso é o coletor de lixo (garbage collector, em inglês) do Python.

# None
Para desreferenciar --> indica que uma referência não aponta mais para um objeto
`outraRef = None`