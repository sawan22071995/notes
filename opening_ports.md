# Opening ports in Ubuntu

```bash
# displays all current rules
$ sudo ufw status verbose 

# to allow 22
$ sudo ufw allow 22/tcp

# if ufw is not enabled. But allow 22 before you enable if you are working on remote server
$ sudo ufw enable

# allow specific ip to access specific port
$ sudo ufw allow from <ip address> to any port <port number> proto tcp

# allow specific IP to access on any port
$ sudo ufw allow from <ip address> to any proto tcp
```

