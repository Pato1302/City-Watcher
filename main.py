import pygame
from pygame import *
import sys, random, time, shelve  # Libraries



# For making buttons
def pintar_boton(screen, boton, palabra):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (237, 128, 19), boton, 0)
    else:
        draw.rect(screen, (70, 189, 34), boton, 0)
    texto = myFont.render(palabra, True, (255, 255, 255))
    screen.blit(texto,
                (boton.x + (boton.width - texto.get_width()) / 2, boton.y +
                 (boton.height - texto.get_height()) / 2))



def mainMenu():
    cielo = image.load("Main/City.png")
    imgDetective = image.load("Main/Detective.png")
    imgGeneral = image.load("Main/General.png")

    Sorprise=mixer.Sound("Main/Easter.wav")

    cielo = transform.scale(cielo, (800, 600))
    imgDetective = transform.scale(imgDetective, (250, 250))
    imgGeneral = transform.scale(imgGeneral, (650, 370))

    Titulo = font.SysFont("Fonts/AHBold.ttf", 80)

    Detective = Rect(185, 450, 150, 50)
    General = Rect(520, 450, 150, 50)

    xCielo, xCielo2 = 0, -800

    while True:
      screen.fill((255, 255, 255))

      for e in event.get():  # Detection of discrete events
        if e.type == QUIT:
          sys.exit()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
          if Detective.collidepoint(mouse.get_pos()):
              return "ElecciónDetective"  #"Detective"
          if General.collidepoint(mouse.get_pos()):
              return "General"
      if key.get_pressed()[pygame.K_p and pygame.K_r]:
        Sorprise.play()

      texto = Titulo.render('City Watcher', True, (255, 255, 255))

      screen.blit(cielo, (xCielo, 0))
      screen.blit(cielo, (xCielo2, 0))
      screen.blit(texto, (200, 10))
      screen.blit(imgDetective, (150, 150))
      screen.blit(imgGeneral, (250, 88))

      # Buttons
      pintar_boton(screen, Detective, "Detective")
      pintar_boton(screen, General, "General")

      xCielo += 1
      xCielo2 += 1

      if xCielo == 800:
          xCielo = -800
      if xCielo2 == 800:
          xCielo2 = -800

      display.flip()



def detectiveScreen():
  imgSus = image.load("JuegoDetective/Sus.jpg")
  Pared = image.load("JuegoDetective/Pared.jpg")
  description = image.load("JuegoDetective/Descripción.png")
  carta = image.load("SUS" + str(nivelDetective) + "/Carta.png")
  audio = image.load("JuegoDetective/Audio.png")
  confirm = image.load("JuegoDetective/Confirmar.png")

  Selec1 = image.load("SUS/Sus1.png")
  Selec2 = image.load("SUS/Sus2.png")
  Selec3 = image.load("SUS/Sus3.png")
  Selec4 = image.load("SUS/Sus4.png")
  Selec5 = image.load("SUS/Sus5.png")
  Selec6 = image.load("SUS/Sus6.png")

  Selec1 = transform.scale(Selec1, (700, 250))
  Selec2 = transform.scale(Selec2, (700, 250))
  Selec3 = transform.scale(Selec3, (700, 250))
  Selec4 = transform.scale(Selec4, (700, 250))
  Selec5 = transform.scale(Selec5, (700, 250))
  Selec6 = transform.scale(Selec6, (700, 250))

  imgSus = transform.scale(imgSus, (700, 250))
  Pared = transform.scale(Pared, (800, 600))
  description = transform.scale(description, (80, 80))
  carta = transform.scale(carta, (800, 500))
  audio = transform.scale(audio, (50, 50))
  confirm = transform.scale(confirm, (130, 50))

  bruno = mixer.Sound("SUS" + str(nivelDetective) + "/Bruno.wav")
  kevin = mixer.Sound("SUS" + str(nivelDetective) + "/Kevin.wav")
  javi = mixer.Sound("SUS" + str(nivelDetective) + "/Javi.wav")
  diego = mixer.Sound("SUS" + str(nivelDetective) + "/Diego.wav")
  pato = mixer.Sound("SUS" + str(nivelDetective) + "/Pato.wav")
  tony = mixer.Sound("SUS" + str(nivelDetective) + "/Tony.wav")

  mostrarCarta = 0
  reproducirAudio = 0

  sospechoso = 0

  tipografia = font.Font("Fonts/Nombres.ttf", 15)

  while True:
    screen.fill((255, 255, 255))

    for e in event.get():  # Detection of discrete events
      if e.type == QUIT:
        sys.exit()
      if e.type == MOUSEBUTTONDOWN and e.button == 1:
        if despliegaCarta.collidepoint(mouse.get_pos()):
          mostrarCarta = not mostrarCarta
        if despliegaAudioBruno.collidepoint(mouse.get_pos()):
          bruno.play()
        if despliegaAudioPato.collidepoint(mouse.get_pos()):
          pato.play()
        if despliegaAudioJavi.collidepoint(mouse.get_pos()):
          javi.play()
        if despliegaAudioDiego.collidepoint(mouse.get_pos()):
          diego.play()
        if despliegaAudioKevin.collidepoint(mouse.get_pos()):
          kevin.play()
        if despliegaAudioTony.collidepoint(mouse.get_pos()):
          tony.play()
        if seleccionBruno.collidepoint(mouse.get_pos()):
          sospechoso = 1
        if seleccionPato.collidepoint(mouse.get_pos()):
          sospechoso = 2
        if seleccionJavi.collidepoint(mouse.get_pos()):
          sospechoso = 3
        if seleccionDiego.collidepoint(mouse.get_pos()):
          sospechoso = 4
        if seleccionKevin.collidepoint(mouse.get_pos()):
          sospechoso = 5
        if seleccionTony.collidepoint(mouse.get_pos()):
          sospechoso = 6
        if confirmButton.collidepoint(mouse.get_pos()):
          if sospechoso == realSus: return "Ganador"
          else: return "Fail"

    screen.blit(Pared, (0, 0))
    screen.blit(audio, (145, 375))
    screen.blit(audio, (240, 375))
    screen.blit(audio, (340, 375))
    screen.blit(audio, (440, 375))
    screen.blit(audio, (525, 375))
    screen.blit(audio, (625, 375))
    screen.blit(description, (700, 500))
    screen.blit(confirm, (360, 500))

    if sospechoso == 1:
      screen.blit(Selec1, (50, 100))
    elif sospechoso == 2:
      screen.blit(Selec2, (50, 100))
    elif sospechoso == 3:
      screen.blit(Selec3, (50, 100))
    elif sospechoso == 4:
      screen.blit(Selec4, (50, 100))
    elif sospechoso == 5:
      screen.blit(Selec5, (50, 100))
    elif sospechoso == 6:
      screen.blit(Selec6, (50, 100))
    else:
      screen.blit(imgSus, (50, 100))

    if mostrarCarta == True:
      screen.blit(carta, (0, 0))
    else:
      despliegaAudioBruno = draw.rect(screen, (0, 0, 0),(143, 372, 56, 56), 4)
      despliegaAudioPato = draw.rect(screen, (0, 0, 0),(238, 372, 56, 56), 4)
      despliegaAudioJavi = draw.rect(screen, (0, 0, 0),(340, 372, 56, 56), 4)
      despliegaAudioDiego = draw.rect(screen, (0, 0, 0),(440, 372, 56, 56), 4)
      despliegaAudioKevin = draw.rect(screen, (0, 0, 0),(525, 372, 56, 56), 4)
      despliegaAudioTony = draw.rect(screen, (0, 0, 0),(625, 372, 56, 56), 4)
      seleccionBruno = draw.rect(screen, (255, 255, 255),(141, 338, 60, 30), 4)
      seleccionPato = draw.rect(screen, (255, 255, 255),(236, 338, 60, 30), 4)
      seleccionJavi = draw.rect(screen, (255, 255, 255),(338, 338, 60, 30), 4)
      seleccionDiego = draw.rect(screen, (255, 255, 255),(436, 338, 60, 30), 4)
      seleccionKevin = draw.rect(screen, (255, 255, 255),(520, 338, 60, 30), 4)
      seleccionTony = draw.rect(screen, (255, 255, 255),(620, 338, 60, 30), 4)
      texto = tipografia.render('Bruno', True, (255, 255, 255))
      screen.blit(texto, (150, 347))
      texto = tipografia.render('Pato', True, (255, 255, 255))
      screen.blit(texto, (250, 347))
      texto = tipografia.render('Javi', True, (255, 255, 255))
      screen.blit(texto, (352, 347))
      texto = tipografia.render('Diego', True, (255, 255, 255))
      screen.blit(texto, (447, 347))
      texto = tipografia.render('Kevin', True, (255, 255, 255))
      screen.blit(texto, (531, 347))
      texto = tipografia.render('Tony', True, (255, 255, 255))
      screen.blit(texto, (634, 347))

    despliegaCarta = draw.rect(screen, (0, 0, 0), (700, 500, 80, 80), 4)

    confirmButton = draw.rect(screen, (0, 0, 0), (360, 500, 130, 50), 4)

    display.flip()



def Ganador():
  felicidades = font.Font("Fonts/Nombres.ttf", 60)
  mensaje = font.Font("Fonts/Nombres.ttf", 30)
  
  win = image.load("PantallasFinales/Win.png")
  win1 = image.load("Carcel/CarcelPato.png")
  win2 = image.load("Carcel/CarcelTony.png")
  win3 = image.load("Carcel/CarcelKevin.png")
  fondoGan=image.load("PantallasFinales/GanasteFondo.jpg")
  placa = image.load("PantallasFinales/Placa.png")
  
  SonWin=mixer.Sound("PantallasFinales/SoundWin.wav")
  SonWin.set_volume(SonWin.get_volume() - .50)

  win = transform.scale(win, (250,235))
  placa = transform.scale(placa, (250,235))
  fondoGan=transform.scale(fondoGan,(800,600))
  win1 = transform.scale(win1, (290,275))
  win2 = transform.scale(win2, (290,275))
  win3 = transform.scale(win3, (290,275))

  SonWin.play()

  WinIniTime = time.time()
  WinActTime = time.time()
  WinTime = time.time()
  limite = 10

  while True:
    screen.fill((255, 255, 255))

    for e in event.get():  # Detection of discrete events
        if e.type == QUIT:
            sys.exit()
    screen.blit(fondoGan,(0,0))
    screen.blit(placa, (100,330))
    screen.blit(win, (450,330))

    if nivelDetective == 1:
      screen.blit(win1, (450,45))
    elif nivelDetective == 2:
      screen.blit(win2, (450,45))
    else:
      screen.blit(win3, (450,45))

    texto = felicidades.render('Felicidades', True, (0, 0, 0))
    screen.blit(texto, (65, 170))
    texto = mensaje.render('Atrapaste al culpable', True, (0, 0, 0))
    screen.blit(texto, (55, 265))
    
    WinActTime = time.time()
    WinTime = WinActTime - WinIniTime
    WinTime = limite - round(WinTime) 
    if WinTime <= 0:
      time.sleep(1)
      SonWin.stop()
      return "MainMenu"

    display.flip()



def Fail():
  fail = font.Font("Fonts/Nombres.ttf", 60)
  mensaje = font.Font("Fonts/Nombres.ttf", 30)
  SonFail=mixer.Sound("JuegoDetective/MissionFailed.wav")
  gameOver = image.load("PantallasFinales/GameOver.jpg")
  escape = image.load("PantallasFinales/Escape.png")

  gameOver = transform.scale(gameOver, (270,270))
  escape = transform.scale(escape, (300,470))

  FIniTime = time.time()
  FActTime = time.time()
  FTime = time.time()
  limite = 60

  SonFail.set_volume(SonFail.get_volume() - .90)
  SonFail.play()
  while True:
    screen.fill((0,0,0))

    for e in event.get():  # Detection of discrete events
      if e.type == QUIT:
        sys.exit()
    
    screen.blit(gameOver, (430,58))
    screen.blit(escape, (50,55))

    texto = mensaje.render('No atrapaste', True, (255,255,255))
    screen.blit(texto, (475, 365))
    texto = mensaje.render('al culpable', True, (255,255,255))
    screen.blit(texto, (483, 405))

    FActTime = time.time()
    FTime = FActTime - FIniTime
    FTime = limite - round(FTime)  #,1)
    if FTime <= 0:
      time.sleep(1)
      SonFail.stop()
      return "MainMenu"

    display.flip()



def eleccionDetective():
  Decapitado = image.load("JuegoDetective/Decapitado.jpg")
  mariaJuana = image.load("JuegoDetective/Maria Juana.jpg")
  PC = image.load("JuegoDetective/PC.jpg")
  Mesa = image.load("JuegoDetective/MesaMadera.jpg")
  Start = image.load("JuegoDetective/Start.png")

  Decapitado = transform.scale(Decapitado, (230, 170))
  mariaJuana = transform.scale(mariaJuana, (230, 170))
  PC = transform.scale(PC, (230, 170))
  Mesa = transform.scale(Mesa, (800, 600))
  Start = transform.scale(Start, (230, 170))

  play1 = Rect(683, 506, 90, 36)
  play2 = Rect(683, 506, 90, 36)
  play3 = Rect(683, 506, 90, 36)

  global nivelDetective
  global realSus

  tipografia = font.Font("Fonts/Nombres.ttf", 30)

  while True:
    screen.fill((255, 255, 255))

    for e in event.get():  # Detection of discrete events
      if e.type == QUIT:
        sys.exit()
      if e.type == MOUSEBUTTONDOWN and e.button == 1:
        if play1.collidepoint(mouse.get_pos()):
          nivelDetective = 1
          realSus = 2
          return "Detective"
        if play2.collidepoint(mouse.get_pos()):
          nivelDetective = 2
          realSus = 6
          return "Detective"
        if play3.collidepoint(mouse.get_pos()):
          nivelDetective = 3
          realSus = 5
          return "Detective"

    play1 = draw.rect(screen, (0, 0, 0), (550, 13, 230, 170), 4)
    play2 = draw.rect(screen, (0, 0, 0), (550, 213, 230, 170), 4)
    play3 = draw.rect(screen, (0, 0, 0), (550, 413, 230, 170), 4)

    screen.blit(Mesa, (0, 0))
    screen.blit(Decapitado, (25, 13))
    screen.blit(mariaJuana, (25, 213))
    screen.blit(PC, (25, 413))
    screen.blit(Start, (550, 13))
    screen.blit(Start, (550, 213))
    screen.blit(Start, (550, 413))

    texto = tipografia.render('Elige tu caso', True, (0, 0, 0))
    screen.blit(texto, (300, 5))

    texto = myFont.render('Estatua decapitada', True, (0, 0, 0))
    screen.blit(texto, (300, 100))
    texto = myFont.render('Venta de marihuana', True, (0, 0, 0))
    screen.blit(texto, (300, 300))
    texto = myFont.render('Robo de computadoras', True, (0, 0, 0))
    screen.blit(texto, (300, 500))

    display.flip()



def generalScreen():
  radar = image.load("JuegoGeneral/Mapa.jpg")
  attackImg = image.load("JuegoGeneral/Attack.png")
  alert = image.load("JuegoGeneral/Alerta.png")
  kills = image.load("JuegoGeneral/Kills.png")
  
  radar = transform.scale(radar, (800, 500))
  attackImg = transform.scale(attackImg, (90, 36))
  alert = transform.scale(alert, (50, 50))
  kills = transform.scale(kills, (50, 50))

  textoX = ""
  textoY = ""

  ingresaX = 0
  ingresaY = 0
  global NewHighScore
  NewHighScore = False
  global countKills
  countKills = 0
  limite = 60

  generalIniTime = time.time()
  generalActTime = time.time()
  generalTime = time.time()

  posX = Rect(483, 506, 70, 36)
  posY = Rect(588, 506, 70, 36)
  attack = Rect(683, 506, 90, 36)

  alertPosX = random.randint(1, 15) * 50
  alertPosY = random.randint(2, 9) * 50

  alertX = alertPosX - 50
  alertY = 450 - alertPosY

  colorX = (0, 0, 0)
  colorY = (0, 0, 0)

  misionImposible = mixer.Sound("JuegoGeneral/MisiónImposible.wav")
  misionImposible.set_volume(misionImposible.get_volume() - .97)
  misionImposible.play()

  while True:
    screen.fill((255, 255, 255))

    for e in event.get():  # Detection of discrete events
      if e.type == QUIT:
        sys.exit()
      if e.type == MOUSEBUTTONDOWN and e.button == 1:
        if attack.collidepoint(mouse.get_pos()):
          if textoX == str(alertX) and textoY == str(alertY):
            textoX = ""
            textoY = ""
            alertPosX = random.randint(1, 15) * 50
            alertPosY = random.randint(2, 9) * 50
            alertX = alertPosX - 50
            alertY = 450 - alertPosY
            countKills += 1
            colorX = (0, 0, 0)
            colorY = (0, 0, 0)
          else:
            if textoX != str(alertX) and textoY != str(alertY):
                colorX = (255, 0, 0)
                colorY = (255, 0, 0)
            elif textoX != str(alertX):
                colorX = (255, 0, 0)
                colorY = (0, 255, 0)
            else:  # textoY != str(alertY)
                colorX = (0, 255, 0)
                colorY = (255, 0, 0)
        if posX.collidepoint(mouse.get_pos()):
          ingresaX = True
        else:
          ingresaX = False
        if posY.collidepoint(mouse.get_pos()):
          ingresaY = True
        else:
          ingresaY = False
      if e.type == KEYDOWN:
        if ingresaX:
          if e.key == K_RETURN:
            pass
          elif e.key == K_BACKSPACE:
            textoX = textoX[:-1]
          else:
            textoX += e.unicode
        if ingresaY:
          if e.key == K_RETURN:
            pass
          elif e.key == K_BACKSPACE:
            textoY = textoY[:-1]
          else:
            textoY += e.unicode
    
    screen.blit(radar, (0, 0))
    screen.blit(attackImg, (683, 530))

    calibriFont = font.SysFont("Fonts/AHBold.ttf", 50)

    draw.line(screen, (231, 123, 123), (0, 450), (800, 450), 6)
    draw.line(screen, (231, 123, 123), (50, 0), (50, 500), 6)

    for index in range(50, 500, 50):
      draw.line(screen, (231, 123, 123), (0, index), (800, index), 1)
      texto = myFont.render(str(450 - index), True, (255, 255, 255))
      screen.blit(texto, (5, index - 8))

    for idx in range(50, 800, 50):
      draw.line(screen, (231, 123, 123), (idx, 0), (idx, 500), 1)
      texto = myFont.render(str(idx - 50), True, (255, 255, 255))
      screen.blit(texto, (idx - 8, 465))

    screen.blit(alert, (alertPosX - 25, alertPosY - 30))

    posX = draw.rect(screen, colorX, (483, 530, 70, 36), 4)
    posY = draw.rect(screen, colorY, (588, 530, 70, 36), 4)
    attack = draw.rect(screen, (0, 0, 0), (683, 530, 90, 36), 4)

    texto = myFont.render('¡¡¡Ingresa la coordenada de ataque!!!', True,(0, 0, 0))
    screen.blit(texto, (50, 540))
    texto = myFont.render('X:', True, (0, 0, 0))
    screen.blit(texto, (459, 540))
    texto = myFont.render(textoX, True, (0, 0, 0))
    screen.blit(texto, (495, 540))
    texto = myFont.render('Y:', True, (0, 0, 0))
    screen.blit(texto, (566, 540))
    texto = myFont.render(textoY, True, (0, 0, 0))
    screen.blit(texto, (600, 540))

    killsRect = draw.rect(screen, (255, 255, 255), (60, 10, 90, 50), 0)
    screen.blit(kills, (35, 10))

    texto = myFont.render(str(countKills), True, (0, 0, 0))
    screen.blit(texto, (87, 27))

    generalActTime = time.time()
    generalTime = generalActTime - generalIniTime
    generalTime = limite - round(generalTime)  #,1)
    textoTiempoGeneral = myFont.render(str(generalTime), True,(255, 255, 255))
    screen.blit(textoTiempoGeneral, (600, 27))

    if generalTime <= 0:
      shelveFile = shelve.open('scores')

      if "puntaje" in shelveFile.keys():
        scores = shelveFile['puntaje']
        if scores < countKills:
          shelveFile['puntaje'] = countKills
          NewHighScore = True
          print("Nuevo record")
      else:
        shelveFile['puntaje'] = countKills

      print(shelveFile['puntaje'])
      shelveFile.close()
    
      time.sleep(1)
      misionImposible.stop()
      HighScore = open("HighScore.txt","w")
      HighScore.write(str(countKills)+"\n")
      
      HighScore.close
      return "Score"

    display.flip()

def score_general():
  global NewHighScore
  global countKills
  
  myFont = font.SysFont("Fonts/AHBold.ttf", 200)
  myFont2 = font.SysFont("Fonts/AHBold.ttf", 80)

  gOv = image.load("PantallasFinales/gmov.jpeg")
  gOv = transform.scale(gOv, (800, 600))

  score=image.load("PantallasFinales/Score.jpg")
  score=transform.scale(score, (270, 200))

  Hscore=image.load("PantallasFinales/HighScore.jpg")
  Hscore=transform.scale(Hscore, (270, 200))

  GameOver=mixer.Sound("PantallasFinales/GameOver.wav")
  GameOver.set_volume(GameOver.get_volume() - .97)

  NewHighScoreSo=mixer.Sound("PantallasFinales/NewHigh.wav")

  SIniTime = time.time()
  SActTime = time.time()
  STime = time.time()
  limite = 10

  while True: 
    screen.fill((0,0,0))
    
    for e in event.get():  # Detection of discrete events
      if e.type == QUIT:
        sys.exit()
    
    SActTime = time.time()
    STime = SActTime - SIniTime
    STime = limite - round(STime)  #,1)

    if STime >= 8:
      screen.blit(gOv, (0,0))
      GameOver.play()
    else:
      screen.blit(score, (450,80))
      screen.blit(Hscore, (50,80))

      if NewHighScore==True:
        NScore = myFont2.render("¡¡Felicidades!!", True,(255, 255, 255))
        screen.blit(NScore, (200, 440))
        NScore2 = myFont2.render("Nuevo record", True,(255, 255, 255))
        screen.blit(NScore2, (220, 500))
        text = myFont.render(str(countKills), True,(255, 255, 255))
        screen.blit(text,(600,300))
        if STime==7:
          NewHighScoreSo.play(loops=0)
      else:
        text = myFont.render(str(countKills), True,(255, 255, 255))
        screen.blit(text,(600,300))
      shelveFile = shelve.open('scores')

      texto = myFont.render(str(shelveFile['puntaje']), True,(255,255,255))
      screen.blit(texto, (170, 300))

      if STime <= 0:
        time.sleep(1)
        return "MainMenu"
      
    display.flip()

init()
mixer.init()

screen = display.set_mode((800, 600))

pantalla = "MainMenu"
NewHighScore = False

myFont = font.SysFont("Fonts/AHBold.ttf", 30)

nivelDetective = 1

while True:
  screen.fill((255, 255, 255))

  for e in event.get():  # Detection of discrete events
    if e.type == QUIT:
      sys.exit()

  if pantalla == "MainMenu":
    pantalla = mainMenu()
  elif pantalla == "Detective":
    pantalla = detectiveScreen()
  elif pantalla == "General":
    pantalla = generalScreen()
  elif pantalla == "Ganador":
    pantalla = Ganador()
  elif pantalla == "Fail":
    pantalla = Fail()
  elif pantalla=="Score":
    pantalla =score_general()
  else: # pantalla == "ElecciónDetective":
    pantalla = eleccionDetective()

  display.flip()