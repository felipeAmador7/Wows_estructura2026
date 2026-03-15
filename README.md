






# **![][sergio.png]**

# **IMPLEMENTACIÓN DE STACK, QUEUE Y CIRCULAR LINKED LIST**

**Presentado por:**   
Felipe Amador  
Andres Carabali  
Kamila Guzman  
Salome Josa

**Presentado a:**  
Guillermo Andres de Mendoza Corrales

**Materia:**  
Estructura de datos lineales

# 

Universidad Sergio Arboleda  
Bogota, DC  
2026

# **IMPLEMENTACIÓN DE STACK**

## **Diseño de la Clase**

La clase Stack representa una estructura de datos tipo pila, la cual sigue el principio LIFO (Last In, First Out). Esto significa que el último elemento que se inserta es el primero que se elimina.

Internamente la implementación utiliza una lista de Python llamada items, la cual almacena los elementos de la pila.

Atributo principal:

items: lista interna donde se almacenan los elementos de la pila.

Representación conceptual:

Top

\[10\]

\[20\]

\[30\]

En este caso, el elemento 30 sería el primero en salir.

## **Métodos Implementados**

### **is\_empty()**

Verifica si la pila está vacía.

Retorna True si no hay elementos y False en caso contrario.

Complejidad: O(1)

### **push(item)**

Agrega un nuevo elemento en la parte superior de la pila.

Se utiliza el método append() de la lista para insertar el elemento.

Complejidad: O(1)

### **pop()**

Elimina y retorna el elemento que se encuentra en la parte superior de la pila.

Si la pila está vacía, se muestra un mensaje indicando que no se puede realizar la operación.

Complejidad: O(1)

### **peek()**

Permite observar el elemento que se encuentra en la parte superior de la pila sin eliminarlo.

Si la pila está vacía retorna None.

Complejidad: O(1)

### **size()**

Retorna la cantidad de elementos almacenados en la pila.

Complejidad: O(1)

## **Gestión de Errores**

Durante la implementación se manejaron algunas validaciones básicas:

* Verificar si la pila está vacía antes de eliminar un elemento.  
* Evitar errores cuando se intenta acceder a un elemento inexistente.  
* Retornar None cuando la operación no puede realizarse.

# **IMPLEMENTACIÓN DE QUEUE**

## **Diseño de la Clase**

La clase Queue representa una estructura de datos tipo cola, que sigue el principio FIFO (First In, First Out). Esto significa que el primer elemento que entra es el primero en salir.

Internamente utiliza una lista llamada elements donde se almacenan los elementos.

Atributo principal:

elements: lista interna donde se guardan los elementos de la cola.

Representación conceptual:

Front → \[10\]\[20\]\[30\]\[40\] ← Rear

El elemento 10 sería el primero en salir de la cola.

## **Métodos Implementados**

### **isEmpty()**

Verifica si la cola está vacía.

Complejidad: O(1)

### **push(element)**

Inserta un nuevo elemento al final de la cola.

Complejidad: O(1)

### **pop()**

Elimina y retorna el primer elemento de la cola.

Si la cola está vacía se lanza una excepción IndexError.

Complejidad: O(n) debido al desplazamiento de los elementos en la lista.

### **peek()**

Permite visualizar el primer elemento de la cola sin eliminarlo.

Si la cola está vacía se genera una excepción.

Complejidad: O(1)

### **tail()**

Retorna el último elemento de la cola.

Complejidad: O(1)

### **clear()**

Elimina todos los elementos de la cola.

Complejidad: O(1)

### **extend(iterable)**

Permite agregar múltiples elementos provenientes de otra colección.

Complejidad: O(n) dependiendo del número de elementos añadidos.

### **copy()**

Crea una copia independiente de la cola actual.

Complejidad: O(n)

### **Métodos especiales de Python**

También se implementaron métodos especiales que permiten un mejor manejo de la estructura:

\_\_str\_\_(): permite imprimir la cola de forma legible.

\_\_len\_\_(): permite obtener el tamaño usando len().

\_\_iter\_\_(): permite recorrer la cola con ciclos.

\_\_contains\_\_(): permite verificar si un elemento está en la cola usando in.

## **Gestión de Errores**

Se incluyeron validaciones para evitar operaciones inválidas:

* Lanzar excepciones cuando se intenta hacer pop o peek en una cola vacía.  
* Control del tamaño de la estructura para evitar accesos incorrectos.

# **IMPLEMENTACIÓN DE CIRCULAR LINKED LIST**

## **Clase Node**

La estructura se basa en nodos.

Cada nodo contiene:

* data: valor almacenado.  
* next: referencia al siguiente nodo.

## **Diseño del CircularList**

La clase CircularList representa una lista enlazada circular.

En este tipo de listas, el último nodo apunta nuevamente al primer nodo, formando un ciclo.

Representación conceptual:

A → B → C →

↑        ↓

←←←←←←←←

Atributos principales:

head: referencia al primer nodo.

tail: referencia al último nodo.

El atributo tail permite mantener la estructura circular conectando nuevamente con el head.

## **Métodos Implementados**

### **append(value)**

Agrega un nuevo nodo al final de la lista.

Si la lista está vacía, el nuevo nodo se convierte en head y tail.

Complejidad: O(1)

### **insert(index, value)**

Inserta un nodo en una posición específica.

Si el índice es 0, el nodo se inserta al inicio.

Si el índice es mayor, se recorre la lista hasta la posición correspondiente.

Complejidad: O(n)

### **delete(index)**

Elimina el nodo en la posición indicada.

Se manejan diferentes casos:

* Eliminar el primer nodo.  
* Eliminar el último nodo.  
* Eliminar nodos intermedios.

Complejidad: O(n)

### **display()**

Recorre la lista circular mostrando los elementos.

El recorrido termina cuando se vuelve al nodo inicial (head).

Complejidad: O(n)

## **Pruebas de Funcionamiento**

Para probar la lista circular se realizaron varias operaciones:

* Inserción de elementos con append()  
* Eliminación del primer nodo con delete(0)  
* Inserción en una posición específica con insert()

Ejemplo de salida:

A → B → C → (Head)

Después de eliminar el primer elemento:

B → C → (Head)

Después de insertar un nuevo elemento:

B → Z → C → (Head)

## **Gestión de Errores**

Durante la implementación se manejaron diferentes casos especiales:

* Cuando la lista está vacía.  
* Inserciones en la primera posición.  
* Eliminación del único nodo existente.  
* Actualización correcta del tail para mantener la estructura circular.

## **Conclusión**

La implementación de Stack, Queue y Circular Linked List permite comprender el funcionamiento interno de diferentes estructuras de datos lineales.

La pila es útil cuando se necesita trabajar con el último elemento insertado, como en algoritmos de retroceso o manejo de llamadas en programas.

La cola se utiliza cuando se requiere procesar los elementos en el mismo orden en que fueron insertados, como en sistemas de atención o procesamiento de tareas.

Por otro lado, la lista circular permite recorrer los elementos de manera continua sin necesidad de reiniciar el recorrido, siendo útil en aplicaciones como reproducción de listas o sistemas que operan en ciclos.

[image1]: <data:image/png;base64,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>
