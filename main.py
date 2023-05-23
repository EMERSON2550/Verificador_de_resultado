
import cv2
from glob import glob
import model.get as mg

caminho = 'verificador_de_resultado_ocr/img_para_analisar'


for path_img in glob(caminho + "/*.jpg"):
    img = cv2.imread(path_img)
    img = cv2.resize(img,None,None, 0.2,0.2)
    nome_json = path_img[:-3] + 'json'
    cv2.imshow('janela', img)

    with open(nome_json, 'r') as arquivo:
        dados = arquivo.read()
    print(dados)
    cv2.waitKey(300)
    menu = int(input('digite a opçao:'))
    if menu == 1:
        mg.salvar_corretos(path_img, nome_json)
    elif menu == 2:
        mg.salvar_incorretas(path_img, nome_json)
    elif menu == 3:
        mg.salvar_tag_danificadas(path_img, nome_json)
    else:
        print('opçao invalida')
        
 