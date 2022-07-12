from crypt import methods
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin, CORS
from src.database import Bookmark, db

bookmarks = Blueprint("bookmarks", __name__, url_prefix='/api/v1/bookmarks')
CORS(bookmarks, supports_credentials=True)

@cross_origin(origins='*',methods=['POST','OPTIONS'])
@bookmarks.route('/new', methods=['POST','OPTIONS'])
@jwt_required()
def add_bookmark():
    if request.method == 'OPTIONS':
        return jsonify({"msg":"success"}), 200
    data = request.get_json()
    title = data.get('title')
    url = data.get('url')
    body = data.get('body')
    icon = data.get('icon')
    category = data.get('category')
    user_id = get_jwt_identity()
    try:
        bookmark = Bookmark(title=title,url=url,body=body,icon=icon,category=category,user_id=user_id)
        if bookmark:
            db.session.add(bookmark)
            db.session.commit()
            return jsonify({
            "message": "bookmark created"
        }), 201
    except Exception:
        return jsonify({
            "error":"error saving bookmark"
        }), 500
    else:
        return jsonify({
            "error":"error saving bookmark"
        }), 500
        

@cross_origin(methods=['DELETE','OPTIONS'])
@bookmarks.route('/remove', methods=['DELETE',])
@jwt_required()
def remove_bookmark():
    if request.method == 'OPTIONS':
        return jsonify({"msg":"success"}), 200
    data = request.get_json()
    id = data.get("id")
    try:
        bookmark = Bookmark.query.filter_by(id=id).first()
        if bookmark:
            db.session.delete(bookmark)
            db.session.commit()
            return jsonify({
                "mesage":"bookmark deleted"
            }), 200
        return jsonify({
            "error":"error deleting bookmark"
        }), 500
    except Exception:
        return jsonify({
            "error": "error deleting bookmark"
        }), 500

@cross_origin(methods=['GET','OPTIONS'])
@bookmarks.route('/my_bookmarks')
@jwt_required()
def get_bookmarks():
    if request.method == 'OPTIONS':
        return jsonify({"msg":"success"}), 200
    user_id = get_jwt_identity()
    bookmarksList = []
    try:
        bookmarks = Bookmark.query.filter_by(user_id=user_id).all()
        if bookmarks:
            for book in bookmarks:
                my_obj = {
                    "title":book.title,
                    "id": book.id,
                    "body":book.body,
                    "url":book.url,
                    "icon":book.icon
                }
                bookmarksList.append(my_obj)
            return jsonify({
                "bookmarks":bookmarksList
            }), 200
        return jsonify({
            "bookmarks": bookmarksList
        }), 200
    except Exception:
        return jsonify({
            "error":"failed to fetch bookmarks"
        }), 500


