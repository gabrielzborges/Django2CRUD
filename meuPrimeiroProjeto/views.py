from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
    return render(req, 'index.html')

def articles(req, year):
    return HttpResponse('O ano enviado foi: ' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27},
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}

def fname(req, nome):
    pessoa = lerDoBanco(nome)
    if pessoa['idade'] > 0:
        return HttpResponse('Nome: ' + pessoa['nome'] + ', Idade: ' + str(pessoa['idade']))
    else:
        return HttpResponse('Pessoa não encontrada')

def fname2(req, nome):
    person = lerDoBanco(nome)
    return render(req, 'pessoa.html', {'person': person})