import os
import io
import json
import requests
from flask import Blueprint, request, jsonify
from models import Note


update_notes = Blueprint('update_notes', __name__)


@update_notes.route('/<id>', methods=['PUT'])
def update(id):
    title = request.get_json().get('title')
    content = request.get_json().get('content')
    if content or title:
        note = Note.objects(id=id).upsert_one(title=title, content=content)
        if not note:
            return "", 400
        note.save()
        return "", 202
    else:
        return "", 204



