# Programa de concessão de aposentadoria

print('Programa para avaliação de concessão de aposentadoria')

print('Para verificar preencha os seus dados:')

nome = input('Digite o seu nome: ')
sexo =input ('Digite o seu sexo M ou F: ')
idade = input('Digite a sua idade:')


# Codigo se masculino
if sexo.upper() == "M":     # No lugar de == poderia ser usado a expressão *is*
    if int(idade) >= 65:
        print(f'Parabéns {nome}! aposentadoria concedida!!!')
    else:
        print(f'Que pena {nome}, ainda não foi possivel conceder a sua aposentadoria, aguande mais {65 -int(idade)} anos.')

# Codigo se feminino
elif sexo.upper() == "F":
    if int(idade) >= 60:
        print(f'Parabéns {nome}! aposentadoria concedida!!!')
    else:
        print(
            f'Que pena {nome}, ainda não foi possivel conceder a sua aposentadoria, aguande mais {60 - int(idade)} anos.')

else:
    print("Você digitor uma opição invalida tente de novo com M ou F!")





