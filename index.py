from os import system as limpa_tela
limpa_tela('cls')


class NumeroInvalidoExcept(Exception):
    pass


def encerra_gerador():
    print('\nGerador de senhas finalizado - Obrigado.\n')


def mensagem_com_enfeite(mensagem):
    limpa_tela('cls')
    print(enfeite_divisor)
    print(mensagem)
    print(enfeite_divisor)


versao = 'v1.1'
enfeite_divisor = '=' * 100
quantidade_caracteres_escolhido = ''
tipo_de_caracter_escolhido = ''
opcoes_de_caracter = ''


print(f'Gerador de Senhas - {versao}')
print(enfeite_divisor)

while True:
    try:
        quantidade_caracteres_escolhido = int(input(
            'Digite a quantidade de caracteres que deseja (de 4 a 50 caracteres ou 0 para finalizar): '))
        if 4 <= quantidade_caracteres_escolhido <= 50:
            break
        elif quantidade_caracteres_escolhido == 0:
            encerra_gerador()
            break
        else:
            raise NumeroInvalidoExcept
    except ValueError:
        mensagem_com_enfeite('!!! Digite um número !!!')
    except NumeroInvalidoExcept:
        mensagem_com_enfeite('!!! Digite um número entre 4 e 50 !!!')

print(enfeite_divisor)

while True:
    try:
        tipo_de_caracter_escolhido = int(input(
            '[1] Números.\n'
            '[2] Letras.\n'
            '[3] Números e letras.\n'
            '[4] Números, letras e caracteres especiais.\n'
            'Escolha quais caracteres a senha terá ou 0 para encerrar: '
        ))
        if 1 <= tipo_de_caracter_escolhido <= 4:
            break
        elif tipo_de_caracter_escolhido == 0:
            encerra_gerador()
            break
        else:
            raise NumeroInvalidoExcept
    except ValueError:
        mensagem_com_enfeite('!!! Digite um número !!!')
    except NumeroInvalidoExcept:
        mensagem_com_enfeite('!!! Digite um número entre 4 e 50 !!!')

match tipo_de_caracter_escolhido:
    case 1:
        opcoes_de_caracter = 'números'
    case 2:
        opcoes_de_caracter = 'letras'
    case 3:
        opcoes_de_caracter = 'números e letras'
    case 4:
        opcoes_de_caracter = 'números, letras e caracteres especiais'

if quantidade_caracteres_escolhido and tipo_de_caracter_escolhido:
    mensagem_com_enfeite(
        f'Aguarde, a senha de {quantidade_caracteres_escolhido} caracteres e contendo {opcoes_de_caracter} será gerada!')
