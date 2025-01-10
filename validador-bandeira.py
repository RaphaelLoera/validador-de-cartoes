# importação da biblioteca re para utilizar expressões regulares
import re

# Esta função recebe o número do cartão de crédito e verifica se a bandeira é válida.
def validar_bandeira(cartao):
    bandeiras = {
        'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
        'Mastercard': r'^(5[1-5][0-9]{14}|2(2[2-9][0-9]{12}|[3-6][0-9]{13}|7[01][0-9]{12}|720[0-9]{12}))$',
        'Elo': r'^(4011|4312|4389|4514|4576|5041|5066|5090|6277|6362|6363|6504|6505|6506|6507|6509|6516|6550|6551|6552)[0-9]{12}$',
        'American Express': r'^3[47][0-9]{13}$',
        'Discover': r'^(6011|65|64[4-9])[0-9]{12,15}$',
        'Hipercard': r'^6062[0-9]{12}$'
    }
# Se a bandeira do cartão for válida, a função retorna a bandeira e a mensagem "Válido". Caso contrário, retorna "Bandeira: Invalida". 
    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, cartao):
            return f'Bandeira: {bandeira}, Válido.'
    return 'Bandeira: Invalida'

# Input do usuário para digitar o número do cartão de crédito
cartao_usuario = input("Digite o número do cartão de crédito: ").strip()
# Printa a função validar_bandeira com o input do usuário
print(validar_bandeira(cartao_usuario))

