# Install flutter

```bash
yay -Syu flutter android-sdk-cmdline-tools-latest android-sdk-platform-tools android-sdk-build-tools android-platform
sudo chown -R $USER /opt/flutter
sudo setfacl -R -m u:$USER:rwx /opt/android-sdk
sudo setfacl -d -m u:$USER:rwX /opt/android-sdk
flutter doctor --android-licenses # aceita tudo com y
flutter run -d web-server # inside the flutter_src directory
```