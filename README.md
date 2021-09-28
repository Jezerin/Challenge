# Challenge
Code proposal for challenge

Funcionamiento
Ejecutar main para correr el programa. Es posible crear instancias adicionales de usuario que hagan request al elevador, una vez creadas, agragarlas a la lista llamada users.

Análisis del problema


El problema plantea un edificio en el cual se encuentran 2 elevadores contíguos, independientes y funcionales, estos elevadores estan a disposición de los usuarios que laboran en dicha ubicación. El edificio cuenta con 7 pisos.

Cada elevador cuenta con los siguientes mecanismos:

- Panel de botones que permiten al usuario ingresar el piso al cual desea trasladarse
	- Cada uno de estos botones tiene una luz propia  la cual permanecerá encendida hasta que el elevador llegue a su destino
	- Esta luz será apagada automaticamente despues de abrir las puertas
- Puertas
	- Deben ser cerradas antes de que el elevador entre en operación para traslado
	- Deben ser abiertas cuando el elevador llegue a su destino
- Motor
	- Debe ser activado para que el elevador entre en movimiento
	- Debe ser desactivado cuando el elevador llegue a su destino

De igual manera, existen paneles para visualización del estado del elevador, estos están presentes en cada uno de los pisos del edificio.


Algoritmo


La petición inicia cuando un usuario solicita un elevador desde cualquiera de los paneles presentes en cada uno de los 7 pisos . El siguiente algoritmo funciona en esta representacion textual, como un loop

1. Recibir petición (push botton)
2. Encender luz del boton "Up" o "Down" según la elección del usuario
3. Detectar elevador disponible
4. Si ambos elevadores están disponibles,  se deberá activar el elevador mas cercano al usuario (diferencia de pisos)
5. Si el elevador no se encuentra en el piso del usuario se deberá trasladar al piso del request
6. Antes de mover el elevador, verificar que las puertas estén cerradas
7. Activar el motor para mover el elevador
8. Una vez en el piso donde el usuario se encuentra, apagar el motor
9. Abrir las puertas para que el usuario ingrese
10. El usuario selecciona el piso a donde desea moverse, se enciende la luz del piso al que se va a trasladar
11. El elevador cierra las puertas
12. El elevador activa el motor
13. El elevador se mueve al piso deseado
14. Una vez en el destino, el elevador apaga el motor
15. El elevador abre las puertas
16. Se apaga la luz del piso que seleccionó anteriormente el usuario
18. El usuario sale al piso que eligió como destino
