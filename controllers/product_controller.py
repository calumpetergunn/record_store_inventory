from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import product_repository, record_label_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)