**Project based in API REST - PYTHON/DJANGO**

- API that can register and associated vessels and equipments. It also has the functionality to inactivate equipments.

---

# VESSEL API REST 

The main functionalities of this API are:

1. Registering a vessel. The vessel data input is its code, which can’t be repeated (return the HTTP code appropriate and an error message if the user tries to register a existing code).
2. Registering a new equipment in a vessel. The data inputs of each equipment are name, code, location and status. Each equipment is associated to a given vessel and has a unique code, which can’t be repeated (return the HTTP code appropriate and an error message if the user tries to register a existing code). For each new equipment registered, the equipment status is automatically active.
3. Setting an equipment’s status to inactive. The input data should be one or a list of equipment code.
4. Returning all active equipment of a vessel.

---

## Swagger

This API uses Swagger as a documentation tool.

* In this project the root is redirecting to this swagger documentation endpoint. It can be accessed in http://localhost:8000/ 

---

## Endpoints

If you rather use Postman to test the endpoints, they are listed below:

1. **(GET)** **_"/vessels/"_** - *Returns all vessels registered.*
2. **(POST)** **_"/vessels/"_** - *Register new vessel.*
3. **(GET)** **_"/vessels/{code}/"_** - *Returns an especific vessel.*
4. **(DELETE)** **_"/vessels/{code}/"_** - *Delete a vessel.*
5. **(GET)** **_"/vessels/{vessel_pk}/equipments/"_** - *Returns all equipments associated to a specific vessel.*
6. **(POST)** **_"/vessels/{vessel_pk}/equipments/"_** - *Register new equipment.*
7. **(GET)** **_"/vessels/{vessel_pk}/equipments/active_equipments/"_** - *Returns all active equipments associated to a specific vessel.*
8. **(DELETE)** **_"/vessels/{vessel_pk}/equipments/{code}/"_** - *Delete an equipment associated to a vessel.*
9. **(POST)** **_"/inactivate-equipments/"_** - *Change status of an equipment or a list of equipments to inactive.*

_This last method is a POST method instead of a PUT or PATCH because it can update a single equipment or a list of equipments. For example, you can send in the request's body:_

```
{"code": "MV100"}

or

[
  {
    "code": "MV100"
  },
  {
    "code": "MV101"
  }
]
```

---

## Utils

I've created 15 Makefile commands to use in this project. However, you'll just need to use 5 of them to run locally:

* **_make setup_**: To set up the entire environment to run the project. Only need to use this command once.
* **_make start_**: Create the project's container and run the project.
* **_make stop_**: Stop the project's container.
* **_make tests_**: Run all tests in the project.
* **_make clean_**: Clean this project's containers, image, volumes and network from your computer. It's recommended to read this Makefile command before you use it, to make sure that you do not have other projects with similar names.

---

## Django Admin

All API functionalities were also registered on the Django Admin. Small customizations were made in the admin to make it better:

* A placeholder was inserted on the Vessel's list search box.
* A placeholder was inserted on the Equipment's list search box.
* Equipments filtered by status.
* Equipments listed by: code, status, name and vessel code.
* Option to activate selected equipments on django actions button.
* Option to inactivate selected equipments on django actions button.

_To make it easy to analyse this project... when the project runs for the first time, one super user is automatically created (username:admin, password:vessel1234). You'll have to use this user to access this admin area. If you'ld like, you can create your own super user with the "make createsuperuser" command and delete the previous one in the Django admin._

_Django's admin can be accessed in:_ http://localhost:8000/admin/

---

## Run Locally


1. Make sure you have the Docker and Docker-compose installed.
2. You'll also need to generate one Django **SECRET KEY** and insert it in the **_develop.env_** file. I've already inserted a random secret key in the file, however is highly recommended to change it by a new one. (The key can be generated here: https://djecrety.ir/)
3. In the first time running the project (and just in the first one) you will have to use the command _make setup_ to create the project's image.
4. Then, use _make start_ to run it locally. Next time, you will just have to use _make start_ and _make stop_ commands.
5. This project runs in: http://localhost:8000/

---

## Tests

There are ten tests being tested in this project. The characteristics of this tests can be readden below:

1. Almost every endpoint is tested once. 
2. The exception is the **"/inactivate-equipments/"** endpoint. This one is tested two times. In the first one, a single code is sent in the body's requisition. In the second one, a list is sent.
3. There is a specific command to run the tests (**_make tests_**). However, the tests also runs when it's necessary to build the project's image. 

---

## Requirements

* **DOCKER-COMPOSE**: 1.27.4
* **DOCKER**: 19.03.13

