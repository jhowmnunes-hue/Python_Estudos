### Exercicio que calcule ou valide um CPF
# CPF tem uma série de regras contendo 11 digitos - formato: xxx.xxx.xxx-xx
# vamos trabalhar retirando a mascara (se necessario)
# como todo documento CPF pode ter 0 a esquerda
# se trabalhar como numero os 0 a esquerda podem sumir
# primeiro devo trabalhar como string para depois calcular digito a digito
# calculo tem uma série de regras
# Primeiro digito verificador é o calculo apartir dos 9 primeiro digitos

def validar_cpf(cpf):
    # removendo caracteres não numericos
    cpf = '' .join(filter(str.isdigit, cpf))

    # verificando se o CPF possui 11 digitos
    if len(cpf) != 11:
        return False

    # Verificando se todos os digitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calculando o primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto <2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # verificando o primeiro digito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False

    # Calculando o segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verificando o segundo digito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False

    # CPF valido
    return True

# Testando a função
cpf = '123.456.789-09'
if validar_cpf(cpf):
    print(f"O CPF {cpf} É válido. ")
else:
    print(f"O CPF {cpf} é inválido.")

    