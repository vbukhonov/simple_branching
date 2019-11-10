# simple_branching
Simple app for showing the interaction of branches and employees.

In order to create new Branch or new Employee, use /admin/ part.

For the Branches you can use Google Maps to select coordinates.
 Access to the coordinates editing is controlled with the permission "edit_coordinates".

You can check the list of objects and details of each object.

You can get the branch which is closest to the selected coordinates by going to the following url:

```
/branches/{LAT}/{LNG}/
```

where `LAT` and `LNG` are Decimal numbers with max 9 digits and 6 decimal palces.

You can get list of employees filtered by branch name and/or ordered by first name, last name, position or branch name
 by using the following url:

```
/employees/?branch_name={BRANCH_NAME}&order_by_fields=first_name,last_name,branch__name
```

There are 10 mock Branches and 10 000 mock Employees which can be added via migrations.

For dockerization check Dockerfile, docker-compose.yml and .env.dev files.

In order to start the app, you will need to set the following environment variables:

```
USE_S3
DJANGO_SETTINGS_MODULE
DB_USER
DB_PASSWORD
SECRET_KEY
DEBUG (default is True)
ALLOWED_HOSTS
SQL_USER
SQL_PASSWORD
SQL_DB
SQL_HOST (default is `localhost`)
SQL_PORT (default is `5432`)
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME
GOOGLE_MAPS_API_KEY
```
