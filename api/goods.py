from common import warehouse_service

def api_get_goods():
    # No validation required
    return warehouse_service.get_goods()
