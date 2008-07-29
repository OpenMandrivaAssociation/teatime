Summary:	Teatime applet for GNOME 2
Name:		teatime
Version:	2.8.0
Release:	%mkrel 3
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://det.cable.nu/teatime/index.rbx
Source0:	http://det.cable.nu/pakete/teatime_applet_2-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
Buildrequires:	libpanel-applet-devel >= 2.6
Buildrequires:	libgstreamer-plugins-base-devel
Buildrequires:	perl-XML-Parser

%description
This is the GNOME 2 port of the legendary teatime applet. There are big
enhancements like animated, rendered teacups, user configurable drawing times
and some other gimmiks.


%prep
%setup -q -n teatime_applet_2-%version


%build
%configure2_5x --disable-schemas-install
%make


%install
rm -rf %buildroot
%makeinstall
%find_lang %name


%clean
rm -rf %buildroot


%post
%post_install_gconf_schemas teatime

%preun
%preun_uninstall_gconf_schemas teatime

%files -f %name.lang
%defattr(0755,root,root,0755)
%{_libdir}/teatime_applet_2
%defattr(0644,root,root,0755) 
%doc AUTHORS ChangeLog COPYING INSTALL README
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_datadir}/pixmaps/*


