# Maintainer: Maximilian Luz <luzmaximilian@gmail.com>

pkgname=surface-ath10k-firmware-override
pkgver=20211031
pkgrel=1
arch=(any)
pkgdesc="Firmware override for Surface devices with QCA6174 ATH10K WiFi Chip"
url="http://github.com/linux-surface/ath10k-firmware-override"
license=('custom')
depends=('linux-surface')

source=(
    board-2.bin
    ath10k.conf
)
sha256sums=('812276afb86ff3e1be58fc444f2e984cb2473d33942b38e9dd4f4495a46ea9e9'
            '8335a992e8d2a20f6aa7514ebd8eaccda1395dd9675ca50007784797843216e9')


package() {
    cd $startdir

    install -D -m644 "board-2.bin" "${pkgdir}/usr/lib/firmware/ath10k/QCA6174/hw3.0/board-2-surface.bin"
    install -D -m644 "ath10k.conf" "${pkgdir}/usr/lib/modprobe.d/ath10k.conf"
}
