import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#//? Set des vertices, edges, surfaces, et uv du cube
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

uv = (
    (1, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
)


def init_GL():
    glClearColor(0.3, 0.2, 0.3, 1.0)  # Couleur de fond (background)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)  # Activer le test de profondeur (depth test)
    glShadeModel(GL_SMOOTH)  # Utilisation du modèle de rendu en douceur (Gouraud shading)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # Correction de la perspective

def init_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (1, 0.5, 0, 1))  # Position de la lumière (point light)

def setup_stencil_for_shadow():
    glClear(GL_STENCIL_BUFFER_BIT)
    glEnable(GL_STENCIL_TEST)

    glStencilFunc(GL_ALWAYS, 1, 0xFF)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)

def setup_stencil_for_ground():
    glStencilFunc(GL_EQUAL, 1, 0xFF)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)

def reset_stencil():
    glDisable(GL_STENCIL_TEST)

def draw_ground():
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.7, 0.7, 0.7, 1))  # Material gris
    glMaterialfv(GL_FRONT, GL_SHININESS, 1)
    glColorMaterial(GL_FRONT, GL_DIFFUSE)

    glDisable(GL_LIGHTING) #//!Test

    glBegin(GL_QUADS)
    glColor3fv((0.7, 0.7, 0.7))  
    glVertex3f(-2.0, -1.05, -2.0)
    glVertex3f(-2.0, -1.05, 2.0) 
    glVertex3f(2.0, -1.05, 2.0)  
    glVertex3f(2.0, -1.05, -2.0) 
    glEnd()

    glEnable(GL_LIGHTING) #//!Test

def draw_cube():
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0, 0.8, 0.8, 1))  # Material cyan
    glMaterialfv(GL_FRONT, GL_SHININESS, 5)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(uv[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    clock = pygame.time.Clock()
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0.0, -5)

    init_GL()
    init_light()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 0, 0.5, 0)  # Rotation du cube
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        setup_stencil_for_shadow()  #//? Config du Stencil pour le cube
        draw_cube() 
        reset_stencil()  #//? Reset du Stencil

        setup_stencil_for_ground()  #//? Config pour le sol
        draw_ground()

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(60)  # Limitation du framerate à 60 images par seconde

if __name__ == "__main__":
    main()
