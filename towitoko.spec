Summary:	Unix driver for Towitoko smartcard readers
Summary(pl):	Uniksowy sterownik do czytników kart procesorowych Towitoko
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
(both type 0 and type 1). It accesses the readers via CT-API or PC/SC
interfaces and has successfully been tested with Towitoko, Kobil and
Reiner-SCT readers.

%description -l pl
Libchipcard pozwala na ³atwy dostêp do kart procesorowych. Udostêpnia
podstawowy dostêp do kart pamiêciowych i procesorowych, ma specjaln±
obs³ugê niemieckich kart medycznych, niemieckich "Geldkarten" oraz
kart do homebankingu HBCI (typu 0 i 1). Dostêp do czytnika mo¿e
odbywaæ siê przez interfejs CT-API lub PC/SC; by³ testowany z
czytnikami Towitoko, Kobil i Reiner-SCT.

%package devel
Summary:	towitoko development kit
Summary(pl):	Pakiet programistyczny towitoko
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for writing programs using towitoko.

%description devel -l pl
Pliki nag³ówkowe do pisania programów z u¿yciem towitoko.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/reader.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/design.html
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/ct*
