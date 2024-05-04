from flask import request, jsonify
from app import app, db
from app.models import Asset, AssetDependency

@app.route('/assets', methods=['POST'])
def add_asset():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    userId = data.get('userId')
    name = data.get('name')
    description = data.get('description')
    status = data.get('status')
    lifetime = data.get('lifetime')

    if not userId or not name or not description or not status or not lifetime:
        return jsonify({'error': 'Missing data'}), 400

    new_asset = Asset(userId=userId, name=name, description=description, status=status, lifetime=lifetime)
    db.session.add(new_asset)
    db.session.commit()

    return jsonify({
        'id': new_asset.id,
        'name': new_asset.name,
        'description': new_asset.description,
        'status': new_asset.status,
        'lifetime': new_asset.lifetime
    }), 201


@app.route('/assets/<string:id>', methods=['DELETE'])
def delete_asset(id):
    asset = Asset.query.filter_by(id=id).first()
    if not asset:
        return jsonify({'error': 'Asset not found'}), 404
    
    db.session.delete(asset)
    db.session.commit()

    return jsonify({'message': 'Asset has been deleted successfully'})


@app.route('/assets/<string:id>', methods=['PUT'])
def update_asset(id):
    data = request.json
    asset = Asset.query.filter_by(id=id).first()
    if not asset:
        return jsonify({'error': 'Asset not found'}), 404
    
    name = data.get('name')
    description = data.get('description')
    status = data.get('status')
    lifetime = data.get('lifetime')

    if name is not None:
        asset.name = name
    if description is not None:
        asset.description = description
    if status is not None:
        asset.status = status
    if lifetime is not None:
        asset.lifetime = lifetime

    db.session.commit()

    return jsonify({
        'id': asset.id,
        'name': asset.name,
        'description': asset.description,
        'status': asset.status,
        'lifetime': asset.lifetime
    }), 201


@app.route('/assets/<string:id>/dependencies', methods=['POST'])
def add_dependency(id):
    data = request.json
    asset = Asset.query.filter_by(id=id).first()
    if not asset:
        return jsonify({'error': 'Asset not found'}), 404
    
    name = data.get('name')
    description = data.get('description')
    status = data.get('status')
    value = data.get('value')
    lifetime = data.get('lifetime')

    if not name or not description or not status or not value or not lifetime:
        return jsonify({'error': 'Missing data'}), 400

    new_dependency = AssetDependency(assetId=asset.id, name=name, description=description, status=status, value=value, lifetime=lifetime)
    db.session.add(new_dependency)
    db.session.commit()

    return jsonify({
        'id': new_dependency.id,
        'assetId': new_dependency.assetId,
        'name': new_dependency.name,
        'description': new_dependency.description,
        'status': new_dependency.status,
        'value': new_dependency.value,
        'lifetime': new_dependency.lifetime
    }), 201


@app.route('/assets/<string:id>/dependencies/<string:dep_id>', methods=['DELETE'])
def delete_dependency(id, dep_id):
    asset = Asset.query.filter_by(id=id).first()
    if not asset:
        jsonify({'error': 'Asset not found'}), 404
    
    dependency = AssetDependency.query.filter_by(id=dep_id).first()
    if not dependency:
        jsonify({'error': 'Dependency not found'}), 404

    db.session.delete(dependency)
    db.session.commit()

    return jsonify({'message': 'Dependency deleted successfully'})


@app.route('/assets/<string:id>/dependencies/<string:dep_id>', methods=['PUT'])
def update_dependency(id, dep_id):
    data = request.json
    asset = Asset.query.filter_by(id=id).first()
    if not asset:
        jsonify({'error': 'Asset not found'}), 404

    dependency = AssetDependency.query.filter_by(id=dep_id).first()
    if not dependency:
        return jsonify({'error': 'Dependency not found'}), 404
    
    name = data.get('name')
    description = data.get('description')
    status = data.get('status')
    value = data.get('value')
    lifetime = data.get('lifetime')  

    if name is not None:
        dependency.name = name
    if description is not None:
        dependency.description = description
    if status is not None:
        dependency.status = status
    if value is not None:
        dependency.value = value
    if lifetime is not None:
        dependency.lifetime = lifetime

    db.session.commit()

    return jsonify({
        'id': dependency.id,
        'name': dependency.name,
        'description': dependency.description,
        'status': dependency.status,
        'value': dependency.value,
        'lifetime': dependency.lifetime
    }), 201



# Listagem    
@app.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    if not assets:
        return jsonify({'error': 'No assets found'}), 404
    
    result = []
    for asset in assets:
        asset_data = {
            'id': asset.id,
            'userId': asset.userId,
            'name': asset.name,
            'description': asset.description,
            'status': asset.status,
            'lifetime': asset.lifetime
        }
        result.append(asset_data)
    
    return jsonify(result)


@app.route('/assets/<string:id>/dependencies', methods=['GET'])
def get_dependencies(id):
    asset = Asset.query.filter_by(id=id).first()
    if not asset:
        return jsonify({'error': 'Asset not found'}), 404

    dependencies = AssetDependency.query.filter_by(assetId=id).all()
    if not dependencies:
        return jsonify({'error': 'No dependencies found for this asset'}), 404

    result = []
    for dependency in dependencies:
        dependency_data = {
            'id': dependency.id,
            'assetId': dependency.assetId,
            'name': dependency.name,
            'description': dependency.description,
            'status': dependency.status,
            'value': dependency.value,
            'lifetime': dependency.lifetime
        }
        result.append(dependency_data)

    return jsonify(result)