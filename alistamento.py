sexo = int(input('Qual seu genero:[1] MASCULINO [2] FEMININO '))
if (sexo == 1):
    atual = date.today().year
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento,idade,atual))
    pass
    if idade == 18:
        print('Você deve tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(' Ainda faltam {} anos para o seu alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade >18:
        saldo = idade - 18
        print('Você já deveria está alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Você não precisa se alistar, mas caso queira seguir carreira procure um concurso.')

