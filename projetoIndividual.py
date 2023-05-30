candidatos = [
    ('Candidato 1',5,10,8,8),#Lista de candidatos
    ('Candidato 2',10,7,7,8),
    ('Candidato 3',8,5,4,9),
    ('Candidato 4',2,2,2,1),
    ('Candidato 5',10,10,8,9)]

def verificar_canditados(nota_min1, nota_min2, nota_min3, nota_min4): #Funções 
    lista_canditados = []
    for candidato in candidatos:
        nome_candidato = candidato[0]
        nota01 = candidato[1]
        nota02 = candidato[2]
        nota03 = candidato[3]
        nota04 = candidato[4]
        if nota01 >= nota_min1 and nota02 >= nota_min2 and nota03 >= nota_min3 and nota04 >= nota_min4:
            lista_canditados.append(nome_candidato)
    return lista_canditados
def inicio_programa():
    print('Ola, seja bem vindo!')
    quantidade_vezes = int(input('Informe quantas vezes deseja verificar as notas: '))
    for i in range(quantidade_vezes):
        if i == 0:
            print('Informe as notas mínimas:')
        else:
            print(f'Informe as notas mínimas do {i+1} candidato:')
        nota_min1 = int(input('Nota minima 1: '))
        nota_min2 = int(input('Nota minima 2: '))
        nota_min3 = int(input('Nota minima 3: '))
        nota_min4 = int(input('Nota minima 4: '))
        lista_canditados = verificar_canditados(nota_min1, nota_min2, nota_min3, nota_min4)
        if len(lista_canditados) > 0:
            print('Candidatos que possuem a nota minima informada:')
            for candidato in lista_canditados:
                print(candidato)
        else:
            print("Nenhum canditado conseguiu a nota minima.")
inicio_programa()