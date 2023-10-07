from common import brew_service

def api_get_brews():
    # No validation required
    return brew_service.get_brews()
