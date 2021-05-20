# Maintainer: Maximilian Luz <luzmaximilian@gmail.com>

pkgname=surface-ath10k-firmware-override
pkgver=20210519
pkgrel=1
arch=(any)
pkgdesc="Firmware override for Surface devices with QCA6174 ATH10K WiFi Chip"
url="http://github.com/linux-surface/ath10k-firmware-override"
license=('custom')

source=(
    board.bin
    ath10k.conf
)
sha256sums=(
    'e79b80e2243c62f41fbaf1cc92845cefb11019b0a6d1c91488cf43fd63dcf85c'
    '854282620f02ef7f76c0658749cb56d517bfda168f231d989395c8c08908cce0'
)


package() {
    cd $startdir

    install -D -m644 "board.bin" "${pkgdir}/usr/lib/firmware/ath10k/QCA6174/hw2.1/board-override.bin"
    install -D -m644 "board.bin" "${pkgdir}/usr/lib/firmware/ath10k/QCA6174/hw3.0/board-override.bin"
    install -D -m644 "ath10k.conf" "${pkgdir}/usr/lib/modprobe.d/ath10k.conf"
}
