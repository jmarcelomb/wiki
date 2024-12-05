# OBS stream screen in camera

Sometimes streaming the screen in an application sucks and is very limited. We can feed a stream to a virtual camera (V4L2 loopback device) in order to have more control in streams.

Note: This guide is for Linux. In windows, you can use the virtual camera feature. It comes builtin since version 26.0.0, but can also be added with the plugin [obs-virtual-cam](https://github.com/CatxFish/obs-virtual-cam).

## Kernel module

To create one of these devices (in Linux), we have to install and load a kernel module: [v4l2loopback](https://github.com/umlaeute/v4l2loopback).

Instructions:
  - `git clone https://github.com/umlaeute/v4l2loopback.git`
  - `cd v4l2loopback`
  - `make && sudo make install`
  - `sudo depmod -a`
  - `sudo modprobe v4l2loopback`

By this point, you should have a new `/dev/videoN` device, where N is an integer. This device will probably be the last one of the ones you have.

This kernel module can be unloaded by doing `sudo rmmod v4l2loopback`. You might have to load it each time you turn on your pc and want to use it: `sudo modprobe v4l2loopback`.

The loading command can take some arguments to specify the number of devices created and the device ID's of these devices, e.g.:
  - `modprobe v4l2loopback devices=4`
  - `modprobe v4l2loopback video_nr=3,4,7`
NOTE: the `exclusive_caps=1` option can be useful to use the device in application that refuse to open devices that have capabilities besides **CAPTURE**, e.g.: Chrome/WebRTC.

## OBS plugin

The [obs-v4l2sink](https://github.com/CatxFish/obs-v4l2sink) plugin provides the capability to [OBS studio](https://obsproject.com/) to output to V4L2 devices.

Instructions (depends on qtbase5-dev and libobs-dev):
  - `git clone --recursive https://github.com/obsproject/obs-studio.git`
  - `git clone https://github.com/CatxFish/obs-v4l2sink.git`
  - `cd obs-v4l2sink`
  - `mkdir build && cd build`
  - `cmake -DLIBOBS_INCLUDE_DIR="../../obs-studio/libobs" -DCMAKE_INSTALL_PREFIX=/usr ..`
  - `make -j4`
  - `sudo make install`

Note: We cloned obs-studios's source code in order to links with its libraries during compilation.

Now, we can go to OBS and open the menu entry `Tools > V4L2 Video Output`. This will open a menu where we can select the video format and the path to the video device (`/dev/videoN`). After that, we just have to press start and our current OBS scene will be streamed on that device.
