# pylint: disable=too-few-public-methods
import abc
import smtplib
from interface import config


class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


class Defectc:
    def __init__(self, type, location, severity):
        self.type = type
        self.location = location
        self.severity = severity


class Product:
    def __init__(self, id, name, measurements):
        self.id = id
        self.name = name
        self.measurements = measurements
        self.defects = []

    def add_defect(self, defect):
        self.defects.append(defect)


class ProductionLine:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)


class QualityAssurance:
    def __init__(self, production_line, date, inspector):
        self.production_line = production_line
        self.date = date
        self.inspector = inspector
        self.defects = []

    def add_defect(self, defect):
        self.defects.append(defect)
