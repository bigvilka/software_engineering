import os
import io
import json
import requests
from models import Note
from config import Config
from flask import Blueprint, request, jsonify


create_notes = Blueprint('create_notes', __name__)


@create_notes.route('', methods=['POST'])
def create():
    title = request.get_json().get('title')
    content = request.get_json().get('content')
    if content:
        note = Note()
        result = note.create_note(title, content)
        return jsonify(result), 201
    else:
        return "", 204