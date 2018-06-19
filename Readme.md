# IMPLEMENTACIÓN TABÚ SEARCH 

- Alumnos: 
	- Ignacio Ibañez
	- Nestor Mora 
	- Francisco Muñoz
	- Joaquín Villagra
- Profesor: Mario Inostroza

## Objetivo
Implementar Tabú Search comparando los resultados obtenidos con la implementación de Simulated Annealing.  


## Especificación de Desarrollo
Según lo especificado en cátedra, Tabú search funciona con Memorias de corto, mediano y largo plazo, las cuales tienen como finalidad:
	- Corto plazo: Prevenir ciclos sobre soluciones ya visitadas
	- Mediano plazo: Caracteriza las buenas soluciones, permite indagar más en dicha vecindad (Intesificación)
	- Largo plazo: Caracteriza aquellas soluciones no visitadas, es decir permite saltar a conjuntos de vecindad alejados (Diversificación)

Teniendo en cuenta lo anterior, se construye tabú Search bajo la siguiente lógica: 
1) En Memorias.py se construye cada memoria como una estructura de datos que en su codificación permite simplificar el procesamiento futuro. Se ocupa la idea de funcionamiento de memorias Cache. 
	- Para la memoria de corto plazo, se guarda el histórico reciente.
	- Para la de mediano plazo se almacenan las soluciones mejores rankeadas. En este caso se hace uso de un timestamp para determinar el tiempo que ha estado una solución en el conjunto, este valor es de utilidad para memorias con un N reducido, aplicando la lógica de políticas de reemplazo existente en memorias Cache.
	- Para la memoria de largo plazo se construye un conjunto de soluciones a partir del conteo de la frecunecia de los atributos utilizados a lo largo del proceso de busqueda. En términos prácticos, al momento de diversificar se usa la solución que reporte el min en sus frecuencias de uso a nivel de atributos 


## Reglas de intensificación y diversificación

Para probar se utilizo:
==========================

Diversificación según número de iteraciones:
- 10 Iteraciones
- 50 Iteraciones
- 100 Iteraciones
- 1000 Iteraciones
