%global _firmware_path /usr/lib/firmware

Name: surface-ath10k-firmware-override
Summary: Firmware override for Surface devices with QCA6174 ATH10K WiFi chip
Version: 20210520
Release: 1

URL: https://github.com/linux-surface/ath10k-firmware-override
BuildArch: noarch
License: proprietary

Source0: board.bin
Source1: ath10k.conf

Requires: kernel-surface

%description
Firmware override for Surface devices with QCA6174 ATH10K WiFi chip,
specifically the Surface Go series and AMD Surface Laptops.

%prep

%build

%install
install -D -m644 board.bin "%{buildroot}%{_firmware_path}/ath10k/QCA6174/hw2.1/board-override.bin"
install -D -m644 board.bin "%{buildroot}%{_firmware_path}/ath10k/QCA6174/hw3.0/board-override.bin"
install -D -m644 ath10k.conf "%{buildroot}%{_modprobedir}/ath10k.conf"

%files
%{_firmware_path}/ath10k/QCA6174/hw2.1/board-override.bin
%{_firmware_path}/ath10k/QCA6174/hw3.0/board-override.bin
%{_modprobedir}/ath10k.conf

%changelog
* Thu May 20 2021 Dorian Stoll <dorian.stoll@tmsp.io> - 20210520-1
- Move package files out of the pkg subdirectory
- Other small improvements

* Wed May 19 2021 Maximilian Luz <luzmaximilian@gmail.com> - 20210519-1
- Initial package
