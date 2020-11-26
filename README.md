# REST API with Python, Django REST Framework and Docker using Test Driven Development (TDD)

## Start up
`docker-compose build`

`docker-compose up`

## Admin url
`http://127.0.0.1:8000:/admin/`

## API url
`http://127.0.0.1:8000/api/`

## Run tests
`docker-compose run --rm app sh -c "python manage.py test && flake8"`


## Add admin user
`docker-compose run --rm app sh -c "python manage.py createsuperuser"`

