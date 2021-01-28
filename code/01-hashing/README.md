# Atividade: Hashing

Esta atividade tem como objetivo implementar o primeiro método no desenvolvimento do nosso **blockchain**. Este método estático será amplamente utilizado em várias etapas do processo, uma vez que *hashing* é uma das técnicas essenciais para o funcionamento deste modelo de blockchain.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas deve ser realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize a IDE de sua preferência (sugestão: Visual Studio Code).

As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instruções de submissão

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários. Todos os *boilerplates* são compatíveis com o Python 3+.

## Descrição

A assinatura do método já está presente na classe `Blockchain`:

```python
@staticmethod
def generateHash(data):
```

Importe o módulo `hashlib` a sua classe e implemente o método `generateHash` para retornar a string referente ao *hash* **SHA256** do argumento passado. Note que o argumento passado pode ser um objeto, portanto serialize o argumento antes (veja em [Dicas](#dicas)).

O arquivo contém um simples teste para verificar se o *output* do seu método está retornando o *hash* esperado para o *input* fornecido.

## Dicas

Confira a documentação do hashlib [https://docs.python.org/3/library/hashlib.html] para verificar como utilizar a função SHA256.

Usar `json.dumps()` do módulo `json` para serializar o objeto de entrada em uma string no formato JSON antes, e lembrar de manter a estrutura sempre ordenada (`sort_keys=True`). Assim temos a garantia de que a função irá retornar o mesmo *hash* independentemente da ordem em que as chaves são apresentadas, crucial para validação de algumas estruturas de nosso blockchain.

```python
json.dumps(data, sort_keys=True)
```

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
