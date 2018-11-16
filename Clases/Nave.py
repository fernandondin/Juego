#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import Proyectil
import threading
import time
class naveEspacial(pygame.sprite.Sprite):
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        #self.ImagenExplosion=pygame.image.load('Imagenes/explota.png')
        self.ImagenN=pygame.image.load("Imagenes/nave.png")
        self.listaImagen=[self.ImagenN]
        self.ImagenNave=self.listaImagen[0]
        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-35
        self.listaDisparo=[]
        self.Vida=True
        self.velocidad=20
        pygame.mixer.init()  
        self.sonido = pygame.mixer.Sound('Sonidos/disparo3.wav')
        self.sonidoExplosion = pygame.mixer.Sound('Sonidos/Explosion.wav')
        self.timeExplosion=10
        self.llenaLista()
        self.explosion=1
    def llenaLista(self):
        for i in range(self.timeExplosion):
            self.listaImagen.append(pygame.image.load("Imagenes/explota"+str(i)+".png"))
    def dispara(self,x,y):
        proyectil = Proyectil.Proyectil(x,y,"Imagenes/proyectil.png",True)
        self.listaDisparo.append(proyectil)
        self.sonido.play()
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave,self.rect)
    def animaExplosion(self,n):
        print("entro")
        self.ImagenNave = self.listaImagen[n]
    def destruccion(self):
        if(self.explosion ==1):
            self.sonidoExplosion.play()
        if(self.explosion < self.timeExplosion):
            self.vida=False
            self.velocidad=0
            self.animaExplosion(self.explosion)
            self.explosion=self.explosion+1
    def revive(self):
        self.velocidad = 20
        self.ImagenNave = self.listaImagen[0]
        self.explosion=1
        
