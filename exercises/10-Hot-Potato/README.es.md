## 10 - Papa Caliente

## Que vas a aprender

En este ejercicio vas a simular un juego usando una cola.
Es una forma practica de aplicar rotacion FIFO en rondas.

## Que debes implementar

Implementa la funcion `hot_potato(players, passes)`.

Reglas:

- Usa una cola para rotar jugadores.
- En cada ronda, rota `passes` veces:
	- quita del frente
	- agrega al final
- Despues de rotar, elimina al jugador del frente.
- Repite hasta que quede solo 1 jugador.
- Devuelve el ganador.

## Guia paso a paso

1. Carga todos los jugadores en una cola.
2. Mientras haya mas de un jugador:
	 - rota `passes` veces.
	 - elimina a una persona.
3. Cuando quede uno, retornalo.
4. Guarda en `winner` el resultado de la llamada requerida.

## Ejemplo rapido

Con `players = ["Ana", "Luis", "Mia", "Leo"]` y `passes = 2`:

- En cada ronda se hacen 2 rotaciones.
- Luego se elimina al jugador del frente.
- El proceso termina con un unico ganador.

## Nota

Cada rotacion conserva el orden relativo, solo mueve el frente al final.

## Variables requeridas

- `winner`: resultado de `hot_potato(["Ana", "Luis", "Mia", "Leo"], 2)`
