class Blockchain(object):

    @staticmethod
    def generateHash(data):
        # Implemente aqui seu método para retornar a string referente ao hash SHA256 do argumento passado.
        # Não é necessário fazer o double SHA256. Uma vez é suficiente.
        # Confira a documentação do hashlib: https://docs.python.org/3/library/hashlib.html
        # Note que o argumento passado pode ser um objeto, portanto serialize o argumento antes.
        # Dica: Use o json.dumps() do módulo json para converter um objeto Python em uma string json. Garanta 
        # que a ordem dos atributos será sempre a mesma com a opção sort_keys=True.
        pass

# Testando sua implementação: espera-se um retorno com hashes gerada e esperada iguais.

data = {
            'nome': "Walter White",
            'idade': 45,
        }
expected_hash = "ef9ef3225f42aed9de1581f19c729083fce7f764b94c3fdbfb261c27399d5fff"
data_hash = Blockchain.generateHash(data)
print(f'Dados: {data}')
print(f'Hash   gerado: {data_hash}')
print(f'Hash esperado: {expected_hash}')
print(f'Hashes iguais: '+ ('SIM!\n' if expected_hash==data_hash else 'NÃO!\n')); 