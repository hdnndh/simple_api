# Sample API - Docker, Flask, Marshmallow, SQLAlchemy

   This project is a **dockerized**, meant to develop a portalbe **workspace** and **deployment** container for sample serverside code written in **Flask** and with **SQlite3** backend with GPU-ready docker
   
## Introduction
* **Dependencies:**
	* Python 3.7
	* Flask
	* Connexion
	* SQLite3
	* SQLAlchemy
	* Marshmallow

## Run
* To build the docker image :
```sh
./BUILD
```
* To start the docker:
```sh
./1_server
```
* To start the server code (inside the docker container):
```sh
cd /sharedVolume && python3 serv.py
```
* Then you can start sending packet to 0.0.0.0:5000, e.g:
```sh
curl --location --request GET 'http://0.0.0.0:5000/api/report?from=1&to=70' \
--header 'Content-Type: application/json' \
--data-raw '{
    "date": 1,
    "fruits": {
        "mango": 5,
        "orange": 6
    }
}'
```
* Or access API documentation at http://0.0.0.0:5000/api/ui/.
* To rebuild sample db:
```sh
python3 sampledb.py 
```
* To print db in beautified format:
```sh
python3 printall.py 
```
## What can this project do?

* setup a basic server-side code and db structure.
* Help making dev env easider with sharedVolume structure

## License
MIT LICENSE
