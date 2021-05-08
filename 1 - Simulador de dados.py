# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:56:52 2020

@author: nelson.junior
"""

#Simular o uso de um dado gerando um valor de 1 até 6.

import random
import PySimpleGUI as sg


'''
Criar layout
Criar uma Janela
Ler os valores da tela
fazer algo com esses valores
'''

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
        
    def Iniciar(self):
        # Criar Janela
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        
        try:                
            if self.eventos =='sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos  == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            (print('Ocorreu um erro ao receber sua resposta'))

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

