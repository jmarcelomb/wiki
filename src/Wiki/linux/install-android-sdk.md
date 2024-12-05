# Install Android SDK (without Android studio) 

## Java 
Check java version (must be 8 or 10)
```bash
java -version
```

Install Java8
```bash
sudo pacman -S jre8-openjdk
```

## Android SDK 
Install Android SDK
```bash
yay -S android-sdk android-sdk-platform-tools android-sdk-build-tools
yay -S android-platform
```

Install Android SDK
```bash
yay -S android-sdk android-sdk-platform-tools android-sdk-build-tools
yay -S android-platform
```

Permissions
```bash
sudo groupadd android-sdk
sudo gpasswd -a $USER android-sdk
sudo setfacl -R -m g:android-sdk:rwx /opt/android-sdk
sudo setfacl -d -m g:android-sdk:rwX /opt/android-sdk
```

Add to PATH
Put these lines on .bashrc
```bash
export ANDROID_SDK_ROOT='/opt/android-sdk'
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools/
export PATH=$PATH:$ANDROID_SDK_ROOT/tools/bin/
export PATH=$PATH:$ANDROID_ROOT/emulator
export PATH=$PATH:$ANDROID_SDK_ROOT/tools/
```

Accept licenses
```bash
cd /opt/android-sdk/tools/bin
yes | sdkmanager --licenses
```

* If still missing license acceptance or missing package error

Install package:
```bash
sdkmanager "platforms;android-28"
```

## Gradle 

Download gradle zip from [[https://gradle.org/releases]]

Unzip downloaded zip:
```bash
mkdir /opt/gradle
unzip -d /opt/gradle gradle-7.2-bin.zip
```

Add to path
```bash
export PATH=$PATH:/opt/gradle/gradle-7.2/bin
```
