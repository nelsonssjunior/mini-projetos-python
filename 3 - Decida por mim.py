# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:12:33 2020

@author: nelson.junior
"""
import random
import PySimpleGUI as sg

class DecidaPormim:
    def __init__(self):
        self.respostas = ['Com certeza, você deve fazer isso',
                          'Não sei, você é quem sabe',
                          'Não faça isso',
                          'Acho que está na hora!']
            
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Decida por mim')]            
            ]
        # criar janela
        self.janela = sg.Window('Decida por mim', layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
                self.janela.Read()
        
decida = DecidaPormim()
decida.Iniciar()
    