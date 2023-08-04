# Swap Ctrl with Win in ubuntu

1. Open ~/.Xmodmap file. If it is not there, then create one

2. Paste the below contents to that file

   ```
   clear control
   clear mod4

   keycode 105 =
   keycode 206 =

   keycode 133 = Control_L NoSymbol Control_L
   keycode 134 = Control_R NoSymbol Control_R
   keycode 37 = Super_L NoSymbol Super_L

   add control = Control_L
   add control = Control_R
   add mod4 = Super_L
   ```

3. Open ~/.profile file and paste the below contents

   ```
   # below command is run to swap ctrl and win
   xmodmap ~/.Xmodmap
   ```

4. Source ~/.profile and you are good to go

5. Since it is in ~/.profile as soon as terminal is fired this will be executed

------------------------------

If you want to run xmodmap ~/.Xmodmap on bootup, then refer to [run_commands_startups](run_commands_on_bootup.md)