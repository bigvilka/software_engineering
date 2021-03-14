import os
import io
import json
import requests
from models import Note
from config import Config
from flask import Blueprint, request, jsonify


delete_notes = Blueprint('delete_notes', __name__)


@delete_notes.route('/<id>', methods=['DELETE'])
def delete(id):
    note = Note.objects(id=id).first()
    if not note:
        return "", 400
    Note.objects(id=id).delete()
    return "", 200