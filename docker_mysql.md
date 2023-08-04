# Install mysql docker on ubuntu

```bash
$ docker pull mysql/mysql-server:latest
```

```bash
$ docker run --name=mysql_strapi_expts -p 3306:3306 -d mysql/mysql-server:latest
```

To view logs

```bash
$ docker logs mysql_strapi_expts
```

Get the root user auto generated password from logs

```bash
$ docker logs mysql_strapi_expts 2>&1 | grep GENERATED
```

Connect to mysql server from with in the container

```bash
$ docker exec -it mysql_strapi_expts mysql -uroot -p
```

Change the root user password by using below command

```bash
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'test1234';
```

Grant all permissions to root

```bash
GRANT ALL PRIVILEGES ON *.* to 'root'@'localhost';
```

Container shell access

```bash
$ docker exec -it mysql_strapi_expts bash
```

start docker container

```bash
$ docker start mysql_strapi_expts
```

stop docker container

```bash
$ docker stop mysql_strapi_expts
```

restart docker container

```bash
$ docker restart mysql_strapi_expts
```

remove container

```bash
$ docker rm mysql_strapi_expts
```







## References

<https://dev.mysql.com/doc/refman/8.0/en/docker-mysql-getting-started.html>

<https://medium.com/@dilsimchandrasena/how-to-deploy-and-use-a-mysql-docker-container-in-ubuntu-4ace7c893982>

