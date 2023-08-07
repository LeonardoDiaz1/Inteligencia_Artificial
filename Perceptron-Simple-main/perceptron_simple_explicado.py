###############################################################################################
#                                   PERCEPTRON SIMPLE                                         #
###############################################################################################

###############################################################################################
#                                      Leonardo Díaz                                          #
###############################################################################################

###############################################################################################
#                                       EXPLICACIÓN                                           #
###############################################################################################

import random

def calculo(t, e, um, x1, x2, d, p1, p2, u):
    
    #Calcular valor entre 0 y 1 (n)
    n = random.uniform(0, 1.0)

    #Calcular coeficiente de aprendizaje (y)
    y = ( p1 * x1) + (p2 * x2) - u

    #Calcular f
    f = 0
    if y >= 0:
        f = 1
    elif y < 0:
        f = 0
    else:
        print("Hay un problema al calcular el coeficiente de aprendizaje (y)")

    #Calcular valor de error
    e = 0
        
    e = d - f

    #Calcular variación para los pesos
    v1 = n * e * x1
    v2 = n * e * x2

    #Calcular nuevo valor de peso
    pe1 = p1 + v1 
    pe2 = p2 + v2

    #Calcular nuevo umbral
    um = u - (n * e)


    
    print("\n", 
        "################################","\n", 
        "Iteración ", t,"\n", 
        "################################","\n",
        "x1:",x1,"\n", 
        "x2:",x2,"\n",
        "p1:",p1,"\n",
        "p2:",p2,"\n",
        "n:",n,"\n",
        "y:",y,"\n",
        "f:",f,"\n",
        "d:",d,"\n",
        "u:",u,"\n",
        "e:",e,"\n",
        "v1:",v1,"\n",
        "v2:",v2,"\n",
        "pe1:",pe1,"\n",
        "pe2:",pe2,"\n",
        "um:",um,"\n",
        )
    t += 1
    um_lis.append(um)
    return (t,  e, um)

def valor_espe(d,x1, x2):
    if x1== 0 and x2==0:
        d = 0
    elif x1== 0 and x2==1:
        d = 0
    elif x1== 1 and x2==0:
        d = 0
    elif x1== 1 and x2==1:
        d = 1
    else:
        print("Error en los pesos, valores deben ser 1 o 0")
    return(d)

def pesos(p1, p2, u):
    #Inicializar los pesos p1 y p2 (Valores aleatorios entre -1 y 1)
    p1 = random.uniform(-1.0, 1.0)
    p2 = random.uniform(-1.0, 1.0)

    #Calcular umbral (Valor aleatorio entre -1 y 1)
    u = random.uniform(-1.0, 1.0)
    
    return (p1, p2, u)

t = 1
d = 0
e = 1
p1 = 0
p2 = 0
u = 0
p1 ,p2 , u = pesos(p1, p2, u)
um_lis = [0, 0, 0, 1]
um = 1

while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um :
    for i in [0, 1, ]:
        for j in [0, 1]:
                        
            x1=i
            x2=j
            
            if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um :
                break
                
            elif e == 0:
                
                #print("No cambiar los pesos, ni el umbral")
                d = valor_espe(d, x1, x2)             
                t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u)
            else:
                #print("Hay que cambiar los pesos y el umbral")
                p1 ,p2 , u = pesos(p1, p2, u)
                d = valor_espe(d, x1, x2)             
                t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u)
                    
            
print(um)
print(um_lis, "\n")
        