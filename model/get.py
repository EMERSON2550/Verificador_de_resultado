
import shutil

def salvar_corretos(img, json):
    destino = 'verificador_de_resultado_ocr/salvar_corretas'
    shutil.copy2(img, destino)
    shutil.copy2(json, destino)
    print(json)

def salvar_incorretas(img, json):
    destino = 'verificador_de_resultado_ocr/salvar_incorretas'
    shutil.copy2(img, destino)
    shutil.copy2(json, destino)

def salvar_tag_danificadas(img, json):
    destino = 'verificador_de_resultado_ocr/salvar_tag_danificadas'
    shutil.copy2(img, destino)
    shutil.copy2(json, destino)
