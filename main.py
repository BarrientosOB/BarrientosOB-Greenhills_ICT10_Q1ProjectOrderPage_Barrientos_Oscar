# explaining code
from pyscript import display, document

    
    
def ordering_form(e):
    item1 = document.getElementById("menu1")
    item2 = document.getElementById("menu2")
    item3 = document.getElementById("menu3")
    item4 = document.getElementById("menu4")
    name = document.getElementById("Oscar").value
    address = document.getElementById("Barrientos").value
    number = document.getElementById("Panganiban").value
    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked)
    
    display(f'Order for: {name}')
    display(f'Address: {address}')
    display(f'Contact number:{number}')
    display(f'Total amount: {total}')
  