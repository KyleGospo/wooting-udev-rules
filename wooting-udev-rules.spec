Name:          wooting-udev-rules
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       udev rules for Wooting keyboards
License:       GPLv2
URL:           https://github.com/KyleGospo/wooting-udev-rules
BuildArch:     noarch

Source:        {{{ git_dir_pack }}}

BuildRequires: systemd

%description
Provides access to Wooting devices to users within the input group

%prep
{{{ git_dir_setup_macro }}}

%build

%install

install -d %{buildroot}%{_udevrulesdir}
cat > %{buildroot}%{_udevrulesdir}/80-wooting.rules << EOF
# Wooting One Legacy
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff01", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff01", MODE:="0660", GROUP="wheel"
# Wooting One update mode 
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2402", MODE:="0660", GROUP="wheel"

# Wooting Two Legacy
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff02", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="ff02", MODE:="0660", GROUP="wheel"
# Wooting Two update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2403", MODE:="0660", GROUP="wheel"

# Wooting One
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1100", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1100", MODE:="0660", GROUP="wheel"
# Wooting One Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1101", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1101", MODE:="0660", GROUP="wheel"
# Wooting One 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1102", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1102", MODE:="0660", GROUP="wheel"

# Wooting Two
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1200", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1200", MODE:="0660", GROUP="wheel"
# Wooting Two Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1201", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1201", MODE:="0660", GROUP="wheel"
# Wooting Two 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1202", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1202", MODE:="0660", GROUP="wheel"

# Wooting Lekker
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1210", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1210", MODE:="0660", GROUP="wheel"
# Wooting Lekker Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1211", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1211", MODE:="0660", GROUP="wheel"
# Wooting Lekker 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1212", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1212", MODE:="0660", GROUP="wheel"

# Wooting Lekker update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="121f", MODE:="0660", GROUP="wheel"

# Wooting Two HE
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1220", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1220", MODE:="0660", GROUP="wheel"
# Wooting Two HE Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1221", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1221", MODE:="0660", GROUP="wheel"
# Wooting Two HE 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1222", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1222", MODE:="0660", GROUP="wheel"

# Wooting Two HE update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="122f", MODE:="0660", GROUP="wheel"

# Wooting 60HE
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1300", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1300", MODE:="0660", GROUP="wheel"
# Wooting 60HE Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1301", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1301", MODE:="0660", GROUP="wheel"
# Wooting 60HE 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1302", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1302", MODE:="0660", GROUP="wheel"

# Wooting 60HE update mode  
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="130f", MODE:="0660", GROUP="wheel"

# Wooting 60HE (ARM)
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1310", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1310", MODE:="0660", GROUP="wheel"
# Wooting 60HE (ARM) Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1311", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1311", MODE:="0660", GROUP="wheel"
# Wooting 60HE (ARM) 2nd Alt-gamepad mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1312", MODE:="0660", GROUP="wheel"
SUBSYSTEM=="usb", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="1312", MODE:="0660", GROUP="wheel"

# Wooting 60HE (ARM) update mode
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="31e3", ATTRS{idProduct}=="131f", MODE:="0660", GROUP="wheel"
EOF

%post -n %{name}
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi

%preun

%files
%license LICENSE
%doc README.md
%_udevrulesdir/80-wooting.rules

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}