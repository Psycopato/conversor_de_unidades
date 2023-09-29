"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
import temperatura
import masa
import tiempo
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] Convertir de Celsius a Fahrenheit")
        print("[2] convertir de Celsius a Kelvin")
        print("[3] convertir de Fahrenheit a Celsius")
        print("[4] convertir de Fahrenheit a Kelvin")
        print("[5] convertir de Kelvin a Celsius")
        print("[6] convertir de Kelvin a Fahrenheit")
        print("[7] convertir de kilogramos a gramos")
        print("[8] convertir de kilogramos a toneladas")
        print("[9] convertir de gramos a kilogramos")
        print("[10] convertir de gramos a toneladas")
        print("[11] convertir de toneladas a kilogramos")
        print("[12] convertir de toneladas a gramos")
        print("[13] convertir de segundos a minutos")
        print("[14] convertir de segundos a horas")
        print("[15] convertir de minutos a segundos")
        print("[16] convertir de minutos a horas")
        print("[17] convertir de horas a segundos")
        print("[18] convertir de horas a minutos")
        print("[0] Salir")
        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        valorInicial = int(input("Ingrese valor  inicial: "))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resultado=temperatura.celsius_a_fahrenheit(valorInicial)
                print("El resultado es: ", resultado)

            elif opcion == 2:
                resultado=temperatura.celsius_a_kelvin(valorInicial)
                print("El resultado es: ", resultado)

            elif opcion == 3:
                resultado=temperatura.fahrenheit_a_celsius(valorInicial)
                print("El resultado es: ", resultado)

            elif opcion == 4:
                resultado=temperatura.fahrenheit_a_kelvin(valorInicial)
                print("El resultado es: ", resultado)

            elif opcion == 5:
                print("El resultado es: ", resultado)
                resultado=temperatura.kelvin_a_celsius(valorInicial)

            elif opcion == 6:
                print("El resultado es: ", resultado)
                resultado=temperatura.kelvin_a_fahrenheit(valorInicial)

            elif opcion == 7:
                print("El resultado es: ", resultado)
                resultado=masa.Kilogramos_a_Gramos(valorInicial)

            elif opcion == 8:
                print("El resultado es: ", resultado)
                resultado=masa.Kilogramos_a_Toneladas(valorInicial)

            elif opcion == 9:
                print("El resultado es: ", resultado)
                resultado=masa.Gramos_a_Kilogramos(valorInicial)

            elif opcion == 10:
                print("El resultado es: ", resultado)
                resultado=masa.Gramos_a_Toneladas(valorInicial)

            elif opcion == 11:
                print("El resultado es: ", resultado)
                resultado=masa.Toneladas_a_Kilogramos(valorInicial)

            elif opcion == 12:
                print("El resultado es: ", resultado)
                resultado=masa.Toneladas_a_Gramos(valorInicial)

            elif opcion == 13:
                print("El resultado es: ", resultado)
                resultado=tiempo.segundos_a_minutos(valorInicial)

            elif opcion == 14:
                print("El resultado es: ", resultado)
                resultado=tiempo.segundos_a_horas(valorInicial)

            elif opcion == 15:
                print("El resultado es: ", resultado)
                resultado=tiempo.minutos_a_segundos(valorInicial)

            elif opcion == 16:
                print("El resultado es: ", resultado)
                resultado=tiempo.minutos_a_horas(valorInicial)
        
            elif opcion == 17:
                print("El resultado es: ", resultado)
                resultado=tiempo.horas_a_segundos(valorInicial)
        
            elif opcion == 18:
                print("El resultado es: ", resultado)
                resultado=tiempo.horas_a_minutos(valorInicial)
        
        

            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()