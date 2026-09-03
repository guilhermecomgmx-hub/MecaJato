from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . models import Cliente, Carros
import re
import json
# Create your views here.

def clientes(request):
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, "clientes.html", {"clientes": clientes_list})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            return render(request, "clientes.html", {"nome":nome, "sobrenome": sobrenome, "email": email, 'carros': zip(carro, placa, ano)})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {"nome":nome, "sobrenome": sobrenome, "cpf": cpf, 'carros': zip(carro, placa, ano)})  

        
        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        cliente.save()

        for carro, placa, ano in zip(carro, placa, ano):
            carro_obj = Carros(
                carro = carro,
                placa = placa,
                ano = ano,
                cliente = cliente
            )
            carro_obj.save()

        return redirect('clientes')


def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    print(cliente_json) 
    return JsonResponse(cliente_json)