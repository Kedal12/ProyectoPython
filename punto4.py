class Asiento:
    def __init__(self,fila,nombre,precio):
        self.fila = fila
        self.nombre=nombre
        self.precio= precio
    def __repr__(self):
        return f"({self.fila}, nombre {self.nombre}, precio ${self.precio})"
#matriz(lista) de asientos desordenados
matriz_asientos=[
    [Asiento("A1","JUAN",30000),Asiento("A1","ANA",35000),Asiento("A1","DANIEL",25000)],
    [Asiento("B2","JOSE",22000),Asiento("B2","FELIPE",21000),Asiento("B2","ANDRES",24000)],
    [Asiento("C3","SOFIA",20000),Asiento("C3","JOSUE",18000),Asiento("C3","JORGE",19000)],
    [Asiento("D4","TATIANA",16000),Asiento("D4","JOAQUIN",14000),Asiento("D4","GUILLERMO",15000)]
]
#Funcion para ordenar los asientos por precio 
def ordenar_asientos_por_precio(matriz):
    for fila in matriz:
        fila.sort(key = lambda Asiento : -Asiento.precio)
#Ordenar los asientos de la "matriz"
ordenar_asientos_por_precio(matriz_asientos)

for fila in matriz_asientos:
    print(fila)