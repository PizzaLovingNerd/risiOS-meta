Name:           risios-meta
Version:        37
Release:        7%{?dist}
Summary:        General files for risiOS
License:        GPL3
URL:            http://risi.io/
Source0:        https://github.com/risiOS/risiOS-meta/archive/refs/heads/main.tar.gz
BuildArch:      noarch

Requires:		risios-bookmarks
Requires:		risios-logos
Requires:		risios-release
Requires:		risifetch
Requires:		zsh
Requires:		risios-repositories
Requires:  flatpak-timeout-fix

Recommends:		risi-zsh-plugins
Recommends:		adw-gtk-theme
Recommends: 	gnome-shell-extension-dock-from-dash
Recommends: 	gnome-shell-extension-risi-gnome
Recommends: 	risi-script
Recommends:		risi-settings
Recommends:		risi-tweaks
Recommends:		risi-welcome
Recommends:		rtheme-d
Recommends:		rtheme-lib
Recommends:		rtheme-plugin-gtk3
Recommends:		rtheme-plugin-gtk4
Recommends:		rtheme-plugin-gnome-shell

%description
Provides some extra files by default in the home dir.
 
%prep
%autosetup -n risiOS-meta-main

%build
%install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/chromium/policies/recommended

cp -a skel %{buildroot}%{_sysconfdir}
cp chromium-risios.json %{buildroot}%{_sysconfdir}/chromium/policies/recommended/risios.json

%files
%{_sysconfdir}/chromium/policies/recommended/risios.json
%dir %{_sysconfdir}/skel/Templates
%{_sysconfdir}/skel/Templates/*
 
%changelog
%autochangelog
