import random

def calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat):
    y = round(( ( p1 * x1) + (p2 * x2) + (p3 * x3) - u ) , 2)
    f = 0
    e = 0
    
    if y >= 0:
        f = 1
    elif y < 0:
        f = 0
    else:
        print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
          
    e = d - f
    
    v1 = n * e * x1
    v2 = n * e * x2
    v3 = n * e * x3
    
    pe1 = p1 + v1 
    pe2 = p2 + v2
    pe3 = p3 + v3

    um = u - (n * e)

    print("\n", 
        "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n", "x3:",x3,"\n","p1:",p1,"\n","p2:",p2,"\n","p3:",p3,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","v3:",v3,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","pe3:",pe3,"\n","um:",um,"\n",)
    t += 1
    um_lis.append(um)
    return (t,  e, um)

def valor_espe(d, pat, x1, x2, x3):
    if x1== 0 and x2==0 and x3==0:
        d = 0
        pat = 1
    elif x1== 0 and x2==0 and x3==1:
        d = 1
        pat = 2
    elif x1== 0 and x2==1 and x3==0:
        d = 1
        pat = 3
    elif x1== 0 and x2==1 and x3==1:
        d = 1
        pat = 4
    elif x1== 1 and x2==0 and x3==0:
        d = 1
        pat = 5
    elif x1== 1 and x2==0 and x3==1:
        d = 1
        pat = 6
    elif x1== 1 and x2==1 and x3==0:
        d = 1
        pat = 7
    elif x1== 1 and x2==1 and x3==1:
        d = 1
        pat = 8
    else:
        print("Error en los pesos, valores deben ser 1 o 0")
    return(d, pat)

def pesos(p1, p2, p3, u):
    p1 = round(random.uniform(-1.0, 1.0), 2)
    p2 = round(random.uniform(-1.0, 1.0), 2)
    p3 = round(random.uniform(-1.0, 1.0), 2)
    u = round(random.uniform(-1.0, 1.0), 2)
    return (p1, p2, p3, u)


t = 1
d = 0
e = 1
p1 = 0
p2 = 0
p3 = 0
u = 0
p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
um_lis = [0, 0, 0, 0, 0, 0, 0, 1]
um = 1
pat = 0

n = round(random.uniform(0, 1.0), 2)

while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um or um_lis[-5] != um or um_lis[-6] != um or um_lis[-7] != um or um_lis[-8] != um:
    for i in [0, 1, ]:
        for j in [0, 1]:
            for k in [0, 1]:            
                x1=i
                x2=j 
                x3=k 
                
                if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um and um_lis[-5] == um and um_lis[-6] == um and um_lis[-7] == um and um_lis[-8] == um:
                        break       
                elif e == 0:
                    d, pat = valor_espe(d, pat, x1, x2, x3)             
                    t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                    if e != 0 :
                        p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                        d, pat = valor_espe(d, pat, x1, x2, x3)             
                        t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                else:
                    while e != 0 :
                        p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                        d, pat = valor_espe(d, pat, x1, x2, x3)             
                        t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                    
            
print(um)
print(um_lis, "\n")
        
