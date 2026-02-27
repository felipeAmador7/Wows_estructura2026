# Wows_estructura2026


[Doc Estructura (1).md](https://github.com/user-attachments/files/25606845/Doc.Estructura.1.md)



# **TALLER 1 \- Array and Linked list**

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

Las estructuras de datos lineales permiten organizar información de manera secuencial, facilitando su almacenamiento, acceso y manipulación. Dentro de estas estructuras se encuentran los arreglos dinámicos y las listas enlazadas, las cuales, aunque cumplen funciones similares, presentan diferencias significativas en su implementación interna y rendimiento.

El presente trabajo tiene como objetivo implementar manualmente un ArrayList y un LinkedList utilizando programación orientada a objetos, comprendiendo su funcionamiento interno, aplicando validaciones y analizando su complejidad algorítmica.

## **Estructuras de Datos Lineales**

Una estructura de datos lineal es aquella en la que los elementos se organizan secuencialmente, es decir, cada elemento tiene un predecesor y un sucesor (excepto el primero y el último).

Ejemplos de estructuras lineales:

* Listas  
* Pilas  
* Colas  
* Arreglos dinámicos

Estas estructuras permiten recorrer los datos en orden y son fundamentales para la construcción de algoritmos más complejos.

## **ArrayList**

El ArrayList es una estructura basada en un arreglo dinámico. Internamente utiliza memoria contigua, lo que permite acceso directo a cualquier posición mediante su índice.

Características principales:

* Acceso directo en tiempo constante O(1).  
* Inserción al final eficiente.  
* Inserción o eliminación en posiciones intermedias requiere desplazamiento de elements.  
* Uso eficiente de memoria contigua.

Representación conceptual:

\[10\]\[20\]\[30\]\[40\]

El acceso al elemento 30 se realiza directamente mediante su índice.

## **LinkedList**

El LinkedList es una estructura compuesta por nodos. Cada nodo contiene:

* Un dato.  
* Una referencia al siguiente nodo.

No utiliza memoria contigua, sino referencias dinámicas.

Representación conceptual:

10 → 20 → 30 → 40 → None

Características principales:

* Inserción eficiente al inicio.  
* No requiere desplazamiento de elementos.  
* Acceso secuencial O(n).  
  Uso adicional de memoria para referencias.

# **IMPLEMENTACIÓN DEL ARRAYLIST**

## **Diseño de la Clase**

La clase ArrayList contiene dos atributos principales:

* `_data`: lista interna donde se almacenan los elementos.  
* `_size`: variable que controla manualmente el número de elementos.

Se decidió manejar el tamaño manualmente para simular el comportamiento interno de un arreglo dinámico real.

## **Métodos Implementados**

### **size()**

Retorna el número de elementos almacenados.  
 Complejidad: O(1).

### **isEmpty()**

Verifica si la lista está vacía.  
 Complejidad: O(1).

### **add(element)**

Agrega un elemento al final de la lista.  
 Complejidad: O(1).

### **add(index, element)**

Inserta un elemento en una posición específica.  
 Se realiza un desplazamiento manual hacia la derecha para abrir espacio.  
 Complejidad: O(n).

### **remove(index)**

Elimina el elemento en la posición indicada.  
 Se realiza un desplazamiento hacia la izquierda para mantener la continuidad.  
 Complejidad: O(n).

### **get(index)**

Retorna el elemento en una posición específica.  
 Complejidad: O(1).

### **set(index, element)**

Reemplaza el elemento en una posición específica.  
 Complejidad: O(1).

### **contains(element)**

Recorre la lista para verificar si el elemento existe.  
 Complejidad: O(n).

### **clear()**

Elimina todos los elementos y reinicia el tamaño.  
 Complejidad: O(1).

# **IMPLEMENTACIÓN DEL LINKEDLIST**

## **Clase Node**

Cada nodo contiene:

* `data`: valor almacenado.  
* `next`: referencia al siguiente nodo.

## **Diseño del LinkedList**

La clase LinkedList contiene:

* `head`: referencia al primer nodo.  
* `_size`: contador del número de elementos.

## **Métodos Implementados**

### **addFirst(element)**

Inserta un nodo al inicio de la lista.  
 Complejidad: O(1).

### **addLast(element)**

Recorre la lista hasta el final e inserta el nuevo nodo.  
 Complejidad: O(n).

### **removeFirst()**

Elimina el primer nodo actualizando la referencia head.  
 Complejidad: O(1).

### **get(index)**

Recorre la lista hasta la posición indicada.  
 Complejidad: O(n).

### **contains(element)**

Recorre nodo por nodo buscando el elemento.  
 Complejidad: O(n).

### **clear()**

Elimina la referencia al primer nodo.  
 Complejidad: O(1).

## 

## **Gestión de Errores**

Durante la implementación se incluyeron validaciones para:

* Índices negativos.  
* Índices mayores al tamaño actual.  
* Eliminación cuando la lista está vacía.

Se utilizaron excepciones como `IndexError` para garantizar que el sistema no presente fallos silenciosos y proporcione mensajes claros ante errores.

**Clases**

* La clase Node representa cada elemento de la lista, que contiene el valor almacenado (data) y la referencia al siguiente nodo (next).  
* La clase LinkedList contiene la referencia al primer nodo (head) y la cantidad de elementos actuales (\_size)

**Validaciones**:

* Ver si la lista está vacía antes de finalizar  
* Verificar si el índice está dentro del rango  
* Manejar el caso especial cuando se elimina el primer nodo  
* Manejar el caso cuando la lista solo tiene un elemento  
* Cuando ocurre un error de rango, se lanza un IndexError  
    
    
    
  


  
**Pruebas de funcionamiento**

Para probar el funcionamiento del ArrayList y del LinkedList se hicieron diferentes pruebas

* Pruebas en ArrayList  
  Aquí se probaron inserciones, elminicación y la búsqueda de un elemento al final y en posiciones específicas

El resultado obtenido es:  
![][image2]

También se probó obtener un elemento fuera de rango:

![][image3]

* Pruebas en LinkedList  
    
  También se probó inserción, eliminación, búsqueda y error  
    
  ![][image4]  
    
  ![][image5]  
  


  
**Comparación final**

| Característica | ArrayList | LinkedList |
| :---- | :---- | :---- |
| Memoria | Contigua | No contigua |
| Acceso por índice | O(1) | O(n) |
| Insertar al principio | O(n) | O(1) |
| Insertar al final | O(1)\* | O(n) |
| Eliminar en medio | O(n) | O(n) |
| Uso de memoria | Menor | Mayor |

**Conclusión**

Implementar el ArrayList y el LinkedList permitió conocer las diferencias que tienen entre sí en cuanto a estructura o rendimiento. El ArrayList usa una memoria contigua, lo que hace que el acceso sea más rápido, mientras que el LinkedList usa nodos enlazados, lo que favorece las inserciones dinámicas. Dependiendo de lo que se necesite, es recomendable usar una u otra.

Un ArrayList es más útil al momento de querer acceder a un dato en específico sin necesidad de modificarlo, por ejemplo acceder al historial médico de un paciente.

Un LinkedList sirve más para modificar constantemente los datos de una lista, por ejemplo una fila de reproducción.

[image1]: 

[image2]: 

[image3]: 

[image4]: 

[image5]: 
