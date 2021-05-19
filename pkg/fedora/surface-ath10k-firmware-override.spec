Name:       surface-ath10k-firmware-override
Summary:    Firmware override for Surface devices with QCA6174 ATH10K WiFi chip
Version:    20210519
Release:    1
URL:        https://github.com/linux-surface/ath10k-firmware-override
License:    proprietary
BuildArch:  noarch

Source0:    https://raw.githubusercontent.com/linux-surface/ath10k-firmware-override/main/board.bin
Source1:    https://raw.githubusercontent.com/linux-surface/ath10k-firmware-override/main/ath10k.conf

%description
Firmware override for Surface devices with QCA6174 ATH10K WiFi chip,
specifically the Surface Go series and AMD Surface Laptops.

%install
install -D -m644 board.bin "%{buildroot}/usr/lib/firmware/ath10k/QCA6174/hw2.1/board-override.bin"
install -D -m644 board.bin "%{buildroot}/usr/lib/firmware/ath10k/QCA6174/hw3.0/board-override.bin"
install -D -m644 ath10k.conf "%{buildroot}/etc/modprobe.d/ath10k.conf"

%files
/usr/lib/firmware/ath10k/QCA6174/hw2.1/board-override.bin
/usr/lib/firmware/ath10k/QCA6174/hw3.0/board-override.bin
/etc/modprobe.d/ath10k.conf

%changelog
* Wed May 19 2021 Maximilian Luz <luzmaximilian@gmail.com> - 20210519-1
- Initial package
