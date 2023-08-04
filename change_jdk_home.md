# Change JDK home in ubuntu

1. download jdk
2. unzip it
3. register it
  sudo update-alternatives --install /usr/bin/java java /path/to/your/jdk/bin/java 1
4. change to manual mode by pointing it to the above jdk
  sudo update-alternatives --config java

To unregister 
sudo update-alternatives --remove java /tools/installed/java/jdk1.8.0_144
