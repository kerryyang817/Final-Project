
from flask import Flask, jsonify, request
from interface.adapters.repository import QualityAssuranceRepository

app = Flask(__name__)
repo = QualityAssuranceRepository()

# endpoint for getting all quality assurance data


@app.route('/quality-assurance', methods=['GET'])
def get_quality_assurance_data():
    quality_assurance_data = repo.get_inspections()
    return jsonify(quality_assurance_data)

# endpoint for getting quality assurance data for a specific product


@app.route('/quality-assurance/<product_id>', methods=['GET'])
def get_quality_assurance_data_for_product(product):
    quality_assurance_data = repo.get_inspections_for_product(
        product)
    if quality_assurance_data:
        return jsonify(quality_assurance_data)
    else:
        return jsonify({'error': 'Product not found.'}), 404

# endpoint for adding new quality assurance data


@app.route('/quality-assurance', methods=['POST'])
def add_quality_assurance_data():
    new_data = request.get_json()
    result = repo.add_inspection(new_data)
    if result:
        return jsonify({'success': 'Data added successfully.'}), 201
    else:
        return jsonify({'error': 'Failed to add data.'}), 400

# endpoint for updating quality assurance data for a specific product


@app.route('/quality-assurance/<product_id>', methods=['PUT'])
def update_quality_assurance_data_for_product(product_id):
    updated_data = request.get_json()
    result = repo.update_inspections_for_product(
        product_id, updated_data)
    if result:
        return jsonify({'success': 'Data updated successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to update data.'}), 400

# endpoint for deleting quality assurance data for a specific product


@app.route('/quality-assurance/<product_id>', methods=['DELETE'])
def delete_quality_assurance_data_for_product(product_id):
    result = repo.delete_quality_assurance_data_for_product(product_id)
    if result:
        return jsonify({'success': 'Data deleted successfully.'}), 200
    else:
        return jsonify({'error': 'Failed to delete data.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
