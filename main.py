import product
import product_manager
import cart 
import random

#kreiranje instance klase ProductManager
manager=product_manager.ProductManager()

#kreiranje nekoliko objekata klase Produkt
pr1=product.Product("cokolada",250,35)
pr2=product.Product("smoki",75,15)
pr3=product.Product("mleko",135,20)

#dodavanje objekata u listu i prikaz iste
manager.input_product(pr1)
manager.input_product(pr2)
manager.input_product(pr3)

<<<<<<< HEAD
=======
#prikaz proizvoda
manager.display_products()

#prikaz ukupne vrednosti inventara
manager.total_value()

#kreiram instancu klase Cart
c=cart.Cart()

#dodajem 3 proizvoda u korpu na slucajan nacin pomocu random-a
c.add_item(random.choice(manager.lista))
c.add_item(random.choice(manager.lista))
c.add_item(random.choice(manager.lista))

#prikaz ukupne vrednosti korpe
c.cart_value()



>>>>>>> add-cart-functionality
