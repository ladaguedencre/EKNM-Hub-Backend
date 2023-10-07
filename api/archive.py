from dataclasses import dataclass, asdict
from typing import List
from common import archive_service
from flask import abort


def api_get_article(arg: any):
    if not arg is str:
        abort(400)
    article = archive_service.get_article(id)
    if not article:
        abort(404)
    return article 

def api_get_bindings():
    # No validation required
    return archive_service.get_bindings()
