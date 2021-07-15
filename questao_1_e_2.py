import cv2
import numpy as np

#chamada da imagem do desafio com uso do opencv
img = cv2.imread('meteor_challenge_01.png')

def acha_pontos(cor, img):
#duas opções de cores para encontrar estrelas e meteoros
    if cor == 'vermelho':
        rgb = [(0, 0, 255), (0, 0, 255)]
        objeto = 'meteoros'
    elif cor == 'branco':
        rgb = [(255, 255, 255), (255, 255, 255)]
        objeto = 'estrelas'
    
    #criando um blur/suavizando a imagem
    blur = cv2.medianBlur(img, 1)
 
    #criando uma copia da imagem
    output = img.copy()
        
    #mask = contorno pra encontrar os pontos
    mask = cv2.inRange(blur, rgb[0], rgb[1])
    
    #circulando
    circulos = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 1, param1=1, param2=1,
                                minRadius=1, maxRadius=1)
        
    #contagem dos círculos criados 
    count = 0
    if circulos is not None:
        circulos = np.round(circulos[0, :]).astype('int')    
    for (x, y, r) in circulos:
        cv2.circle(output, (x, y), r, (255, 0, 255), -1)
        count += 1
        
    resposta = 'No. de {} detectados(as): {}'.format(objeto, count)
    
    #caso queira visualizar os círculos criados:
    #cv2.imshow('Imagem marcada', output)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    return resposta
 
estrelas = acha_pontos('branco', img)
print(estrelas)
meteoros = acha_pontos('vermelho', img)
print(meteoros)
