Name:       wooting-udev-rules
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    udev rules for Wooting keyboards
License:    GPLv2+
URL:        https://github.com/KyleGospo/wooting-udev-rules
BuildArch:  noarch

%description
Provides access to Wooting devices to users within the input group

%prep

%build

%install

install -d %{buildroot}%{_sysconfdir}/udev/rules.d
cat > %{buildroot}%{_sysconfdir}/udev/rules.d/80-wooting.rules << EOF
# Wooting One Legacy
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff01", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff01", MODE:="0660", GROUP="input"
# Wooting One update mode 
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2402", MODE:="0660", GROUP="input"

# Wooting Two Legacy
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff02", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff02", MODE:="0660", GROUP="input"
# Wooting Two update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2403", MODE:="0660", GROUP="input"

# Wooting One
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1100", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1100", MODE:="0660", GROUP="input"
# Wooting One Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1101", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1101", MODE:="0660", GROUP="input"
# Wooting One 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1102", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1102", MODE:="0660", GROUP="input"

# Wooting Two
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1200", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1200", MODE:="0660", GROUP="input"
# Wooting Two Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1201", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1201", MODE:="0660", GROUP="input"
# Wooting Two 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1202", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1202", MODE:="0660", GROUP="input"

# Wooting Lekker
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1210", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1210", MODE:="0660", GROUP="input"
# Wooting Lekker Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1211", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1211", MODE:="0660", GROUP="input"
# Wooting Lekker 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1212", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1212", MODE:="0660", GROUP="input"

# Wooting Lekker update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="121f", MODE:="0660", GROUP="input"

# Wooting Two HE
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1220", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1220", MODE:="0660", GROUP="input"
# Wooting Two HE Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1221", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1221", MODE:="0660", GROUP="input"
# Wooting Two HE 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1222", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1222", MODE:="0660", GROUP="input"

# Wooting Two HE update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="122f", MODE:="0660", GROUP="input"

# Wooting 60HE
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1300", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1300", MODE:="0660", GROUP="input"
# Wooting 60HE Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1301", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1301", MODE:="0660", GROUP="input"
# Wooting 60HE 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1302", MODE:="0660", GROUP="input"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1302", MODE:="0660", GROUP="input"

# Wooting 60HE update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="130f", MODE:="0660", GROUP="input"
EOF

%post

%preun

%files
%{_sysconfdir}/udev/rules.d/80-wooting.rules
