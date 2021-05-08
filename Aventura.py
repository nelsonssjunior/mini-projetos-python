# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:57:21 2020

@author: nelson.junior
"""
import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no Norte ou no Sul? (n/s)'
        self.pergunta2 = 'Você prefere espada ou escudo? (espada/escudo)'
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico)'
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nesta batalha!'
    
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Output(size=(30,0),key='respostas')],
            [sg.Input(size=(25,0), key='escolha')],
            [sg.Button('Responder')],            
            ]
        self.janela = sg.Window('Jogo de Aventura!',layout)
        print(self.pergunta1)
        self.LerValores()       
        if self.valores['escolha'] == 'n':
            print(self.pergunta2)
            self.LerValores()
            if self.valores['escolha'] == 'espada':
                print(self.finalHistoria1)
            if self.valores['escolha'] == 'escudo':
                print(self.finalHistoria2)
        if self.valores['escolha'] == 's':
            print(self.pergunta3)
            if self.valores['escolha'] == 'linha de frente':
                print(self.finalHistoria3)
            if self.valores['escolha'] == 'tatico':
                print(self.finalHistoria4)
                
                     
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()
        
jogo = JogoDeAventura()
jogo.Iniciar()