from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import product_repository, record_label_repository
from models.record_label import RecordLabel

record_labels_blueprint = Blueprint("record_labels", __name__)

@books_blueprint.route("/record_labels")
def record_labels():
    