from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import product_repository, record_label_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product=product)


@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    products = product_repository.select_all()
    record_labels = record_label_repository.select_all()
    return render_template("products/new.html", products=products, record_labels=record_labels)

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    record_label_id = request.form['record_label_id']
    title = request.form['title']
    artist = request.form['artist']
    record_label = record_label_repository.select(record_label_id)
    format = request.form['format']
    genre = request.form['genre']
    quantity = request.form['quantity']
    buy_cost = request.form['buy_cost']
    sell_price = request.form['sell_price']
    product = Product(title, artist, record_label, format, genre, quantity, buy_cost, sell_price)
    product_repository.save(product)
    return redirect("/products")

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")


@products_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select(id)
    record_labels = record_label_repository.select_all()
    return render_template("/products/edit.html", title = "Edit Product", product=product, record_labels=record_labels)

@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    title = request.form['title']
    artist = request.form['artist']
    record_label = record_label_repository.select(request.form['record_label_id'])
    format = request.form['format']
    genre = request.form['genre']
    quantity = request.form['quantity']
    buy_cost = request.form['buy_cost']
    sell_price = round(float(request.form['sell_price']) * float(request.form['on_sale']),2)
    product = Product(title, artist, record_label, format, genre, quantity, buy_cost, sell_price, id)
    product_repository.update(product)
    return redirect("/products")