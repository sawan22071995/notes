# Stapi related notes

### To connect strapi with mysql

```bash
$ npm install sails-mysql
```

```bash
$ npm install strapi-connector-bookshelf
```



Connecting to multiple databases

database.json should have something like below

```
{
  "defaultConnection": "default",  
  "connections": {
    "default": {
      "connector": "mongoose",
      "settings": {
        "database": "strapi_db",
        "host": "localhost",
        "srv": false,
        "port": 27017,
        "username": "strapi_admin",
        "password": "test1234"
      },
      "options": {
        "authenticationDatabase": "admin"
      }
    },
    "mysql":{
      "connector": "bookshelf",
      "settings": {
        "client": "mysql",
        "database": "strapi_expts",
        "host": "localhost",
        "port": 3306,
        "username": "dev_user",
        "password": "pass"
      },
      "options": {
      }
    }
  }
}

```



