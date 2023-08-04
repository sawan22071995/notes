# Vysor in Ubuntu

## References

https://github.com/koush/vysor.io/issues/242

https://app.vysor.io/#/ - Progressive web app

```bash
# exit vysor first
$ sudo apt install adb
$ adb kill-server
$ adb start-server
# verify your device is listed now. You may see a permission error.
$ adb devices
```

