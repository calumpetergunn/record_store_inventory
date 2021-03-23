from db.run_sql import run_sql
import repositories.record_label_repository as record_label_repository
from models.product import Product
from models.record_label import RecordLabel



def save(product):
    sql = """
        INSERT INTO products (title, artist, record_label_id, format, genre, quantity, buy_cost, sell_price) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    """
    values = [product.title, product.artist, product.record_label.id, product.format, product.genre, product.quantity, product.buy_cost, product.sell_price]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        record_label = record_label_repository.select(row['record_label_id'])
        product = Product(row['title'], row['artist'], record_label, row['format'], row['genre'], row['quantity'], row['buy_cost'], row['sell_price'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        record_label = record_label_repository.select(result['record_label_id'])
        product = Product(result['title'], result['artist'], record_label, result['format'], result['genre'], result['quantity'], result['buy_cost'], result['sell_price'], result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (title, artist, record_label_id, format, genre, quantity, buy_cost, sell_price) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.title, product.artist, product.record_label.id, product.format, product.genre, product.quantity, product.buy_cost, product.sell_price, product.id]
    run_sql(sql, values)
