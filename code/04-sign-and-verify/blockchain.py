import hashlib
import json
from time import time
import copy
import bitcoinlib # pip install bitcoin

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash valido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        # Cria o bloco genêsis
        self.createBlock(previousHash='0'*64, nonce=0)
        self.mineProofOfWork(self.prevBlock) 

    def createBlock(self, nonce=0, previousHash=None):
        # Retorna um novo bloco criado e adicionado ao blockchain (ainda não minerado).
        if (previousHash == None):
            previousBlock = self.chain[-1]
            previousBlockCopy = copy.copy(previousBlock)
            previousBlockCopy.pop("transactions", None)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': '0'*64,
            'nonce': nonce,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
        }

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, prevBlock):
        # Retorna o nonce que satisfaz a dificuldade atual para o bloco passado como argumento.
        nonce = 0
        while self.isValidProof(prevBlock, nonce) is False:
            nonce += 1

        return nonce

    @staticmethod
    def isValidProof(block, nonce):
        # Retorna True caso o nonce satisfaça a dificuldade atual para o bloco passado como argumento.
        block['nonce'] = nonce
        guessHash = Blockchain.getBlockID(block)
        return guessHash[:DIFFICULTY] == '0' * DIFFICULTY 

    @staticmethod
    def generateHash(data):
        # Retorna o SHA256 do argumento passado.
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        # Retorna o ID (hash do cabeçalho) do bloco passado como argumento.
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        return Blockchain.generateHash(blockCopy)

    def printChain(self):
        # Imprime no console um formato verboso do blockchain.
        print(json.dumps(self.chain, indent=2, sort_keys=True))
        pass # Mantenha seu metodo de impressao do blockchain feito na pratica passada.

    @property
    def prevBlock(self):
        # Retorna o último bloco incluído no blockchain.
        return self.chain[-1]

    @staticmethod
    def getWifCompressedPrivateKey(private_key=None):
        # Retorna a chave privada no formato WIF-compressed da chave privada hex.
        if private_key is None:
            private_key = bitcoinlib.random_key()
        return bitcoinlib.encode_privkey(bitcoinlib.decode_privkey((private_key + '01'), 'hex'), 'wif')
        
    @staticmethod
    def getBitcoinAddressFromWifCompressed(wif_pkey):
        # Retorna o endereço Bitcoin da chave privada WIF-compressed.
        return bitcoinlib.pubtoaddr(bitcoinlib.privkey_to_pubkey(wif_pkey))

    @staticmethod
    def sign(wifCompressedPrivKey, message):
        # Retorna a assinatura digital da mensagem e a respectiva chave privada WIF-compressed.
        return bitcoinlib.ecdsa_sign(message, wifCompressedPrivKey)

    @staticmethod
    def verifySignature(address, signature, message):
        # Verifica se a assinatura é correspondente a mensagem e o endereço BTC.
        # Você pode verificar aqui também: https://tools.bitcoin.com/verify-message/
        return bitcoinlib.ecdsa_verify(message, signature, address)


# Teste
# Fique a vontade para criar outra chave privada aleatória
# Você pode usar o método getBitcoinAddressFromWifCompressed() para pegar o endereço WIF a partir da chave privada
# Ou use um gerador de chaves/endereços. Ex: https://www.bitaddress.org/

addr = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF'
privKey = 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U'
message = 'Bora assinar essa mensagem?'

signature = Blockchain.sign(privKey, message)

print('Mensagem: {}'.format(message))
print('Endereço BTC: {}'.format(addr))
print('Assinatura gerada: {}'.format(signature))
print('Assinatura válida para mensagem e endereço indicado? {}'.format(Blockchain.verifySignature(addr, signature, message)))

