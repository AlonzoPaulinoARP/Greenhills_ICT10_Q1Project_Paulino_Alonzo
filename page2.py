from pyscript import display, document


def create_sku(e):
    drop_category = document.getElementById('category')
    category_code = display(drop_category.value, target='show') # displays the type of food category
    text_name = document.getElementById('name').value
    name_code = display(str(text_name.upper()), target='show') # displays the name of the product typed
    text_stock = document.getElementById('stock').value
    stock_code = display(str(text_stock), target='show') # displays the stock quantity
    


def clear_sku(e):
    document.getElementById('show').innerHTML = " " # this is used to clear the entire sku