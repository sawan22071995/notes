# Switching python versions

1. List all the installed versions

    ```bash
    => ~ ls -l /usr/bin/python*
    lrwxrwxrwx 1 root root       9 Sep 23 10:18 /usr/bin/python -> python2.7
    lrwxrwxrwx 1 root root       9 Sep 23 10:18 /usr/bin/python2 -> python2.7
    -rwxr-xr-x 1 root root 3617176 Sep 24 00:06 /usr/bin/python2.7
    lrwxrwxrwx 1 root root       9 Oct 10 08:00 /usr/bin/python3 -> python3.6
    -rwxr-xr-x 2 root root 4568920 Oct  3 23:45 /usr/bin/python3.6
    -rwxr-xr-x 2 root root 4568920 Oct  3 23:45 /usr/bin/python3.6m
    lrwxrwxrwx 1 root root      10 Oct 10 08:00 /usr/bin/python3m -> python3.6m
    ```

2. You can switch by creating alias (This will change only for the current user)

    1. have the following line in ~/.bashrc

        ```bash
        alias python='/usr/bin/python3'
        ```

    2. Source ~/.bashrc

        ```bash
        $ source ~/.bashrc
        ```

3. By using update-alternatives (for all users)

    ```bash
    => ~ update-alternatives --list python
    update-alternatives: error: no alternatives for python
    ```

    ```bash
    => ~ ls -l /usr/bin/python*
    lrwxrwxrwx 1 root root       9 Sep 23 10:18 /usr/bin/python -> python2.7
    lrwxrwxrwx 1 root root       9 Sep 23 10:18 /usr/bin/python2 -> python2.7
    -rwxr-xr-x 1 root root 3617176 Sep 24 00:06 /usr/bin/python2.7
    lrwxrwxrwx 1 root root       9 Oct 10 08:00 /usr/bin/python3 -> python3.6
    -rwxr-xr-x 2 root root 4568920 Oct  3 23:45 /usr/bin/python3.6
    -rwxr-xr-x 2 root root 4568920 Oct  3 23:45 /usr/bin/python3.6m
    lrwxrwxrwx 1 root root      10 Oct 10 08:00 /usr/bin/python3m -> python3.6m
    ```

    ```bash
    => ~ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
    update-alternatives: using /usr/bin/python2.7 to provide /usr/bin/python (python) in auto mode
    => ~ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
    update-alternatives: using /usr/bin/python3.6 to provide /usr/bin/python (python) in auto mode
    ```

    ```bash
    => ~ ls -l /usr/bin/python*
    lrwxrwxrwx 1 root root      24 Feb  5 08:35 /usr/bin/python -> /etc/alternatives/python
    lrwxrwxrwx 1 root root       9 Sep 23 10:18 /usr/bin/python2 -> python2.7
    -rwxr-xr-x 1 root root 3617176 Sep 24 00:06 /usr/bin/python2.7
    lrwxrwxrwx 1 root root       9 Oct 10 08:00 /usr/bin/python3 -> python3.6
    -rwxr-xr-x 2 root root 4568920 Oct  3 23:45 /usr/bin/python3.6
    -rwxr-xr-x 2 root root 4568920 Oct  3 23:45 /usr/bin/python3.6m
    lrwxrwxrwx 1 root root      10 Oct 10 08:00 /usr/bin/python3m -> python3.6m
    ```

    ```bash
    => ~ update-alternatives --list python
    /usr/bin/python2.7
    /usr/bin/python3.6
    ```

    ```bash
    => ~ sudo update-alternatives --config python
    There are 2 choices for the alternative python (providing /usr/bin/python).

      Selection    Path                Priority   Status
    ------------------------------------------------------------
    * 0            /usr/bin/python3.6   2         auto mode
      1            /usr/bin/python2.7   1         manual mode
      2            /usr/bin/python3.6   2         manual mode

    Press <enter> to keep the current choice[*], or type selection number: 1
    update-alternatives: using /usr/bin/python2.7 to provide /usr/bin/python (python) in manual mode
    => ~ python --version
    Python 2.7.14

    ```

    ```bash
    => ~ sudo update-alternatives --config python
    There are 2 choices for the alternative python (providing /usr/bin/python).

      Selection    Path                Priority   Status
    ------------------------------------------------------------
      0            /usr/bin/python3.6   2         auto mode
    * 1            /usr/bin/python2.7   1         manual mode
      2            /usr/bin/python3.6   2         manual mode

    Press <enter> to keep the current choice[*], or type selection number: 2
    update-alternatives: using /usr/bin/python3.6 to provide /usr/bin/python (python) in manual mode
    => ~ python --version
    Python 3.6.3

    ```

    ​

