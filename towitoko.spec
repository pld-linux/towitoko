
Summary:	Unix driver for Towitoko smartcard readers
Name:		towitoko
Version:	2.0.7
Release:	1
Source0:	http://www.geocities.com/cprados/files/%{name}-%{version}.tar.gz
Group:		Libraries
License:	LGPL
URL:		http://www.geocities.com/cprados/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libchipcard allows easy access to smart cards. It provides basic
access to memory and processor cards and has special support for
German medical cards, German "Geldkarten" and HBCI (homebanking) cards
(both type 0 and type 1). It accesses the readers via CTAPI or PC/SC
interfaces and has successfully been tested with Towitoko, Kobil and
Reiner-SCT readers.

%package devel
Summary:	towitoko development kit
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for writing programs using towitoko.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT \
  install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/reader.conf
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/design.html
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/ct*
