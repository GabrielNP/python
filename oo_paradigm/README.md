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
Para desreferenciar --> indica que uma referência não aponta mais para um objeto.
```
outraRef = None
```

# Métodos estáticos
Métodos que conseguimos chamar sem uma referência recebem o nome de estáticos, porque eles fazem parte da classe.
``` @staticmethod
    def codigo_banco():
    return "001"
```

# Atributo estático
Faz parte da classe, ou seja, é um atributo que pode ser usado sem ter criado um objeto. É possível alterar o valor deste atributo mudando seu estado e não é necessário criar uma instância para acessá-lo. Precisamos usar o __class__ para definir que queremos o atributo de classe. 
```
class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False
```

# Métodos de Classe
São acessíveis sem necessidade de criar uma instância.

São métodos declarados com @classmethod. Quando criamos um método de classe, temos acesso aos atributos da classe. Da mesma forma com os atributos de classe, podemos acessar estes métodos de dentro dos métodos de instância, a partir de __class__, se desejarmos:

```
class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'
```
Perceba que, ao invés de self, passamos cls para o método, já que neste caso sempre recebemos uma instância da classe como primeiro argumento. O nome cls é uma convenção, assim como self.


# Representação textual de objetos 
`__str__` Função interna do python dedicada à exibição de textos para o usuário final.

# Representação de log/debugs
`__repr` 
``` 

```