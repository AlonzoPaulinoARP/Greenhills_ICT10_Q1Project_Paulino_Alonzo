from pyscript import display, document


def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2") 
    prod3 = document.getElementById("item3") 
    prod4 = document.getElementById("item4") 
    prod5 = document.getElementById("item5") 

    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked # this adds all the order values when checked but when not checked gives a value of 0
    tax = subtotal * 0.12
    total = subtotal + tax
    
    display(f'Subtotal: {subtotal}', target="show")
    display(f'Tax: {tax}', target="show")
    display(f'Total: {total}', target="show")

def clear_order(e):
    document.getElementById('show').innerHTML = " " # this is used to clear the entire receipt