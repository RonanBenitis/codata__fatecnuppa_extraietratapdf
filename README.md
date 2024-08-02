![Static Badge](https://img.shields.io/badge/status-released-brightgreen)
![Static Badge](https://img.shields.io/badge/version-3-brightgreen)

# EXTRAÇÃO E PRÉ-PROCESSAMENTO DE TABELAS - FATEC NUPPA
Este programa destina-se à "raspagem" dos [boletins semanais do Núcleo de Pesquisas em Preços Agrícolas (NUPPA)](https://www.fatecmogidascruzes.com.br/admin/workGroups/view/NUPPA) para captura e estruturação da tabela e captura de dados desejados.

Em linhas gerais, o programa captura a tabela e o texto do PDF - através de bibliotecas específicas Python - tratando e organizando os dados obtidos - através de regex - e os estrutura em um novo DataFrame.

O produto deste processamento será utilizado para estruturação (script de processamento dos dados obtidos) e consumo para manipulação e visualização do dashboard em PowerBI

## Funcionamento
- `main.py` = script destinado a:
  - Buscar os PDF's e estruturá-los em listas;
  - Chamar a função `estrutura_tabela_pdf` dentro da iteração;
  - Salvar o retorno da função `estrutura_tabela_pdf`.
- `structpdftable.py` = script da função `estrutura_tabela_pdf`, destinado a:
  - Receber caminho para o arquivo PDF;
  - Chamar a função `get_boletim_and_coleta` para capturar o nº do boletim e a data de coleta;
  - Capturar a tabela do PDF;
  - Gerar arquivo `.xslx` da tabela capturada (planilha bruta, para conferência);
  - Realizar tratamentos da planilha capturada;
  - Chamar a função `cell_to_col` para capturar a unidade de medida e os valores do produto;
  - Atribuir os valores tratados para as colunas do Dataframe Destino;
  - Retorna o número do boletim e o DatFrame destino.
- `getboletimandcoleta.py` = script da função `get_boletim_and_coleta`, destinado a:
  - Receber caminho para o arquivo PDF;
  - Capturar o texto do PDF lido;
  - No texto do PDF, utilizando regex, buscar o nº do boletim e a data da coleta;
  - Retornar o nº do boletim e a data da coleta.
- `celltocol.py` = script da função `cell_to_col`, destinado a:
  - Receber valor da celula, da tabela, a ser tratada;
  - Realizar tratamentos através regex;
  - Capturar os valores desejados através de regex;
  - Retornar os valores capturados.