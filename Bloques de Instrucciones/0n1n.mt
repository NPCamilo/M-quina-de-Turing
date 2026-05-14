Estados: q0,q1,q2,q3,q4,qf
Alfabeto_entrada: 0,1
Alfabeto_cinta: 0,1,B,X,Y
Inicial: q0
Finales: qf
Blanco: B
Transiciones:
# q0: Busca el primer 0 para marcarlo como X
q0,0 -> q1,X,R
q0,Y -> q4,Y,R

# q1: Salta 0s y Ys buscando el primer 1
q1,0 -> q1,0,R
q1,Y -> q1,Y,R
q1,1 -> q2,Y,L

# q2: Se mueve a la izquierda para iniciar el retorno
q2,0 -> q2,0,L
q2,Y -> q2,Y,L
q2,X -> q0,X,R

# q4: Verificación final (ya no deben quedar 0s ni 1s)
q4,Y -> q4,Y,R
q4,B -> qf,B,S