#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame,sys
from pygame.locals import *
from random import randint
from pygame import mixer
from Clases import Nave
from Clases import Invasor
import threading
class Button():
    def __init__(self,color,posX,posY,width,height,text,font,sfont):
        self.color=color
        self.posX=posX
        self.posY=posY
        self.width=width
        self.height=height
        self.text=text
        self.font=font
        self.sfont=sfont
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.posX,self.posY,self.width,self.height),0)
        font = pygame.font.SysFont(self.font,self.sfont)
        text = font.render(self.text, 1, (0,0,0))
        window.blit(text, (self.posX + (self.width/2 - text.get_width()/2), self.posY + (self.height/2 - text.get_height()/2)))
    def isOver(self, pos):
        if pos[0] > self.posX and pos[0] < self.posX + self.width:
            if pos[1] > self.posY and pos[1] < self.posY + self.height:
                return True
        return False
ancho = 900
alto = 480
listaEnemigos= []
def detenerTodo():
    for enemigo in listaEnemigos:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
        enemigo.conquista=True
def cargarEnemigos(x,y,d):
    enemigo = Invasor(x,y,d,"Imagenes/Marciano.png","Imagenes/Marciano1.png")
    listaEnemigos.append(enemigo)
def llenaEnemigos():
    cargarEnemigos(100,30,100)
    cargarEnemigos(350,30,50)
    cargarEnemigos(600,30,90)

    cargarEnemigos(100,130,50)
    cargarEnemigos(350,130,60)
    cargarEnemigos(600,130,90)

    cargarEnemigos(100,230,30)
    cargarEnemigos(350,230,100)
    cargarEnemigos(600,230,50)
def eliminaEnemigos():
    while(True):
        for enemigo in listaEnemigos:
            listaEnemigos.remove(enemigo)
        if len(listaEnemigos) == 0:
            return
        
def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Naves locochonas");
    ImagenFondo = pygame.image.load("Imagenes/fondo.png")
    pygame.mixer.music.load('Sonidos/Sonido.wav')
    pygame.mixer.music.play(-1)
    fuente = pygame.font.SysFont("comfortaa",30)
    texto = fuente.render("GAME",0,(0, 163, 92))
    texto1 = fuente.render("OVER",0,(0, 163, 92))
    textoWin = fuente.render("YOU",0,(0, 163, 92))
    textoWin1 = fuente.render("WIN",0,(0, 163, 92))
    jugador = Nave.naveEspacial(ancho,alto)
    llenaEnemigos()
    enJuego=True
    reloj = pygame.time.Clock()
    boton=Button(pygame.Color(29,216,191,0),ancho-100,alto-100,100,100,"Reiniciar","comfortaa",20)
    while True:
        reloj.tick(60)
        tiempo=pygame.time.get_ticks()/1000
        if jugador.rect.left > 840:
            jugador.rect.left = 0
        if jugador.rect.left < 0 :
            jugador.rect.left = 840
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                sys.exit()
            if(not(enJuego)):
                for disparo in jugador.listaDisparo:
                    jugador.listaDisparo.remove(disparo)
                if event.type == pygame.MOUSEBUTTONUP and boton.isOver(pygame.mouse.get_pos()):
                    enJuego=True
                    if(len(listaEnemigos) != 0):
                        hilo=threading.Thread(target=eliminaEnemigos)
                        hilo.start()
                    llenaEnemigos()
                    jugador.revive()
                    #eliminaEnemigos()
                    #llenaEnemigos()
            if(enJuego):
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y=jugador.rect.center
                    x-=5
                    y-=40
                    jugador.dispara(x,y)
                #Si se quiere hacer con teclas
                if(event.type == pygame.KEYDOWN):
                    if(event.key == K_LEFT):
                        jugador.rect.left -= jugador.velocidad
                        print(jugador.velocidad)
                        print(jugador.rect.left)
                    elif(event.key == K_RIGHT):
                            jugador.rect.right += jugador.velocidad
                    elif(event.key == K_SPACE):
                        x,y=jugador.rect.center
                        x-=5
                        y-=40
                        jugador.dispara(x,y)
        ventana.blit(ImagenFondo,(0,0))
        if(len(jugador.listaDisparo)>0):
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top <0:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemigo in listaEnemigos:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigos.remove(enemigo)
                            jugador.listaDisparo.remove(x)
        if(len(listaEnemigos)==0):
            ventana.blit(textoWin,(200,230))
            ventana.blit(textoWin1,(590,230))
        if(len(listaEnemigos)>0):
            for enemigo in listaEnemigos:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)
                if(enemigo.rect.colliderect(jugador.rect)):
                    #jugador.destruccion()
                    enJuego=False
                    detenerTodo()
                    print(enJuego)
                if(len(enemigo.listaDisparo)>0):
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego=False
                            detenerTodo()
                        if x.rect.top > 900:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)
        if len(listaEnemigos) == 0:
            enJuego=False
        if not enJuego and len(listaEnemigos) > 0:
            ventana.blit(texto,(180,230))
            ventana.blit(texto1,(590,230)) 
        jugador.dibujar(ventana)
        if(not(enJuego) or len(listaEnemigos) == 0):
            boton.draw(ventana)
            print enJuego
        pygame.display.update()
SpaceInvader()
