import pdb

from models.product import Product
from models.record_label import RecordLabel

import repositories.product_repository as product_repository
import repositories.record_label_repository as record_label_repository

product_repository.delete_all()
record_label_repository.delete_all()

record_label1 = RecordLabel("Castleface Records", "San Francisco")
record_label_repository.save(record_label1)
record_label2 = RecordLabel("Melted Ice Cream Records", "Christchurch")
record_label_repository.save(record_label2)

product1 = Product("Lifetime of Secretion", "Dance Asthmatics", record_label2, "Cassette", "Post-Punk", 15, 8.50, 19.99)
product_repository.save(product1)

product2 = Product("Castlemania", "Thee Oh Sees", record_label1, "LP", "Psychedelic", 25, 9.50, 21.99)
product_repository.save(product1)

product3 = Product("Metalmania", "Salad Boys", record_label2, "CD", "Jangle-Rock", 35, 8.50, 15.99)
product_repository.save(product1)

