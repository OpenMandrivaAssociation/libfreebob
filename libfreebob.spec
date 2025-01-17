%define major 0
%define libname %mklibname freebob %major

Name: 	 	libfreebob
Summary: 	Library for BeBoB audio devices
Version: 	1.0.11
Release: 	8
License:	GPL
Group:		Sound
URL:		https://freebob.sourceforge.net/
Source:		%{name}-%{version}.tar.gz
Patch0:		libfreebob-1.0.7-gcc43.diff
Patch1:		libfreebob-1.0.11-gcc451.diff
BuildRequires:	libalsa-devel >= 1.0.0
BuildRequires:	libavc1394-devel >= 0.5.3
BuildRequires:	libiec61883-devel >= 1.1.0
BuildRequires:	libraw1394-devel >= 1.2.1
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This library provides access to BeBoB devices from the Freebob project.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Provides:	%name
Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
rm -f configure
libtoolize --copy --force; aclocal; autoconf

%configure2_5x --enable-static=false

%make
										
%install
rm -rf %{buildroot}

%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

