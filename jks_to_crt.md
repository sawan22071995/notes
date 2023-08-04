# Export .crt and .key from .jks

Reference - https://serverfault.com/questions/715827/how-to-generate-key-and-crt-file-from-jks-file-for-httpd-apache-server

```bash
$ keytool -importkeystore -srckeystore mycert.jks -destkeystore keystore.p12 -deststoretype PKCS12
$ openssl pkcs12 -in keystore.p12 -nokeys -out my_key_store.crt
$ openssl pkcs12 -in keystore.p12 -nocerts -nodes -out my_store.key
```

