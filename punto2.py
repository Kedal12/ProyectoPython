#2)	la tienda D1 requiere identificar las ventas asociadas al mes de abril, por lo cual recurre al área de sistemas para que le ayude con eso, y necesita que se le presente un informe indicando cuanto fueron sus ventas totales 

class Venta():
    def __init__(self, producto, valor, cantidad, mes):
        self.producto = producto
        self.valor = valor
        self.cantidad = cantidad
        self.mes = mes
        

ventas = [Venta("jabon",2000,2,"Enero"),Venta("atun",5500,8,"Febrero"),Venta("pollo",8000,4,"Abril"),Venta("legumbres",10000,1,"Abril"),Venta("desodorante",2100,5,"Octubre"),Venta("cuaderno",4000,4,"Marzo"),Venta("pan",1500,4,"Abril"),Venta("tostadas",1250,3,"Septiembre"),Venta("galletas",3400,6,"Agosto")]

# productos vendidos en abril: pollo-legumbres-pan
        
# Iteramos la lista validando que cada venta cumpla con que el mes sea abril y si cumple sumamos el valor multiplicado por la cantidad vendida de ese producto al total
total = 0
for venta in ventas:
    if venta.mes.lower() == "abril":
        total += venta.valor * venta.cantidad
        
        
#Imprimimos el informe

print("-------------VENTAS ABRIL------------")
for i in ventas:
    if i.mes.lower() == "abril":
        print(f" PRODUCTO: {i.producto} CANTIDAD: {i.cantidad} VALOR/Unidad: {i.valor} TOTAL: {i.cantidad * i.valor}")
        print()

print(f"Las ventas totales de los productos vendidos en el mes de Abril suman un TOTAL de: {total}")


