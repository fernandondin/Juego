#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import Proyectil
class naveEspacial(pygame.sprite.Sprite):
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave=pygame.image.load('Imagenes/nave.png')
        self.ImagenExplosion=pygame.image.load('Imagenes/Marciano.png')
        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-35
        self.listaDisparo=[]
        self.Vida=True
        self.velocidad=20
        pygame.mixer.init()  
        self.sonido = pygame.mixer.Sound('Sonidos/disparo3.wav')
        self.sonidoExplosion = pygame.mixer.Sound('Sonidos/Explosion.wav')
    def dispara(self,x,y):
        proyectil = Proyectil.Proyectil(x,y,"Imagenes/proyectil.png",True)
        self.listaDisparo.append(proyectil)
        self.sonido.play()
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave,self.rect)
    def destruccion(self):
        self.sonidoExplosion.play()
        self.vida=False
        self.velocidad=0
        self.imagenNave = self.ImagenExplosion
