import pygame, sys, random
import pygame.camera
from pygame.locals import *
from PIL import Image
import pytesseract as pt

"""S_L = 'eng'
D_L = 'en'"""
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30

BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

BGCOLOR = BLACK
BASICFONTSIZE = 20

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))

def terminate():
    pygame.quit()
    sys.exit()

def startScreen():
    pygame.display.set_caption('Linguista')
    DISPLAYSURF.fill(BLACK)
    TITLEFONT = pygame.font.Font('Fonts/calibri.ttf', 40)
    titleText = TITLEFONT.render('Linguista', True, WHITE)
    titleRect = titleText.get_rect()
    titleRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    DISPLAYSURF.blit(titleText, titleRect)
    pygame.display.flip()
    chooseScreen()
    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if (e.type == KEYDOWN and e.key == K_ESCAPE):
                # close the camera safely
                terminate()
                going = False
            elif (e.type == MOUSEBUTTONDOWN):
                obj = Capture()
                obj.main()
            elif (e.type == KEYDOWN and e.key == K_BACKSPACE):
                startScreen()



def chooseScreen():

    #DISPLAYSURF.fill(BGCOLOR)
    global S_L
    global D_L

    srcLang = BASICFONT.render('Source Language', True, WHITE)
    srcLangRect = srcLang.get_rect()
    srcLangRect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT / 30)

    s_eng = BASICFONT.render('English', True, WHITE)
    s_engRect = s_eng.get_rect()
    s_engRect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT / 12)

    s_ger = BASICFONT.render('German', True, WHITE)
    s_gerRect = s_ger.get_rect()
    s_gerRect.center = (WINDOWWIDTH / 4, 2 * WINDOWHEIGHT / 12)

    s_spa = BASICFONT.render('Spanish', True, WHITE)
    s_spaRect = s_spa.get_rect()
    s_spaRect.center = (WINDOWWIDTH / 4, 3 * WINDOWHEIGHT / 12)

    s_hin = BASICFONT.render('Hindi', True, WHITE)
    s_hinRect = s_hin.get_rect()
    s_hinRect.center = (WINDOWWIDTH / 4, 4 * WINDOWHEIGHT / 12)

    s_ben = BASICFONT.render('Bengali', True, WHITE)
    s_benRect = s_ben.get_rect()
    s_benRect.center = (WINDOWWIDTH / 4, 5 * WINDOWHEIGHT / 12)

    s_pun = BASICFONT.render('Punjabi', True, WHITE)
    s_punRect = s_pun.get_rect()
    s_punRect.center = (WINDOWWIDTH / 4, 6 * WINDOWHEIGHT / 12)

    s_fre = BASICFONT.render('French', True, WHITE)
    s_freRect = s_fre.get_rect()
    s_freRect.center = (WINDOWWIDTH / 4, 7 * WINDOWHEIGHT / 12)

    s_ita = BASICFONT.render('Italian', True, WHITE)
    s_itaRect = s_ita.get_rect()
    s_itaRect.center = (WINDOWWIDTH / 4, 8 * WINDOWHEIGHT / 12)

    dstLang = BASICFONT.render('Destination Language', True, WHITE)
    dstLangRect = dstLang.get_rect()
    dstLangRect.center = ((3*WINDOWWIDTH) / 4, WINDOWHEIGHT / 30)

    d_eng = BASICFONT.render('English', True, WHITE)
    d_engRect = d_eng.get_rect()
    d_engRect.center = ((3*WINDOWWIDTH) / 4, WINDOWHEIGHT / 12)

    d_ger = BASICFONT.render('German', True, WHITE)
    d_gerRect = d_ger.get_rect()
    d_gerRect.center = ((3*WINDOWWIDTH) / 4, 2 * WINDOWHEIGHT / 12)

    d_spa = BASICFONT.render('Spanish', True, WHITE)
    d_spaRect = d_spa.get_rect()
    d_spaRect.center = ((3*WINDOWWIDTH) / 4, 3 * WINDOWHEIGHT / 12)

    d_hin = BASICFONT.render('Hindi', True, WHITE)
    d_hinRect = d_hin.get_rect()
    d_hinRect.center = ((3*WINDOWWIDTH) / 4, 4 * WINDOWHEIGHT / 12)

    d_ben = BASICFONT.render('Bengali', True, WHITE)
    d_benRect = d_ben.get_rect()
    d_benRect.center = ((3*WINDOWWIDTH) / 4, 5 * WINDOWHEIGHT / 12)

    d_pun = BASICFONT.render('Punjabi', True, WHITE)
    d_punRect = d_pun.get_rect()
    d_punRect.center = ((3*WINDOWWIDTH) / 4, 6 * WINDOWHEIGHT / 12)

    d_fre = BASICFONT.render('French', True, WHITE)
    d_freRect = d_fre.get_rect()
    d_freRect.center = ((3*WINDOWWIDTH) / 4, 7 * WINDOWHEIGHT / 12)

    d_ita = BASICFONT.render('Italian', True, WHITE)
    d_itaRect = d_ita.get_rect()
    d_itaRect.center = ((3*WINDOWWIDTH) / 4, 8 * WINDOWHEIGHT / 12)

    DISPLAYSURF.blit(srcLang, srcLangRect)
    DISPLAYSURF.blit(s_hin, s_hinRect)
    DISPLAYSURF.blit(s_spa, s_spaRect)
    DISPLAYSURF.blit(s_ger, s_gerRect)
    DISPLAYSURF.blit(s_eng, s_engRect)
    DISPLAYSURF.blit(s_pun, s_punRect)
    DISPLAYSURF.blit(s_fre, s_freRect)
    DISPLAYSURF.blit(s_ita, s_itaRect)

    DISPLAYSURF.blit(dstLang, dstLangRect)
    DISPLAYSURF.blit(d_hin, d_hinRect)
    DISPLAYSURF.blit(d_spa, d_spaRect)
    DISPLAYSURF.blit(d_ger, d_gerRect)
    DISPLAYSURF.blit(d_eng, d_engRect)
    DISPLAYSURF.blit(d_pun, d_punRect)
    DISPLAYSURF.blit(d_fre, d_freRect)
    DISPLAYSURF.blit(d_ita, d_itaRect)
    
    pygame.display.update()


    going = True
    count_s = 0
    count_d = 0

    while going:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                if s_hinRect.collidepoint(mouseX, mouseY):
                    S_L = 'hin'
                    count_s = count_s + 1
                elif s_gerRect.collidepoint(mouseX, mouseY):
                    S_L = 'deu'
                    count_s = count_s + 1
                elif s_engRect.collidepoint(mouseX, mouseY):
                    S_L = 'eng'
                    count_s = count_s + 1
                elif s_spaRect.collidepoint(mouseX, mouseY):
                    S_L = 'spa'
                    count_s = count_s + 1
                elif s_punRect.collidepoint(mouseX, mouseY):
                    S_L = 'pan'
                    count_s = count_s + 1
                elif s_freRect.collidepoint(mouseX, mouseY):
                    S_L = 'fra'
                    count_s = count_s + 1
                elif s_itaRect.collidepoint(mouseX, mouseY):
                    S_L = 'ita'
                    count_s = count_s + 1
                elif d_hinRect.collidepoint(mouseX, mouseY):
                    D_L = 'hi'
                    count_d = count_d + 1
                elif d_engRect.collidepoint(mouseX, mouseY):
                    D_L = 'en'
                    count_d = count_d + 1
                elif d_gerRect.collidepoint(mouseX, mouseY):
                    D_L = 'de'
                    count_d = count_d + 1
                elif d_spaRect.collidepoint(mouseX, mouseY):
                    D_L = 'es'
                    count_d = count_d + 1
                elif d_punRect.collidepoint(mouseX, mouseY):
                    D_L = 'pa'
                    count_d = count_d + 1
                elif d_freRect.collidepoint(mouseX, mouseY):
                    D_L = 'fr'
                    count_d = count_d + 1
                elif d_itaRect.collidepoint(mouseX, mouseY):
                    D_L = 'it'
                    count_d = count_d + 1
                if (count_s == 1 and count_d == 1):
                    going = False
                    break




class Capture(object):
    def __init__(self):
        self.size = (640,480)
        #self.size2 = (640, 380)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)

        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
        self.img = pygame.image.load('Images/black.jpg')
        self.display.blit(self.img,(0,360))
        pygame.display.update()

    def black_region(self, blck):
        self.display.blit(blck,(0,360))
        pygame.display.update()

    def get_and_flip(self, blck):
        # if you don't want to tie the framerate to the camera, you can check
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)
     
        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0,0))
        self.black_region(blck)


    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT:
                    # close the camera safely
                    self.cam.stop()
                    going = False
                elif (e.type == KEYDOWN and e.key == K_SPACE):
                    ini_image = self.cam.get_image()
                    self.filename = '2.jpg'
                    pygame.image.save(ini_image, self.filename)
                    self.display.blit(ini_image, (0,0))
                    self.get_text()
                elif (e.type == KEYDOWN and e.key == K_ESCAPE):
                    self.cam.stop()
                    startScreen()

            self.get_and_flip(self.img)

    def get_text(self):
        fin_file = pt.func(self.filename, S_L, D_L)
        fin_img = pygame.image.load(fin_file)
        going = True
        while going:
            self.black_region(fin_img)
            events = pygame.event.get()
            for e in events:
                if (e.type == KEYDOWN and e.key == K_BACKSPACE):
                    going = False
                    self.main()
                elif (e.type == KEYDOWN and e.key == K_ESCAPE):
                    self.cam.stop()
                    startScreen()
                elif e.type == QUIT:
                    # close the camera safely
                    self.cam.stop()
                    going = False
"""self.display.blit(fin_img,(0,360))
        pygame.display.update()"""




def main():
    global DISPLAYSURF, BASICFONT, FPSCLOCK, S_L, D_L
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('Fonts/calibri.ttf', BASICFONTSIZE)
    S_L = 'eng'
    D_L = 'en'
    startScreen()


if __name__ == '__main__':
	main()