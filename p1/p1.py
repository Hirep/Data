""" Practical Assignment #1
    Student: Dima Samoilenko
    Variant: 24
    Surface: Surface of Revolution “Wellenkugel”
"""

import pygame
from pygame.locals import *

import numpy as np
import math

from OpenGL.GL import *
from OpenGL.GLU import *

def surface_x(u,v):
    return u*math.cos(math.cos(u))*math.cos(v)

def surface_y(u,v):
    return u*math.cos(math.cos(u))*math.sin(v)
    
def surface_z(u,v):
    return u*math.sin(math.cos(u))

def set_material():
    glEnable(GL_DEPTH_TEST)
    qaBlack = (0.0, 0.0, 0.0, 1.0)
    qaGreen = (0.0, 1.0, 0.0, 1.0)
    qaWhite = (1.0, 1.0, 1.0, 1.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, qaGreen)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, qaGreen)
    glMaterialfv(GL_FRONT, GL_SPECULAR, qaWhite)
    glMaterialf(GL_FRONT, GL_SHININESS, 60.0)

def surface_draw():
    set_material()
    glNormal3f(0.0, 0.0, 1.0)
    d = 0.3
    for u in np.arange(0, 15, d):
        for v in np.arange(0, 1.5*math.pi, d):
            glBegin(GL_QUADS)
            glVertex3fv((surface_x(u,v), surface_y(u,v), surface_z(u,v)))
            glVertex3fv((surface_x(u+d,v), surface_y(u+d,v), surface_z(u+d,v)))
            glVertex3fv((surface_x(u+d,v+d), surface_y(u+d,v+d), surface_z(u+d,v+d)))
            glVertex3fv((surface_x(u,v+d), surface_y(u,v+d), surface_z(u,v+d)))
            glEnd()

def light_init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -3.0, 3.0)

	# Lighting set up
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

	# Set lighting intensity and color
    qaAmbientLight = (0.2, 0.2, 0.2, 1.0)
    qaDiffuseLight = (0.8, 0.8, 0.8, 1.0)
    qaSpecularLight = (1.0, 1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, qaAmbientLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, qaDiffuseLight)
    glLightfv(GL_LIGHT0, GL_SPECULAR, qaSpecularLight)

	# Set the light position
    qaLightPosition = (0, 1, -.5, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, qaLightPosition)

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    light_init()

    gluPerspective(45, (display[0]/display[1]), 1, 70.0)

    glTranslatef(.0, .0, -50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        x_change = 0
        y_change = 0
        z_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                x_change += 5
            elif event.key == pygame.K_2:
                y_change += 5
            elif event.key == pygame.K_3:
                z_change += 5
            elif event.key == pygame.K_q:
                x_change -= 5
            elif event.key == pygame.K_w:
                y_change -= 5
            elif event.key == pygame.K_e:
                z_change -= 5   
        
        glRotatef(x_change, 1, 0, 0)
        glRotatef(y_change, 0, 1, 0)
        glRotatef(z_change, 0, 0, 1)
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        surface_draw()

        pygame.display.flip()
        pygame.time.wait(10)


main()

