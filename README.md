# Firmware override for Surface devices with QCA6174 ATH10K WiFi Chip

Firmware override for Surface devices with QCA6174 ATH10K WiFi chip,
specifically the Surface Go devices and the AMD Surface Laptops.

The board file is taken from a Killer WiFi chip and has be obtained from the [Killer support page](https://web.archive.org/web/20201111213909/http://www.killernetworking.com/support/K1535_Debian/board.bin).
This workaround requires [this](https://github.com/linux-surface/kernel/commit/19d746dc9980d9109b93c9424138d3966c8a67cf) patch to work.
It does not override the previously installed firmware files and only overrides the loading procedure via the linked patch and the modprobe config in this repository.
