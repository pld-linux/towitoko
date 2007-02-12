Summary:	Unix driver for Towitoko smartcard readers
Summary(pl.UTF-8):   Uniksowy sterownik do czytników kart procesorowych Towitoko
Name:		towitoko
Version:	2.0.7
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.geocities.com/cprados/files/%{name}-%{version}.tar.gz
# Source0-md5:	6cb2f842ca11aa79692af89d3730f4ce
URL:		http://www.geocities.com/cprados/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libchipcard allows easy access to smart cards. It provides basic
access to memory and processor cards and has special support for
German medical cards, German "Geldkarten" and HBCI (homebanking) cards
(both type 0 and type 1). It accesses the readers via CT-API or PC/SC
interfaces and has successfully been tested with Towitoko, Kobil and
Reiner-SCT readers.

%description -l pl.UTF-8
Libchipcard pozwala na łatwy dostęp do kart procesorowych. Udostępnia
podstawowy dostęp do kart pamięciowych i procesorowych, ma specjalną
obsługę niemieckich kart medycznych, niemieckich "Geldkarten" oraz
kart do homebankingu HBCI (typu 0 i 1). Dostęp do czytnika może
odbywać się przez interfejs CT-API lub PC/SC; był testowany z
czytnikami Towitoko, Kobil i Reiner-SCT.

%package devel
Summary:	towitoko development kit
Summary(pl.UTF-8):   Pakiet programistyczny towitoko
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for writing programs using towitoko.

%description devel -l pl.UTF-8
Pliki nagłówkowe do pisania programów z użyciem towitoko.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/reader.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/design.html
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_mandir}/man3/ct*
