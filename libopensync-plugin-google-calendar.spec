Summary:	OpenSync Google Calendar Plugin
Summary(pl.UTF-8):	Wtyczka Google Calendar do OpenSync
Name:		libopensync-plugin-google-calendar
Version:	0.36
Release:	1
License:	GPL v2+
Group:		Libraries
# originally http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw, dead now
# resored from http://ftp.iij.ad.jp/pub/linux/momonga/5/Everything/SOURCES/libopensync-plugin-google-calendar-0.36.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	69b382845fb62a58e1976bc74a82dd86
Patch0:		%{name}-libopensync0.39.patch
# dead domain
#URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= 0.39
BuildRequires:	pkgconfig
BuildRequires:	python-httplib2
BuildRequires:	sed >= 4.0
Requires:	libopensync >= 0.39
Requires:	python-httplib2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains Google Calendar Plugin plugin for OpenSync
framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę Google Calendar dla szkieletu OpenSync.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python},' src/google-cal-helper.py

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libopensync1/google-cal-helper
%attr(755,root,root) %{_libdir}/libopensync1/plugins/gcalendar.so
%{_datadir}/libopensync1/capabilities/google-calendar-gcal-2005.xml
%{_datadir}/libopensync1/defaults/google-calendar
%{_datadir}/libopensync1/descriptions/google-calendar.xml
