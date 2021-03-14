from flask import Blueprint, jsonify, request
from config import Config
import requests
from models import Note

get_notes = Blueprint('get_notes', __name__)


@get_notes.route('', methods=['GET'])
def get_query():
    query = request.args.get('query')
    if query:
        result = []
        notes = Note.objects(title__icontains=query)
        for note in notes:
            if note:
                if not note.title:
                    note.title = note.content[:Config.COUNT_OF_FIRST_N_LETTERS]
                result.append({
                    'id': note.id,
                    'title': note.title,
                    'content': note.content
                })
        notes = Note.objects(content__icontains=query)
        for note in notes:
            if note:
                if not note.title:
                    note.title = note.content[:Config.COUNT_OF_FIRST_N_LETTERS]
                result.append({
                    'id': note.id,
                    'title': note.title,
                    'content': note.content
                })
        if result:
            return jsonify(result)
        else:
            return "", 400
    else:
        notes = Note.objects
        result = []
        for note in notes:
            if not note.title:
                note.title = note.content[:Config.COUNT_OF_FIRST_N_LETTERS]
            result.append({
                'id': note.id,
                'title': note.title,
                'content': note.content
            })
        return jsonify(result)


@get_notes.route('/<id>', methods=['GET'])
def get(id):
    note = Note.objects(id=id).first()
    if not note:
        return "", 400
    if not note.title:
        note.title = note.content[:Config.COUNT_OF_FIRST_N_LETTERS]
    title = note.title
    content = note.content
    return jsonify({
        'id': id,
        'title': title,
        'content': content
    })
