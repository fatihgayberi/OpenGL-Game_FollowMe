from OpenGL.GL import *
from PIL import Image
''' Verilen str ile texture'lama yapmak için gerekli initilaziton işlemlerini yapan fonksiyon '''
def LoadTextures(str):
    # global texture
    glActiveTexture(GL_TEXTURE0)
    image = Image.open(str)
    image = image.convert('RGBA')
    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBA")

    glShadeModel(GL_SMOOTH)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glEnable(GL_TEXTURE_2D)

''' Map paramtrelerine göre yeryüzü/gökyüzü/yan alanların texture'landığı fonksiyon '''
def mapTexture(mapX,mapY,mapZ):
    glPushMatrix()
    glActiveTexture(GL_TEXTURE0)
    LoadTextures("assets/plane.png")
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0), glVertex3f(-mapX, 0.0, -mapZ)
    glTexCoord2f(0.0, 1.0), glVertex3f(-mapX, 0.0, mapZ)
    glTexCoord2f(1.0, 1.0), glVertex3f(mapX, 0.0, mapZ)
    glTexCoord2f(1.0, 0.0), glVertex3f(mapX, 0.0, -mapZ)

    glEnd()
    glDisable(GL_TEXTURE_3D)
    LoadTextures("assets/wall-2.png")

    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0),glVertex3f(-mapX, 0.0, -mapZ)
    glTexCoord2f(0.0, 0.0),glVertex3f(-mapX, mapY, -mapZ)
    glTexCoord2f(1.0, 0.0),glVertex3f(mapX, mapY, -mapZ)
    glTexCoord2f(1.0, 1.0),glVertex3f(mapX, 0.0, -mapZ)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0),glVertex3f(-mapX, 0.0, mapZ)
    glTexCoord2f(0.0, 0.0),glVertex3f(-mapX, mapY, mapZ)
    glTexCoord2f(1.0, 0.0),glVertex3f(mapX, mapY, mapZ)
    glTexCoord2f(1.0, 1.0),glVertex3f(mapX, 0.0, mapZ)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex3f(mapX, 0.0, -mapZ)
    glTexCoord2f(0.0, 0.0), glVertex3f(mapX, mapY, -mapZ)
    glTexCoord2f(1.0, 0.0), glVertex3f(mapX, mapY, mapZ)
    glTexCoord2f(1.0, 1.0), glVertex3f(mapX, 0.0, mapZ)
    glEnd()
    LoadTextures("assets/wall-1.png")
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex3f(-mapX, 0.0, mapZ)
    glTexCoord2f(0.0, 0.0), glVertex3f(-mapX, mapY, mapZ)
    glTexCoord2f(1.0, 0.0), glVertex3f(-mapX, mapY, -mapZ)
    glTexCoord2f(1.0, 1.0), glVertex3f(-mapX, 0.0, -mapZ)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    LoadTextures("assets/sky.png")
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0), glVertex3f(-mapX, mapY, -mapZ)
    glTexCoord2f(0.0, 1.0), glVertex3f(-mapX, mapY, mapZ)
    glTexCoord2f(1.0, 1.0), glVertex3f(mapX, mapY, mapZ)
    glTexCoord2f(1.0, 0.0), glVertex3f(mapX, mapY, -mapZ)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()