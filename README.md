# Firmware override for Surface devices with QCA6174 ATH10K WiFi Chip

Firmware override for Surface devices with QCA6174 ATH10K WiFi chip,
specifically the Surface Go devices and the AMD Surface Laptops.

This workaround requires [this](https://github.com/linux-surface/kernel/commit/19d746dc9980d9109b93c9424138d3966c8a67cf) patch to work.
It does not override the previously installed firmware files and only overrides the loading procedure via the linked patch and the modprobe config in this repository.

- The `board-2.bin` file has been created by Hans de Goede based on Windows firmware files.
  See [these](https://github.com/linux-surface/linux-surface/issues/542) [issues](https://github.com/linux-surface/linux-surface/issues/41) and [this](https://github.com/kvalo/ath10k-firmware/pull/11) pull request for mored details.

### Outdated Files

- The `bus=pci,vendor=168c,device=003e,subsystem-vendor=168c,subsystem-device=3370.bin` has been obtained from the Windows installation on a Surface Go.
  See [this](https://github.com/linux-surface/linux-surface/issues/542) issue and [this](https://lore.kernel.org/ath10k/226790d7-75d8-bac3-9991-d73fa5b7df5b@hansg.org/T/#u) mailing-list post for details.

- The `board.bin` file is taken from a Killer WiFi chip and has be obtained from the [Killer support page](https://web.archive.org/web/20201111213909/http://www.killernetworking.com/support/K1535_Debian/board.bin).
  Please note that this is not the correct board file for either the Surface Laptop 3 and Surface Go, but seems to work anyways.
