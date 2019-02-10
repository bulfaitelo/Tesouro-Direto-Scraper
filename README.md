Select Language: **English**, [Portuguese](https://github.com/bulfaitelo/Tesouro-Direto-Scraper/blob/master/README-pt.md)
========
# Tesouro direto Scraper  

The scripts with selenium use, extracts the data from the direct treasury, extracting the extract and the protocols from the operations, and returning a json  

## Installation  

The preferred way to install the Yii framework is through [composer](http://getcomposer.org/download/).

Either run  

```
composer require bulfaitelo/tesouro-direto-scraper

```
or add

```json

"bulfaitelo/tesouro-direto-scraper": "^1.0",

```

  

to the require section of your composer.json.

  

## Requeriments
  

- **selenium** (`$ pip install selenium`)
 

## To use
 

Run tesouro_direto_extrato.py whit cpf and password, you get current extract

  

To tesouro_direto_protocolo.py with cpf and password, you get current month protocol.

#### Optional
You can add a third parameter, to create a print screen error, defining file path. You can define erro name on `default_file_name = 'erro.png'`


### Example

  

$ python tesouro_direto_extrato.py 1234567890 pass123

$ python tesouro_direto_extrato.py 1234567890 pass123 c:\error\dir/

$ python tesouro_direto_protocolo.py 1234567890 pass123

$ python tesouro_direto_protocolo.py 1234567890 pass123 /var/error/dir/

$ python tesouro_direto_precos_taxa_titulo.py

$ python tesouro_direto_precos_taxa_titulo.py /project_path/errors/ 

## Return  

Returns a json with the data: 

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
