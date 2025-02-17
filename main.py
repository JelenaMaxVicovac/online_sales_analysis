import product
import product_manager

#kreiranje instance klase ProductManager
manager=product_manager.ProductManager()

#kreiranje nekoliko objekata klase Produkt
pr1=product.Product("maramice",250,10)
pr2=product.Product("smoki",75,15)
pr3=product.Product("zvake",135,12)

#dodavanje objekata u listu i prikaz iste
manager.input_product(pr1)
manager.input_product(pr2)
manager.input_product(pr3)

#prikaz proizvoda
manager.display_products()

#prikaz ukupne vrednosti inventara
manager.total_value()
