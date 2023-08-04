# Recover boot loader after updating Mac OS

1. Have live ubuntu USB

2. Boot into that live OS and execute the following commands

   ```bash
   $ sudo apt-get install efibootmgr
   Reading package lists... Done
   Building dependency tree  	 
   Reading state information... Done
   efibootmgr is already the newest version (0.12-4).
   0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
   ```

   ```bash
   $ sudo efibootmgr
   BootCurrent: 0000
   Timeout: 5 seconds
   BootOrder: 0080,0000
   Boot0000* ubuntu
   Boot0080* Mac OS X
   Boot0081* Mac OS X
   Boot0082*
   BootFFFF*
   ```

   ```bash
   $ sudo efibootmgr -o 0000,0080
   BootCurrent: 0000
   Timeout: 5 seconds
   BootOrder: 0000,0080
   Boot0000* ubuntu
   Boot0080* Mac OS X
   Boot0081* Mac OS X
   Boot0082*
   BootFFFF*
   ```

3. Shutdown

4. Remove live usb

5. power back on

6. It will boot into ubuntu