import sys, argparse, traceback, os

from car_framework.context import context
from car_framework.app import BaseApp
from car_framework.extension import SchemaExtension

from connector.server_access import AssetServer
from connector.full_import import FullImport
from connector.inc_import import IncrementalImport


version = '1.0.1'


class App(BaseApp):
    def __init__(self):
        super().__init__('This script is used for pushing asset data to CP4S CAR ingestion microservice')
        self.parser.add_argument('-host', dest='CONNECTION_HOST', default=os.getenv('CONNECTION_HOST',None), type=str, required=False, help='The url of the Asset data')

    def setup(self):
        super().setup()
        context().asset_server = AssetServer()
        context().full_importer = FullImport()
        context().inc_importer = IncrementalImport()
    
    def get_schema_extension(self):

        # The following extension adds "site" vertex collection, "site_asset" edge collection and adds "initial_value" field to "asset" collection

        return SchemaExtension(
            key = 'c06ec385-0abc-4646-9c71-5c7a1ab8b1ad',   # generate your own UUID key!
            owner = 'Reference Connector',
            version = '1',
            schema = '''
            {
                "vertices": [
                    {
                    "name": "site",
                    "properties": {
                        "name": {
                        "description": "name",
                        "type": "text",
                        "indexed": true,
                        "required": true,
                        "default": ""
                        },
                        "address": {
                        "description": "address",
                        "type": "text",
                        "required": true,
                        "default": ""
                        }
                      }
                    },
                    {
                        "name": "asset",
                        "properties": {
                            "initial_value": {
                                "type": "numeric"
                            }
                        }
                    }
                ],
                "edges": [
                    { "end1": "site", "end2": "asset" }
                ]
            }
            '''
        )

app = App()
app.setup()
app.run()