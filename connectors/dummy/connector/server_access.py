import requests, base64
import json
import os

from car_framework.context import context
from car_framework.util import DatasourceFailure
from car_framework.server_access import BaseAssetServer


class AssetServer(BaseAssetServer):

    def __init__(self):
        pass

    def test_connection(self):
        try:
            self.get_collection('xrefproperties')
            code = 0
        except DatasourceFailure as e:
            context().logger.error(e)
            code = 1
        return code

    # Get entity for the specific id cached
    def get_object(self, url):
        asset_id = int(url.rstrip('/').split('/')[-1])
        asset = self.get_collection("assets")
        for item in asset:
            if item['pk'] == asset_id:
                return item

    # Get list of entities as per the identifiers passed.
    def get_objects(self, asset_server_endpoint, ids):
        data = []
        ip_address = self.get_collection(asset_server_endpoint)
        for id in ids:
            for item in ip_address:
                if item['pk'] == id:
                    data.append(item)
        
        return data
                     

    # Pulls asset data for all collection entities
    def get_collection(self, asset_server_endpoint):

        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, "asset_files", f"{asset_server_endpoint}.json")

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


    # To get the save point in data source. If data source doesn't have it then this function can be deleted.
    def get_model_state_id(self):
        return None

    # This function has logic to gather all information required to pull data between two save points
    def get_model_state_delta(self, last_model_state_id, new_model_state_id):
        return None

