Select Language: [English](https://github.com/bulfaitelo/Tesouro-Direto-Scraper/blob/master/README.md), **Portuguese**
========
# Tesouro direto Scraper  

Os scripts com uso de Selenium, extraem os dados da Tesouro direto, extraindo o extrato e os protocolos das operações, e retornando um json

## Instalação  

Caso prefira instalar pelo Composer: [composer](http://getcomposer.org/download/).

Rode o comando? 

```
composer require bulfaitelo/tesouro-direto-scraper

```
ou adicione ao `composer.json`

```json

"bulfaitelo/tesouro-direto-scraper": "^1.0",

```

## Requerimentos
  

- **selenium** (`$ pip install selenium`)
 

## Para Usar:
 

Execue o  `tesouro_direto_extrato.py` Com o cpf e senha, para você conseguir o extrato do dia

Execute o `tesouro_direto_protocolo.py` com cpf e senha, para pegar o protocolo do mês em questão

#### Opcional
Você pode adicionar um terceiro paraletro para que seja criado um printscrenn do erro (caso ocorra) basta passa como terceiri parametro o caminho de onde queria que seja salvo o erro. Você pode definir o nome do erro na da variavel :`default_file_name = 'erro.png'`

### Exemplos de Uso  

$ python tesouro_direto_extrato.py 1234567890 pass123

$ python tesouro_direto_extrato.py 1234567890 pass123 c:\error\dir/

$ python tesouro_direto_protocolo.py 1234567890 pass123

$ python tesouro_direto_protocolo.py 1234567890 pass123 /var/error/dir/

$ python tesouro_direto_precos_taxa_titulo.py

$ python tesouro_direto_precos_taxa_titulo.py /project_path/errors/ 

## Retorno  

Retorna o `json` com os seguintes dados:

### Extrato:  

- titulo

  

- vencimento
- valor_investido
- valor_bruto_atual
- valor_liquido_atual
- quant_total
- quant_bloqueado
  

### Protocolo:
- numero_protocolo
- operacao
- situacao
- realizacao
- liquidacao
- nome_representante
- titulo
- quantidade
- valor_unitario
- taxa_juros
- taxa_b3
- taxa_custodia
- valor_total
  

### Protocolo:
- numero_protocolo
- operacao
- situacao
- realizacao
- liquidacao
- representante
- titulo
- quantidade
- valor_unitario
- taxa_juros
- taxa_b3
- taxa_custodia
- valor_total
