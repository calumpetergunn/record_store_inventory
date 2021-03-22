from db.run_sql import run_sql

from models.record_label import RecordLabel
from models.product import  Product

def save(record_label):
    sql = "INSERT INTO record_labels (name, location) VALUES (%s, %s) RETURNING *"
    values = [record_label.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    record_label.id = id
    return record_label

def select_all():
    record_labels = []

    sql = "SELECT * FROM record_labels"
    results = run_sql(sql)

    for row in results:
        record_label = RecordLabel(row['name'], row['location'], row['id'])
        record_labels.append(record_label)
    return record_labels

def select(id):
    record_label = None
    sql = "SELECT * FROM record_labels WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        record_label = RecordLabel(result['name'], result['location'], result['id'])
    return record_label

def delete_all():
    sql = "DELETE FROM record_labels"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM record_labels WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(record_label):
    sql = "UPDATE record_labels SET (name, location) = (%s, %s) WHERE id = %s"
    values = [record_label.name, record_label.location, record_label.id]
    run_sql(sql, values)

def products(record_label):
    products = []

    sql = "SELECT * FROM products WHERE record_label_id = %s"
    values = [record_label.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['title'], row['artist'], row['record_label_id'], row['format'], row['genre'], row['quantity'], row['buy_cost'], row['sell_price'], row['id'])
        products.append(product)
    return products
