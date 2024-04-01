from flask import Blueprint, request, jsonify
from myapp import db
from myapp.models import TestTable
from myapp.models import WebpageInfo
bp = Blueprint('views', __name__)

@bp.route('/add', methods=['GET'])
def add_record():
    name = request.args.get('name')
    record = TestTable(name=name)
    db.session.add(record)
    db.session.commit()
    return jsonify({'id': record.id, 'name': record.name}), 200

@bp.route('/get', methods=['GET'])
def get_record():
    id = request.args.get('id')
    record = TestTable.query.get(id)


    if record:
        return jsonify({'id': record.id, 'name': record.name}), 200
    else:
        return jsonify({'error': 'Record not found'}), 404


@bp.route('/update', methods=['POST'])
def update_record():
    id = request.form.get('id')
    name = request.form.get('name')
    record = TestTable.query.get(id)
    if record:
        record.name = name
        db.session.commit()
        return jsonify({'id': record.id, 'name': record.name}), 200
    else:
        return jsonify({'error': 'Record not found'}), 404

@bp.route('/delete', methods=['POST'])
def delete_record():
    id = request.form.get('id')
    record = TestTable.query.get(id)

    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify({'success': 'Record deleted'}), 200
    else:
        return jsonify({'error': 'Record not found'}), 404

# from flask import jsonify, request

@bp.route('/webpage_info', methods=['GET'])
def get_webpage_info():
    # 默认的页数为1，每页的数量为10
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    pagination = WebpageInfo.query.paginate(page=page, per_page=per_page)
    webpage_infos = pagination.items

    results = []

    if webpage_infos:
        for webpage_info in webpage_infos:
            results.append({
                "id": webpage_info.id,
                "website_url": webpage_info.website_url,
                "title": webpage_info.title,
                "h1_titles": webpage_info.h1_titles,
                "distinct_link_domains": webpage_info.distinct_link_domains,
                "screenshot_path": webpage_info.screenshot_path,
                "minio_path": webpage_info.minio_path,
            })

        data = {
            "webpage_infos": results,
            "total_pages": pagination.pages,
            "current_page": pagination.page,
            "total_items": pagination.total,
        }

        return jsonify(data)
    else:
        return jsonify({"error": "No webpage info found"}), 404