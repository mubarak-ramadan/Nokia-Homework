
### Meal service rendered by FastAPI, Postgresql, docker and Kubernetes

* FastAPI app to store meals
* Postgresql with SQLAlchemy
* containerized with Docker



### How to run this app

* Ensure you have docker installed and running on your machine

* in the terminal (Ensure you are in the right direectory where the app is located because the .yaml files must be present in the directory)

'''
run the following command

docker-compose up --build

'''


### Testing

* There is a unit test file where all the tests are written

* But one good thing about FastAPI is that it provides a nice interface for testiing the API services

* To easily test the app go to localhost/docs

* The endpoints can be tested easily and more interactively there.