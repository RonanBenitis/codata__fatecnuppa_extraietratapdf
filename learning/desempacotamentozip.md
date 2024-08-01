### SOBRE O ZIP: https://docs.python.org/3/library/functions.html#zip

### SOBRE OPERADOR DE DESEMPACOTAMENTO + ZIP
O operador `*` em Python é conhecido como o operador de desempacotamento. Ele tem várias utilidades dependendo do contexto em que é usado. Aqui estão algumas das principais funções:

### 1. Desempacotamento de Argumentos em Funções

Quando usado em chamadas de função, `*` desempacota uma lista ou tupla em argumentos posicionais:

```python
def soma(a, b, c):
    return a + b + c

valores = (1, 2, 3)
resultado = soma(*valores)  # Equivalente a soma(1, 2, 3)
print(resultado)  # Saída: 6
```

### 2. Desempacotamento de Iteráveis

Você pode usar `*` para desempacotar elementos de uma lista ou tupla em outra lista ou tupla:

```python
lista = [1, 2, 3]
nova_lista = [0, *lista, 4]
print(nova_lista)  # Saída: [0, 1, 2, 3, 4]
```

### 3. Desempacotamento em `zip`

Como vimos anteriormente, `*` pode desempacotar uma lista de tuplas para que `zip` possa reestruturar os dados:

```python
tuplas = [(1, 2), (3, 4), (5, 6)]
a, b = zip(*tuplas)
print(a)  # Saída: (1, 3, 5)
print(b)  # Saída: (2, 4, 6)
```

### 4. Desempacotamento em Listas e Tuplas

Você pode usar `*` para capturar múltiplos elementos em uma lista ou tupla:

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # Saída: 1
print(b)  # Saída: [2, 3, 4]
print(c)  # Saída: 5
```

### 5. Desempacotamento em Dicionários

O operador `**` é usado para desempacotar dicionários em chamadas de função:

```python
def mostrar_info(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

info = {'nome': 'Alice', 'idade': 30}
mostrar_info(**info)  # Equivalente a mostrar_info(nome='Alice', idade=30)
```

Esses são alguns dos usos mais comuns do operador `*` em Python. Ele é bastante versátil e pode simplificar muito o código em várias situações. Se precisar de mais alguma coisa, estou aqui para ajudar! 😊