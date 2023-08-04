# MySQL Commands

1. Root user is not allowed to connect from outside the container. So we need to create a user and then connect workbench through that user or we need to remove the security

Take a look at docker_mysql.md file on how to get into mysql shell

```bash
mysql> create user 'admin'@'%' identified by 'pass';
```

```bash
mysql> grant all privileges on *.* to 'admin'@'%' with grant option;
```

```bash
mysql> select host, user from mysql.user;
```

```bash
mysql> flush privileges;
```
