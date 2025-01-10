# *Validador de Bandeira de Cartão de Crédito*

**Este projeto contém um script em Python para validar a bandeira (marca) de um cartão de crédito com base no número do cartão.**

# *Funcionamento*

**O script verifica o número do cartão de crédito fornecido pelo usuário usando padrões de expressões regulares para identificar a bandeira do cartão. As bandeiras suportadas são: Visa, Mastercard, Elo, American Express, Discover e Hipercard.**

*Estrutura do Código*

*Importação da Biblioteca*
**A biblioteca re é usada para trabalhar com expressões regulares.**

**Função validar_bandeira**
**Esta função recebe o número do cartão de crédito como entrada e verifica se a bandeira é válida.**

*Dicionário de Bandeiras e Padrões*
**O dicionário bandeiras contém as expressões regulares que definem os padrões dos números de cartões de cada bandeira.**

*Validação da Bandeira*
**A função percorre cada bandeira e seu respectivo padrão no dicionário. Se o número do cartão corresponder ao padrão de alguma bandeira, a função retorna a bandeira e a mensagem "Válido". Caso contrário, retorna "Bandeira: Invalida".**

*Input do Usuário*
**O usuário é solicitado a digitar o número do cartão de crédito, que é validado pela função validar_bandeira e o resultado é impresso.**
