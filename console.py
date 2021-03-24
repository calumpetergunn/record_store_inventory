import pdb

from models.product import Product
from models.record_label import RecordLabel

import repositories.product_repository as product_repository
import repositories.record_label_repository as record_label_repository

product_repository.delete_all()
record_label_repository.delete_all()

record_label1 = RecordLabel("Castleface Records", "San Francisco, CA")
record_label_repository.save(record_label1)
record_label2 = RecordLabel("Melted Ice Cream Records", "Christchurch, NZ")
record_label_repository.save(record_label2)
record_label3 = RecordLabel("Flying Nun Records", "Christchurch, NZ")
record_label_repository.save(record_label3)

product1 = Product("Lifetime of Secretion", "Dance Asthmatics", record_label2, "Cassette", "Post-Punk", 15, 8.50, 19.99)
product_repository.save(product1)

product2 = Product("Castlemania", "Thee Oh Sees", record_label1, "LP", "Psychedelic", 25, 9.50, 21.99)
product_repository.save(product2)

product3 = Product("Metalmania", "Salad Boys", record_label2, "CD", "Jangle-Psych", 35, 8.50, 15.99)
product_repository.save(product3)

product4 = Product("Screens", "The Mint Chicks", record_label3, "LP", "Post-Punk", 7, 12.50, 23.99)
product_repository.save(product4)

product5 = Product("Meat Prize", "Team Ugly", record_label2, "Cassette", "Slop-Rock", 10, 5.50, 9.99)
product_repository.save(product5)

product6 = Product("Hubba Bubba", "Damaged Bug", record_label1, "LP", "Synth", 23, 9.50, 19.99)
product_repository.save(product6)

product7 = Product("III", "Milk", record_label3, "LP", "Post-Punk", 14, 6.66, 21.99)
product_repository.save(product7)

product8 = Product("Wammo", "Bailterspace", record_label3, "Cassette", "Noise", 7, 19.50, 22.99)
product_repository.save(product8)

product9 = Product("Welcome to Mediocrity", "BnP", record_label2, "CD", "Harsh Noise", 35, 7.50, 18.99)
product_repository.save(product9)

product10 = Product("Put", "Ben Woods", record_label2, "LP", "Slowcore", 17, 7.20, 16.99)
product_repository.save(product10)

product11 = Product("Live in San Francisco", "Destruction Unit", record_label1, "Cassette", "Rock", 0, 9.50, 21.99)
product_repository.save(product11)


pdb.set_trace()