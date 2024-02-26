#Implemente um programa que leia um valor em reais e mostre o valor em dolar
import requests
import json
requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
cotacao = requisicao.json()
dolar = float(cotacao['USD']['bid'])
real = float(input("valor em real: R$"))
print(f'Valor em dolar: ${real*dolar}')
