from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import product_repository, record_label_repository
from models.record_label import RecordLabel

record_labels_blueprint = Blueprint("record_labels", __name__)

@record_labels_blueprint.route("/record_labels")
def record_labels():
    record_labels = record_label_repository.select_all()
    return render_template("record_labels/index.html", record_labels = record_labels)

@record_labels_blueprint.route("/record_labels/<id>")
def show(id):
    record_label = record_label_repository.select(id)
    products = record_label_repository.products(record_label)
    return render_template("record_labels/show.html", record_label=record_label, products=products)



    