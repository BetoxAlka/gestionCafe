import gestionCafe

def test_0():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Frappe, 5, 10, 25"))
    respuestaE = "Nombre de la bebida: Frappe | Tamanios para la bebida: [5, 10, 25]"
    assert respuestaE == respuestaR
    
def test_name1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Capuccino, 25"))
    respuestaE = "Nombre de la bebida: Capuccino | Tamanios para la bebida: [25]"
    assert respuestaE == respuestaR
    
def test_name2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("7rr4pp3, 5, 10, 15, 20, 25"))
    respuestaE = "Nombre de la bebida INVALIDO"
    assert respuestaE == respuestaR

def test_namelen1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("A, 5, 10, 15, 20"))
    respuestaE = "Nombre de la bebida INVALIDO"
    assert respuestaE == respuestaR
    
def test_namelen2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Parangaricutirimicaro, 5, 10"))
    respuestaE = "Nombre de la bebida INVALIDO"
    assert respuestaE == respuestaR
    
def test_numberlen1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Chocolate, 5, 10, 15, 20, 100"))
    respuestaE = "Tamanio INVALIDO"
    assert respuestaE == respuestaR
    
def test_numberlen2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Chocolate, 0, 1, 15, 49, 55"))
    respuestaE = "Tamanio INVALIDO"
    assert respuestaE == respuestaR
    
def test_intnumber1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Capuccino, 5, 10, 15, 20, 25"))
    respuestaE = "Nombre de la bebida: Capuccino | Tamanios para la bebida: [5, 10, 15, 20, 25]"
    assert respuestaE == respuestaR
    
def test_intnumber2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Chocolate, 5.2, 10.9"))
    respuestaE = "Nombre de la bebida: Chocolate | Tamanios para la bebida: [5, 10]"
    assert respuestaE == respuestaR

def test_order1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Vainilla, 2, 7, 9, 12"))
    respuestaE = "Nombre de la bebida: Vainilla | Tamanios para la bebida: [2, 7, 9, 12]"
    assert respuestaE == respuestaR
    
def test_order2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Vainilla, 7, 12, 2, 9"))
    respuestaE = "Los tamanios no estan ordenados de forma ascendente"
    assert respuestaE == respuestaR
    
def test_quantity1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Oreo"))
    respuestaE = "Cantidad de tamanios INVALIDO"
    assert respuestaE == respuestaR
    
def test_quantity2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Oreo, 5, 10, 15, 20, 25, 30"))
    respuestaE = "Cantidad de tamanios INVALIDO"
    assert respuestaE == respuestaR
    
def test_namefirst1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("10, Coco, 10, 15, 20, 25"))
    respuestaE = "Nombre de la bebida INVALIDO"
    assert respuestaE == respuestaR
    
def test_namefirst2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("5, 10, 15, Coco, 20"))
    respuestaE = "Nombre de la bebida INVALIDO"
    assert respuestaE == respuestaR
    
def test_spaces1():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("Frappe,    5, 10    , 25   "))
    respuestaE = "Nombre de la bebida: Frappe | Tamanios para la bebida: [5, 10, 25]"
    assert respuestaE == respuestaR

def test_spaces2():
    respuestaR = gestionCafe.cafe(gestionCafe.stringtolist("  Fra ppe  , 5, 1 0, 2 5"))
    respuestaE = "Nombre de la bebida: Frappe | Tamanios para la bebida: [5, 10, 25]"
    assert respuestaE == respuestaR