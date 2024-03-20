# Dummy connector implementation of a CAR connector


Use server UI to modify the model (create/delete/modify Asset model items): http://localhost:8000/admin/
Login credentials are admin/admin

Generate a model of a pre-defined size: http://localhost:8000/admin/assets/assetmodelsize/1/change/
Set the "size" to some number and click "Save" button.


## Connector

Install python dependencies
```
pip3 install -r requirements.txt
```

Running the connector:
```
python3 app.py -car-service-url=http://localhost:3000/api/car/v2 -car-service-key=none -car-service-password=none -source=test

```

## Developer Guide

See the [developer](https://github.com/IBM/cp4s-car-connectors/blob/develop/guide-build-connectors.md) guide for building a new CAR connector.

## Deploy connector in CP4S cluster

