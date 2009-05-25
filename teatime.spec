Summary:	Teatime applet for GNOME 2
Name:		teatime
Version:	3.0
Release:	%mkrel 1
License:	GPLv3
Group:		Graphical desktop/GNOME
URL:		http://det.cable.nu/teatime/index.rbx
Source0:	http://det.cable.nu/pakete/teatime-%version.tar.bz2
#configure does not like ruby-gettext 1.10
Patch:		teatime-3.0-configure-check.patch
#gw disable installation here
Patch1:		teatime-3.0-installation.patch
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	ruby-panelapplet2
BuildRequires:	ruby-cairo
BuildRequires:	ruby-gst
BuildRequires:       ruby-gconf2

BuildRequires:	x11-server-xvfb
Requires:	ruby-panelapplet2
Requires:	ruby-cairo
Requires:	ruby-gst
Requires:       ruby-gconf2

%description
This is the GNOME 2 port of the legendary teatime applet. There are big
enhancements like animated, rendered teacups, user configurable drawing times
and some other gimmiks.


%prep
%setup -q
%patch -p1
%patch1 -p1

%build
cd teatime
xvfb-run ruby setup.rb config
ruby setup.rb setup


%install
rm -rf %buildroot
cd teatime
ruby setup.rb install --prefix=%buildroot
#gw usually done by post-install.rb:
install -D -m 644 data-ext/GNOME_TeatimeApplet3_Factory.server %buildroot%_libdir/bonobo/servers/GNOME_TeatimeApplet3_Factory.server
install -D -m 644 data-ext/teatime_applet_3.schemas %buildroot%_sysconfdir/gconf/schemas/teatime_applet_3.schemas
cd ..
%find_lang %name


%clean
rm -rf %buildroot

%if %mdvver < 200900
%post
%post_install_gconf_schemas teatime_applet_3
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas teatime_applet_3

%files -f %name.lang
%defattr(0755,root,root,0755)
%{_bindir}/teatime_applet_3
%defattr(0644,root,root,0755) 
%doc teatime/AUTHORS teatime/ChangeLog teatime/README
%{_sysconfdir}/gconf/schemas/teatime_applet_3.schemas
#gw this dir is arch-dependant:
%{_libdir}/bonobo/servers/*
%{_datadir}/pixmaps/*
%ruby_sitelibdir/%{name}*
%_datadir/icons/hicolor/*/apps/*
