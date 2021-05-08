# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:19:49 2020

@author: nelson.junior
"""

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 10
        self.tentar_novamente = True
        
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute',size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
            ]
# Janela
        self.janela = sg.Window('Chute um numero!', layout)
        self.GerarNumeroAleatorio()        
        try:
            while True:
                # Receber os valores
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if self.valor_do_chute > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif self.valor_do_chute < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if self.valor_do_chute == self.valor_aleatorio:
                            self.tentar_novamente == False
                            print('Parabéns! Você acertou!!')
                            break
        except:
            print('Favor digitar apenas números')
            self.Iniciar()


    def LerValorDaTela(self):
        self.evento, self.valores = self.janela.Read()

   # def PedirValorAleatorio(self):
        #self.valor_do_chute = int(input('Chute um numero: '))
    
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
        
chute = ChuteONumero()
chute.Iniciar()
