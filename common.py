from pymongo import MongoClient
import os

from services.archive_service import ArchiveService
from services.brew_service import BrewService
from services.warehouse_service import WarehouseService


MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb')
MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
common_client = MongoClient(MONGODB_URL, port=MONGODB_PORT)
common_db = common_client.hub_db

# To be replaced with a service-locator
archive_service = ArchiveService(common_db)
brew_service = BrewService(common_db)
warehouse_service = WarehouseService(common_db)
