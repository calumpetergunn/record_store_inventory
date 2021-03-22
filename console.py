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

product3 = Product("Metalmania", "Salad Boys", record_label2, "CD", "Jangle-Rock", 35, 8.50, 15.99)
product_repository.save(product3)

product4 = Product("Screens", "The Mint Chicks", record_label3, "LP", "Post-Punk", 7, 12.50, 23.99)
product_repository.save(product4)

product5 = Product("Meat Prize", "Team Ugly", record_label2, "Cassette", "Slop-Rock", 10, 5.50, 9.99)
product_repository.save(product5)

product6 = Product("Hubba Bubba", "Damaged Bug", record_label1, "LP", "Synth", 23, 9.50, 19.99)
product_repository.save(product6)


pdb.set_trace()