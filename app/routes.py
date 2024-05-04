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
    nextMaintenance = data.get('nextMaintenance')
    value = data.get('value')
    dependencies = data.get('dependencies')

    if not userId or not name or not description or not status or not nextMaintenance or not value:
        return jsonify({'error': 'Missing data'}), 400

    new_asset = Asset(userId=userId, name=name, description=description, status=status, nextMaintenance=nextMaintenance, value=value)
    db.session.add(new_asset)
    db.session.commit()

    if dependencies:
        for dependency_data in dependencies:
            dependency_name = dependency_data.get('name')
            dependency_description = dependency_data.get('description')
            dependency_status = dependency_data.get('status')
            dependency_value = dependency_data.get('value')
            dependency_next_maintenance = dependency_data.get('nextMaintenance')

            if not dependency_name or not dependency_description or not dependency_status or not dependency_value or not dependency_next_maintenance:
                return jsonify({'error': 'Missing dependency data'}), 400

            new_dependency = AssetDependency(assetId=new_asset.id, name=dependency_name, description=dependency_description, status=dependency_status, value=dependency_value, nextMaintenance=dependency_next_maintenance)
            db.session.add(new_dependency)
            
    db.session.commit()

    return jsonify({
        'id': new_asset.id,
        'name': new_asset.name,
        'description': new_asset.description,
        'status': new_asset.status,
        'nextMaintenance': new_asset.nextMaintenance,
        'value': new_asset.value
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
    nextMaintenance = data.get('nextMaintenance')
    value = data.get('value')

    if name is not None:
        asset.name = name
    if description is not None:
        asset.description = description
    if status is not None:
        asset.status = status
    if nextMaintenance is not None:
        asset.nextMaintenance = nextMaintenance
    if value is not None:
        asset.value = value

    db.session.commit()

    return jsonify({
        'id': asset.id,
        'name': asset.name,
        'description': asset.description,
        'status': asset.status,
        'nextMaintenance': asset.nextMaintenance,
        'value': asset.value
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
    nextMaintenance = data.get('nextMaintenance')

    if name is not None:
        dependency.name = name
    if description is not None:
        dependency.description = description
    if status is not None:
        dependency.status = status
    if value is not None:
        dependency.value = value
    if nextMaintenance is not None:
        dependency.nextMaintenance = nextMaintenance

    db.session.commit()

    return jsonify({
        'id': dependency.id,
        'assetId': dependency.assetId,
        'name': dependency.name,
        'description': dependency.description,
        'status': dependency.status,
        'value': dependency.value,
        'nextMaintenance': dependency.nextMaintenance
    }), 201



# List
@app.route('/assets/<string:user_id>', methods=['GET'])
def get_assets(user_id):
    assets = Asset.query.filter_by(userId=user_id).all()
    if not assets:
        return jsonify({'error': 'No assets found for this user'}), 404
    
    result = []
    for asset in assets:
        asset_data = {
            'id': asset.id,
            'userId': user_id,
            'name': asset.name,
            'description': asset.description,
            'status': asset.status,
            'nextMaintenance': asset.nextMaintenance,
            'value': asset.value,
            'dependencies': []
        }

        dependencies = AssetDependency.query.filter_by(assetId=asset.id).all()
        for dependency in dependencies:
            dependency_data = {
                'id': dependency.id,
                'name': dependency.name,
                'description': dependency.description,
                'status': dependency.status,
                'nextMaintenance': dependency.nextMaintenance,
                'value': dependency.value
            }
            asset_data['dependencies'].append(dependency_data)
        
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
            'nextMaintenance': dependency.nextMaintenance
        }
        result.append(dependency_data)

    return jsonify(result)