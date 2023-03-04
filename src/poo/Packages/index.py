from  Packages.user.product import Product
from  Packages.products.user import User


user1 = User()
user1.find()
user1.create()

product1 = Product()
product1.create()
product1.find()