# HTMLGen

## Descrição

HTMLGen, é um gerador de aquivos `html`, podendo ser usado em framewoks de desenvolvimento web para gerar páginas dinâmicas de meio rápido, prático e fácil.

## Instalação

Para se fazer a instalação, basta copiar o diretório de download para a `site-packages` dentro da versão desejada do python.

```bash
	# Faz o download do arquivo
	$ git clone https://github.com/Brumazzi/htmlgen-1.1.2.git htmlgen
	# # para a instalação, basta copiar os arquivos para o diretorio `site-packages`
	$ sudo cp htmlgen /usr/lib/python2.7/site-packages/
```

## Documentação

```
Classe HTMLContent - Tipo `object`
  Método __init__ - Parâmetros: `Sem parâmetros` - Retorno: `Sem retorno`
  Método create - Parâmetros: [`string`:`tag`], [`bool keyword`:`required = (default = False)`], [`keyword`:`**properts`] - Retorno : `self`
    `tag` : Tag html a ser criada.
    `required` : Define que o componente não pode ser `Null` ao submeter o formulário.
    `properts` : Propriedades e valores para o componente `id="obj1" class="objType" onclick=" console.log('action'); "`.
  Método close - Parâmetros: `Sem parâmetros` - Retorno: `self`
  Método end_page - Parâmetros: `Sem parâmetros` - Retorno: `self`
  Método innerHTML - Parâmetros: [`string`:`context`] - Retorno: `self`
    `context` : Conteúdo para a `tag` aberta.
  Método get_page : Parâmetros: `Sem parâmetros` - Retorno: `unicode string`
  Método get_page_min : Parâmetros: `Sem parâmetros` - Retorno: `unicode string`
  Método cursor : Parâmetros: `Sem parãmetros` - Retorno: `unicode string`

Classe Route - Tipo `object`
  Método __init__ - Parâmetros: `Sem parãmetros` - Retorno: `Sem retorno`
  Método new_route - Parâmetros: [`string`:`fname`], [`string`:`path`], [`string`:`alias`] - Retorno : `Sem retorno`
  Método call - Parâmetros: [`string`:`alias`], [`keyword`:`**vars`] - Retorno: `string`

------------------------------------------------------------------------------------------------------

HTMLContent
  `create`	- Cria um novo bloco de `tags` HTML.
  `close`	- Fecha um bloco HTML.
  `end_page`	- Fecha todos os blocos abertos.
  `innerHTML`	- Inseri um conteúdo dentro do bloco aberto.
  `get_page`	- Retorna a página HTML.
  `get_page_min`- Retorna a página HTML sem espaçamento e quebra de linhas.
  `cursor`	- Retorna a `tag` atualmente aberta.

Route
  `new_route`	- Cria uma nova rota para o arquivo `html`.
  `call`	- Carrega o arquivo `html` substituindo as variáveis pelas `keywords` e retorna o conteúdo página.
```

## Como informar Bugs

Qualquer identificação de `BUGs`, por favor entrar em contato com brumazzi_daniel@yahoo.com.br.

## Autor(es)

`Daniel Borges Brumazzi`

## Copyright

---
