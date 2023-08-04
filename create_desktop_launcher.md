# Create desktop launcher

Make any file that can run to launch from desktop by using app launcher (win+space)

1. Create Typora.desktop file with the following contents (replace file paths properly)
   
   ```bash
   [Desktop Entry]
   Encoding=UTF-8
   Version=1.0
   Type=Application
   Terminal=false
   Exec=/typora/Typora-linux-x64/Typora
   Name=Typora
   Icon=/typora/Typora-linux-x64/resources/app/asserts/icon/icon_128x128.png
   ```

2. ​Save this file under /usr/share/applications/ if this app is required for everybody. Else save it under ~/.local/share/applications