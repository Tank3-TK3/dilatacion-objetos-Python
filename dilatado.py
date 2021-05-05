# >>>>>>>>>>>>>>>>>>>>>>>>>>>Hecho por Roberto (Tank3) Cruz Lozano<<<<<<<<<<<<<<<<<<<<<<<<<<<
#############################################################################################
#                                          MODULOS
import cv2
import numpy as np
import matplotlib.pyplot as plt
#############################################################################################
#                                         FUNCIONES
def umbralizacion( img ):
    imgUmbralizada = np.zeros( img.shape , dtype=np.uint8 )
    for i in range( 0 , img.shape[0] ):
        for j in range( 0 , img.shape[1] ):
            if img[i][j] >= 128:
                imgUmbralizada[i][j] = 255
            else:
                imgUmbralizada[i][j] = 0                
    return imgUmbralizada

def dilatacion( img ):
    imgDilatada = np.zeros( img.shape , dtype=np.uint8 )
    for i in range( 0 , img.shape[0] ):
        for j in range( 0 , img.shape[1] ):
            if img[i][j] == 255:
                for y in range( -1 , 2 ):
                    for x in range( -1 , 2 ):
                        try:
                            imgDilatada[i+x][j+y] = 255
                        except:
                            pass
    return imgDilatada
#############################################################################################
#                                           MAIN
if __name__ == '__main__':
    img = cv2.imread( './img/objetos.jpg' , 2 )
    plt.subplot( 1 , 3 , 1 )
    plt.imshow( img , 'gray' )
    plt.title( 'Imagen Original' )
    plt.axis( 'off' )

    img2 = umbralizacion( img )
    plt.subplot( 1 , 3 , 2 )
    plt.imshow( img2 , 'gray' )
    plt.title( 'Imagen Umbralizada' )
    plt.axis( 'off' )

    img3 = dilatacion( img2 )
    plt.subplot( 1 , 3 , 3 )
    plt.imshow( img3 , 'gray' )
    plt.title( 'Imagen Dilatada' )
    plt.axis( 'off' )

    plt.show()