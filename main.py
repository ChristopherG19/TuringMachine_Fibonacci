from TM import *
from build import *

if __name__ == "__main__":
    
    print('\nBienvenido al PROYECTO 1\n')
    print(' --> Teniendo en cuenta')
    print('\t*\tLa representacion se da con numeros naturales')
    print('\t*\tEl retorno sera el valor de la posicion solicitada')
    print('\t*\tLas graficas se muestran en el archivo empirical_analysis.ipynb')
    print('\t*\tPara obtener un nuevo valor ejecutar proyecto1.py nuevamente y cambiar el valor n\n')

    veri = True
    while(veri):
        num = input('Numero de Fibonacci que desea calcular: ')
        if(num == 'exit'):
            veri = False
            print("\nGracias por utilizar este programa\n")
        else:
            if (int(num) < 0):
                num = int(-num)
            input_cinta = leerCinta(int(num))
            maquina = buildTM(input_cinta)
            print("Resultado: ", maquina.fibonacci().count('1'))