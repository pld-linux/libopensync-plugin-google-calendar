Summary:	OpenSync Google Calendar Plugin
Summary(pl.UTF-8):	Wtyczka Google Calendar do OpenSync
Name:		libopensync-plugin-google-calendar
Version:	0.22
Release:	3
License:	GPL v2+
Group:		Libraries
# originally http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw, dead now
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e97862bc7479e449206e2a438a159336
# dead domain
#URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-httplib2
BuildRequires:	sed >= 4.0
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
%{__sed} -i -e '1s,#!.*python,#!%{__python},' src/google-cal-helper.py

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/google-cal-helper
%attr(755,root,root) %{_libdir}/opensync/plugins/gcalendar.so
%{_datadir}/opensync/defaults/google-calendar
