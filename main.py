import time
import csv
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
        if num == 'exit' or num == 0:
            veri = False
            print("\nGracias por utilizar este programa\n")
        else:
            #Time and result
            start_time = time.time()
            
            if (int(num) < 0):
                num = int(-num)
            input_cinta = leerCinta(int(num))
            maquina = buildTM(input_cinta)
            print("Resultado: ", maquina.fibonacci().count('1'))
            
            #Time and registration
            end_time = time.time()
            execution_time = end_time - start_time
            print("El tiempo de ejecución fue:", execution_time, "segundos\n")
            with open('time_value.csv', mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([num, execution_time])