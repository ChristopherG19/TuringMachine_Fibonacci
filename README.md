# TuringMachine_Fibonacci

Universidad del Valle de Guatemala <br>
Facultad de Ingeniería <br>
Departamento de Ciencias de la Computación <br>
Análisis y Diseño de Algoritmos <br>

## Integrantes 
Óscar Estrada		    20565 <br>
Christopher García		20541 <br>
Javier Valle     		20159 <br>
Maria Isabel Solano		20504 <br>
Gabriel Vicente		20498 <br>
Mario de Leon		19019 <br>

## Introducción 
El objetivo de este proyecto es evaluar la comprensión del estudiante sobre la notación O en el tiempo de ejecución de un algoritmo.

## Instrucciones
Su grupo deberá investigar sobre la notación asintótica O, el tiempo de ejecución de una máquina de Turing y realizar una simulación de una máquina de Turing determinista de una cinta que calcule la sucesión de Fibonacci (https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci).  Debe  definir  una  convención para  manejar  los  enteros  no  negativos  en  la  cinta  y  definir  una  convención  de  la  interpretación  de  la respuesta en la cinta. Asimismo, los componentes que definen dicha máquina se deben cargar a través de un archivo, permitiendo que el programa pueda hacer la simulación de la ejecución de cualquier máquina de Turing determinista de una cinta. <br>

Descripción de convenciones elegidas:
- El programa consta de los siguientes elementos:
  - Una clase Turing Machine que posee:
    - Un diccionario de transiciones (Key = {Estado, símbolo}, Value = {Estado, símbolo dirección})
    - Símbolo blank
    - Estado inicial y estado final 
    - La cinta con la que se trabajará
    - Método de lectura para obtener los símbolos de la cinta
    - Método fibonacci que se encarga del movimiento y escritura en la cinta
  - Un clase Tape que posee:
    - La cinta en sí creada con el input del archivo y blanks
    - La posición actual
    - El output final
    - Método que determina si se llegó al final de la cinta
    - Método que lee cada símbolo (simula al lector)
    - Método que obtiene la posición del lector
    - Método que reinicia el lector a su posición inicial
    - Método que escribe símbolos en la cinta
    - Método que se encarga del movimiento en la cinta
    - Métodos para obtener el resultado final de la cinta
  - Un archivo build donde se tiene:
    - Un método que convierte el número ingresado en una cadena aceptada por la cinta
    - Un método que construye la máquina en sí con ayuda de los archivos .txt que se describen más adelante, de estos se extrae la información necesaria para crear la máquina
  - Un documento, maquina.txt, con la descripción de la máquina de Turing, incluyendo su estado inicial, su estado de aceptación, alfabeto y nombre de todos los estados. 
  - Un documento, transiciones.txt, con las transiciones de la máquina de Turing.
  - Un programa write.py, el cual, a partir de las transiciones genera un genera un documento llamado graph.txt que contiene la información de un grafo de esas transiciones. Con ayuda de Graphviz, a partir del txt se obtiene una imágen con la representación gráfica de la máquina. 
- La cadena inicial, el input, es un número entero, el cual a partir de él se obtiene su respectiva cadena de 1s.
  - Si el input es negativo, se obtiene su valor absoluto y de él se obtiene la secuencia de Fibonacci. 
  - Si el número es 0, el programa no continúa y termina.
- La respuesta generada por la máquina de Turing, el output,  es una secuencia de 1s que representan el número según la cantidad de 1s que hay en la cinta. Pero para facilitar la lectura del resultado, al finalizar se realiza un conteo de la cantidad de 1s
- La cinta utilizada crece proporcionalmente al número ingresado, se trató de simular una cinta infinita pero por tema de recursos esto se tuvo que limitar y es por ello que se debe ajustar el tamaño de la cinta para que acepte números más grandes.



## Diagrama
![output](https://user-images.githubusercontent.com/60373842/222864712-46f29428-c3bc-426c-a77e-2128a2a6833f.jpg)

## Análisis empírico
a. Listado de entradas de prueba usadas para medir tiempos de ejecución de la máquina. 
- Para esto se creó un archivo .csv (time_value.csv) donde se almacenan los input ingresados y el tiempo de la ejecución con dicho input. Algunos de los valores ingresados fueron: 1,2,3,4,...,15,...
- Se realizaron pruebas de manera automática para obtener una cantidad considerable de datos que permitieran realizar un análisis empírico relevante. En un principio trabajamos con 300 pruebas de diferentes valores y tiempos de ejecución.
b. Diagrama de dispersión que muestre los tiempos de ejecución de la máquina en función de su tamaño de entrada. <br>
![image](https://user-images.githubusercontent.com/60373842/222868984-eb670105-aee4-40e8-9b6b-8ee3ac183cf1.png)
c. Regresión polinomial que se ajuste mejor a los datos.<br>
![image](https://user-images.githubusercontent.com/60373842/222869088-faf502f5-a2ff-4927-b498-bfb56b0d8949.png)
