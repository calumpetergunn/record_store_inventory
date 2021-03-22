from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import product_repository, record_label_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)