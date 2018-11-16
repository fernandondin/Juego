#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from random import randint
import Proyectil
class Invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy,distancia,imagenUno,imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load(imagenUno)
        self.imagenB = pygame.image.load(imagenDos)
        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen=0
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()
        self.listaDisparo = []
        self.velocidad=4
        self.rect.top=posy
        self.rect.left=posx
        self.tiempoCambio=1
        self.rangoDisparo = 2
        self.tiempoCambio = 1
        self.conquista=False
        self.derecha=True
        self.contador=0
        self.MaxDescenso=self.rect.top+40
        self.limiteDerecha=posx+distancia
        self.limiteIzquierda=posx-distancia
    def comportamiento(self,tiempo):
        if not self.conquista:
            self.__movimientoLateral()
            self.__ataque()
        if self.tiempoCambio == tiempo:
            self.posImagen +=1
            self.tiempoCambio+=1
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen=0
    def dibujar(self,superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)
    def __ataque(self):
        if(randint(0,100)<self.rangoDisparo):
            self.__disparo()
    def __movimientos(self):
        if self.contador < 3:
            self.__movimientoLateral()
        else:
            self.__descenso()
    def __descenso(self):
        if self.MaxDescenso == self.rect.top:
            self.contador=0
            self.MaxDescenso=self.rect.top+40
        else:
            self.rect.top+=1
    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left=self.rect.left+self.velocidad
            if self.rect.left > self.limiteDerecha:
                self.derecha = False
                
                self.contador+=1
        else:
            self.rect.left = self.rect.left -self.velocidad
            if self.rect.left < self.limiteIzquierda:
                self.derecha = True
                
    def __disparo(self):
        x,y=self.rect.center
        proyectil = Proyectil.Proyectil(x,y,"Imagenes/proyectil1.png",False)
        self.listaDisparo.append(proyectil)
