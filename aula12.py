nome = str(input('Digite seu nome?: '))
if nome == 'Gustavo':
    print('Que nome bonito {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))
