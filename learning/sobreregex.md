Claro! As expressões regulares (regex) são uma ferramenta poderosa para a correspondência de padrões em texto. Vamos fazer um tour pelos principais símbolos e suas funções, divididos em categorias.

### 1. **Caractere Literais**
- **`a`**: Corresponde ao caractere `a`.
- **`.`**: Corresponde a qualquer caractere, exceto uma nova linha.

### 2. **Metacaracteres**
- **`^`**: Corresponde ao início da string.
- **`$`**: Corresponde ao fim da string.
- **`\d`**: Corresponde a qualquer dígito (equivalente a `[0-9]`).
- **`\D`**: Corresponde a qualquer caractere que não seja um dígito.
- **`\w`**: Corresponde a qualquer caractere alfanumérico (equivalente a `[a-zA-Z0-9_]`).
- **`\W`**: Corresponde a qualquer caractere não alfanumérico.
- **`\s`**: Corresponde a qualquer espaço em branco (espaço, tab, nova linha, etc.).
- **`\S`**: Corresponde a qualquer caractere que não seja espaço em branco.

### 3. **Quantificadores**
- **`*`**: Corresponde a zero ou mais ocorrências do caractere anterior.
- **`+`**: Corresponde a uma ou mais ocorrências do caractere anterior.
- **`?`**: Corresponde a zero ou uma ocorrência do caractere anterior.
- **`{n}`**: Corresponde exatamente a `n` ocorrências do caractere anterior.
- **`{n,}`**: Corresponde a `n` ou mais ocorrências do caractere anterior.
- **`{n,m}`**: Corresponde a entre `n` e `m` ocorrências do caractere anterior.

### 4. **Grupos e Alternância (ver abaixo sobre Grupos)**
- **`(abc)`**: Corresponde exatamente à sequência `abc`.
- **`a|b`**: Corresponde a `a` ou `b`.
- **`(a|b)`**: Corresponde a `a` ou `b`.

### 5. **Classes de Caracteres**
- **`[abc]`**: Corresponde a qualquer caractere dentro dos colchetes (`a`, `b`, ou `c`).
- **`[^abc]`**: Corresponde a qualquer caractere que não esteja dentro dos colchetes.
- **`[a-z]`**: Corresponde a qualquer caractere no intervalo de `a` a `z`.
- **`[A-Z]`**: Corresponde a qualquer caractere no intervalo de `A` a `Z`.
- **`[0-9]`**: Corresponde a qualquer dígito.

### 6. **Âncoras e Limites**
- **`\b`**: Corresponde a uma borda de palavra (entre um caractere `\w` e um `\W`).
- **`\B`**: Corresponde a uma posição que não seja uma borda de palavra.

### 7. **Retrovisores**
- **`\1`, `\2`, etc.**: Correspondem ao texto correspondente do grupo de captura número 1, 2, etc.

### Exemplos Práticos

1. **Correspondência de um número de telefone no formato `(xx) xxxx-xxxx`**:
    ```regex
    \(\d{2}\) \d{4}-\d{4}
    ```
   - `\(`: Corresponde ao caractere `(`.
   - `\d{2}`: Corresponde a exatamente dois dígitos.
   - `\)`: Corresponde ao caractere `)`.
   - `\d{4}`: Corresponde a exatamente quatro dígitos.
   - `-`: Corresponde ao caractere `-`.
   - `\d{4}`: Corresponde a exatamente quatro dígitos.

2. **Correspondência de um endereço de e-mail**:
    ```regex
    \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
    ```
   - `\b`: Âncora de borda de palavra.
   - `[A-Za-z0-9._%+-]+`: Corresponde a um ou mais caracteres alfanuméricos ou os caracteres `.`, `_`, `%`, `+`, `-`.
   - `@`: Corresponde ao caractere `@`.
   - `[A-Za-z0-9.-]+`: Corresponde a um ou mais caracteres alfanuméricos ou os caracteres `.` ou `-`.
   - `\.`: Corresponde ao caractere `.`.
   - `[A-Z|a-z]{2,}`: Corresponde a duas ou mais letras (maiusculas ou minúsculas).
   - `\b`: Âncora de borda de palavra.

### Aplicação em Python

Aqui está um exemplo de como usar essas expressões regulares em Python para capturar o número ao lado de "Preços" e a data após "Minor Harada":

```python
import re

# Exemplo de texto extraído do PDF
text = """
Boletim Semanal de Preços 53/2024
Amostra de preços médios unitários do atacado de produtos classificados como AA pelos permissionários, no
Mercado Municipal do Produtor Rural de Mogi das Cruzes “Minor Harada” em 17/07/2024.
"""

# Expressões regulares para capturar as informações desejadas
preco_pattern = r"Preços\s+(\d+\/\d{4})"
data_pattern = r"Minor Harada[^\d]*(\d{2}\/\d{2}\/\d{4})"

# Encontrar os padrões no texto
preco_match = re.search(preco_pattern, text)
data_match = re.search(data_pattern, text)

# Extrair os valores encontrados
preco = preco_match.group(1) if preco_match else "Não encontrado"
data = data_match.group(1) if data_match else "Não encontrado"

print(f"Boletim Semanal de Preços: {preco}")
print(f"Data após 'Minor Harada': {data}")
```

### Conclusão

As expressões regulares são uma ferramenta poderosa e versátil para correspondência de padrões em texto. Com a prática, você pode construir expressões regulares para praticamente qualquer tarefa de processamento de texto. Se precisar de mais ajuda ou tiver dúvidas específicas, estarei à disposição para ajudar!

### SOBRE GRUPOS DE CAPTURA

Os parênteses em expressões regulares são usados para criar grupos de captura. Eles desempenham um papel crucial na extração e manipulação de partes específicas do texto correspondido. Vamos detalhar o que eles fazem e o que acontece se não os utilizarmos.

### Grupos de Captura

1. **Criação de Grupos de Captura**:
   - **Parênteses `()`**: Envolvem uma parte do padrão e permitem que você capture essa parte do texto correspondente para uso posterior. O texto que corresponde ao padrão dentro dos parênteses é salvo em um grupo de captura.

   No exemplo:
   ```regex
   Minor Harada[^\d]*(\d{2}\/\d{2}\/\d{4})
   ```
   O padrão `(\d{2}\/\d{2}\/\d{4})` está dentro dos parênteses, o que significa que essa parte do texto correspondente será capturada e poderá ser acessada separadamente.

2. **Acesso aos Grupos de Captura**:
   - Após a correspondência, você pode acessar o texto que foi capturado pelos parênteses usando `group(1)`, `group(2)`, etc., onde o número representa a ordem do grupo de captura.

### Exemplo com Parênteses

**Código com Parênteses:**

```python
import re

text = "Mercado Municipal do Produtor Rural de Mogi das Cruzes “Minor Harada” em 17/07/2024."

# Padrão com grupos de captura
data_pattern = r"Minor Harada[^\d]*(\d{2}\/\d{2}\/\d{4})"
data_match = re.search(data_pattern, text)

# Extrair e imprimir a data
data = data_match.group(1) if data_match else "Não encontrado"
print(f"Data após 'Minor Harada': {data}")
```

**Saída:**

```
Data após 'Minor Harada': 17/07/2024
```

**Explicação**:
- O padrão `(\d{2}\/\d{2}\/\d{4})` captura a data no formato `dd/mm/aaaa`.
- `group(1)` acessa o texto capturado pelo primeiro grupo de captura, que é a data.

### Sem Parênteses

Se você remover os parênteses:

**Código Sem Parênteses:**

```python
import re

text = "Mercado Municipal do Produtor Rural de Mogi das Cruzes “Minor Harada” em 17/07/2024."

# Padrão sem grupos de captura
data_pattern = r"Minor Harada[^\d]*\d{2}\/\d{2}\/\d{4}"
data_match = re.search(data_pattern, text)

# O grupo de captura não está presente
data = data_match.group() if data_match else "Não encontrado"
print(f"Data após 'Minor Harada': {data}")
```

**Saída:**

```
Data após 'Minor Harada': Minor Harada em 17/07/2024
```

**Explicação**:
- O padrão `Minor Harada[^\d]*\d{2}\/\d{2}\/\d{4}` corresponde ao texto completo que inclui "Minor Harada" e a data.
- `group()` retorna o texto completo correspondente ao padrão, e não apenas a data.

### Resumo

- **Com Parênteses**: Você pode capturar partes específicas do texto e acessá-las separadamente. Isso é útil para extrair dados específicos, como datas, números, ou qualquer outra informação relevante dentro do texto.
- **Sem Parênteses**: O padrão corresponde ao texto completo, sem separar ou capturar partes específicas.

Se precisar de mais detalhes ou tiver outras perguntas sobre expressões regulares ou qualquer outro assunto, sinta-se à vontade para perguntar!

### EXEMPLOS DE UTILIZAÇÃO
```PYTHON
import re

# Texto de exemplo
text = "The cat sat on the catalog concatenating various categories of catnip."

# Encontrar palavras que começam com 'cat'
pattern_start = r"\bcat\w*"
matches_start = re.findall(pattern_start, text)
print(f"Palavras que começam com 'cat': {matches_start}")

# Encontrar palavras que terminam com 'cat'
pattern_end = r"\w*cat\b"
matches_end = re.findall(pattern_end, text)
print(f"Palavras que terminam com 'cat': {matches_end}")

# Encontrar a palavra 'cat' exatamente
pattern_exact = r"\bcat\b"
matches_exact = re.findall(pattern_exact, text)
print(f"Palavra 'cat' exatamente: {matches_exact}")

# Encontrar 'cat' que não está no início nem no fim de uma palavra
# Importante:
# r"\w*\Bcat\B\w*" (concatenating)
# r"\B\w*cat\w*\B" (oncatenatin)
pattern_inside = r"\w*\Bcat\B\w*"
matches_inside = re.findall(pattern_inside, text)
print(f"'cat' dentro de uma palavra: {matches_inside}")

# Encontrar todas as palavras que em qualquer posição tenha 'cat'
pattern_inside = r"\w*cat\w*"
all_matches = re.findall(pattern_inside, text)
print(f"'cat' dentro de uma palavra: {all_matches}")
```