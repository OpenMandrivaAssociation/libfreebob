%define name	libfreebob
%define version	1.0.0
%define svn	199
%define release %mkrel 1

%define major	0
%define libname %mklibname freebob %major

Name: 	 	%{name}
Summary: 	Library for BeBoB audio devices
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://freebob.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig libxml2-devel zlib-devel
BuildRequires:	libavc1394-devel >= 0.5.2
BuildRequires:	libiec61883-devel >= 1.1.0
BuildRequires:	libraw1394-devel
BuildRequires:	libalsa-devel

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
%setup -q -n %name-%version

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc


