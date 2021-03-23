from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import product_repository, record_label_repository
from models.record_label import RecordLabel
from models.product import Product

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

@record_labels_blueprint.route("/record_labels/new", methods=['GET'])
def new_record_label():
    products = product_repository.select_all()
    record_labels = record_label_repository.select_all()
    return render_template("record_labels/new.html", title = "Add Record Label", products=products, record_labels=record_labels)

@record_labels_blueprint.route("/record_labels", methods=['POST'])
def create_record_label():
    name = request.form['name']
    location = request.form['location']
    record_label = RecordLabel(name, location)
    record_label_repository.save(record_label)
    return redirect("/record_labels")

@record_labels_blueprint.route("/record_labels/<id>/delete", methods=["POST"])
def delete_record_label(id):
    record_label_repository.delete(id)
    return redirect("/record_labels")

@record_labels_blueprint.route("/record_labels/<id>/edit", methods=['GET'])
def edit_record_label(id):
    record_label = record_label_repository.select(id)
    return render_template("record_labels/edit.html", title = "Edit Record Label", record_label=record_label)

@record_labels_blueprint.route("/record_labels/<id>", methods=['POST'])
def update_record_label(id):
    name = request.form['name']
    location = request.form['location']
    record_label = RecordLabel(name, location, id)
    record_label_repository.update(record_label)
    return redirect("/record_labels")





    