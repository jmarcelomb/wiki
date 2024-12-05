# Smartcard reader on linux

Most information was taken from [ArchWiki](https://wiki.archlinux.org/title/Smartcards).

## Needed packages

Install [ccid](https://archlinux.org/packages/community/x86_64/ccid) and
[opensc](https://archlinux.org/packages/community/x86_64/opensc):
`pacman -Syu ccid opensc`

Start/Enable the systemd unit: `systemctl start pcscd.service` or
`systemctl enable --now pcscd.service`

### Test it

Install [pcsc-tools](https://archlinux.org/packages/community/x86_64/pcsc-tools),
and call `pcsc_scan`. Try plugging/unplugging the card reader and a card, and
examine the terminal output.

**Note**: you can uninstall **pcsc-tools** now.

## Firefox support

The browser needs to set the new security-related device. Open the Security Devices
page (reach it via `Preferences > Privacy & Security > Certificates > Security Devices...`),
then click `Load` and set the Module Name to **CAC Module** and module filename
to /usr/lib/opensc-pkcs11.so.

## Plugin Autenticação.gov pt

Install [plugin-autenticacao-gov-pt](https://aur.archlinux.org/packages/plugin-autenticacao-gov-pt)
from the [AUR](https://aur.archlinux.org). For other distributions see
[here](https://autenticacao.gov.pt/fa/ajuda/autenticacaogovpt.aspx):

- **Debian/Ubuntu**: `dpkg -i plugin-autenticacao-gov.deb`
- **Fedora**: `dnf install plugin-autenticacao-gov_fedora.rpm`
- **RedHat/CentOS**: `yum install plugin-autenticacao-gov_rhel`
- **OpenSuse**: `zypper install plugin-autenticacao-gov_opensuse.rpm`
