nome = "Caique Rian Boaventura Barbuda"
altura = 1.88
peso = 150
imc = peso / (altura * altura)


abaixo_do_peso = 18.49
abaixo_do_peso_limite = 18.50

inicio_peso_saudavel = 18.50
fim_peso_saudavel2 = 24.9

inicio_Sobrepeso = 25
fim_Sobrepeso2 = 29.9

inicio_Obesidade_Grau_I = 30
fim_Obesidade_Grau_I2 = 34.9

inicio_Obesidade_Grau_II = 35
fim_Obesidade_Grau_II2 = 39.9

Obesidade_Grau_III_Obesidade_mórbida = 40

resultado = f"Olá, {nome}, Seu imc é : {imc:.2f} e logo abaixo você pode ver em qual classificação de peso você esta."

abaixo_do_peso_texto = f"Você esta abaixo do peso, um IMC abaixo de {abaixo_do_peso_limite:.2f} significa que voce esta abaixo do seu peso ideal, busque a ajuda de um medico especialista para te auxiliar em uma dieta Hipercalórica"

peso_saudavel_texto = f"Parabéns, você esta no seu peso ideal ou saudavel, essa classificação de 'PESO IDEAL' é de : {inicio_peso_saudavel:.2f} ATE {fim_peso_saudavel2:.2f}, então procure se exercitar e comer comidas saudáveis para manter o peso e continuar saudavel."


sobrepeso_texto = f"Você esta em sobrepeso, o sobrepeso inicia em {inicio_Sobrepeso:.2f} e tem como valor maximo dentro da classificação de sobrepeso o valor de {fim_Sobrepeso2:.2f}, seu peso esta um pouco acima do ideal, procure se exercitar e comer coisas mais saudáveis para perder o peso, mas acima de tudo procure um medico especialista para te auxiliar em uma dieta Hipocalórica"


obesidade_grau_I_texto = f"Voce esta no grau de Obesidade Grau I, essa classificação se inicia em {inicio_Obesidade_Grau_I:.2f} de IMC e que esta entre {fim_Obesidade_Grau_I2:.2f} de IMC nesse grau voce aumenta o risco de adquirir varios tipos de doenças, alguma delas são : Risco aumentado de doenças cardiovasculares, Diabetes tipo 2, Apneia do sono, Problemas respiratórios, Esteatose hepática, Problemas articulares, Distúrbios psicológicos, Problemas de fertilidade e Câncer, então recomendo que procure um medico especialista para te explicar mais sobre cada uma dessas doenças e para te ajudar no processo de emagrecimento"


Obesidade_Grau_II_texto = f"Você esta no estagio de obesidade Grau II, essa classificação se encontra entre {inicio_Obesidade_Grau_II:.2f} e {fim_Obesidade_Grau_II2:.2f} de IMC, esse estagio é muito arriscado, além de todas as doenças que podem ser adquiridas no grau I, você também tem risco de adquirir outros tipos como, Problemas Gastrointestinais, Complicações na Gravidez e etc, é fundamental que você procure ajuda o mais rápido possível, busque um medico especialista e mude seus hábitos para hábitos mais saudáveis"


Obesidade_Grau_III_Obesidade_mórbida_texto = f"Você esta no estagio de Obesidade Grau III ou Obesidade mórbida, esse é o ultimo estagio classificatorio de IMC, ele tem seu inicio em {Obesidade_Grau_III_Obesidade_mórbida:.2f} de IMC e segue desse valor adiante, além de todas as doenças que você pode já ter adquirido no grau II você também te possibilidade de adquirir elas e algumas outras como Dificuldades na Mobilidade e Complicações Cirúrgicas, é fundamental que você faça um acompanhamento medico, procure um medico o mais rápido possível, isso pode salvar sua vida"


print(resultado)


if imc <= abaixo_do_peso:
    print(abaixo_do_peso_texto)


elif imc >= inicio_peso_saudavel and imc <= fim_peso_saudavel2:
    print(peso_saudavel_texto)

elif imc >= inicio_Sobrepeso and imc <= fim_Sobrepeso2:
    print(sobrepeso_texto)

elif imc >= inicio_Obesidade_Grau_I and imc <= fim_Obesidade_Grau_I2:
    print(obesidade_grau_I_texto)

elif imc >= inicio_Obesidade_Grau_II and imc <= fim_Obesidade_Grau_II2:
    print(Obesidade_Grau_II_texto)
else:
    print(Obesidade_Grau_III_Obesidade_mórbida_texto)
