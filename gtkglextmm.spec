Name:			gtkglextmm
Version:		1.2.0
Release:		%mkrel 1

%define	major		0
%define	api_version	1.2
%define	libname		%mklibname gtkglextmm %major
%define develname	%mklibname gtkglextmm -d

Summary:	Libraries for the gtkglextmm package
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.k-3d.org/gtkglext/Main_Page
Source0:	http://downloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2

BuildRequires:	gtkmm2.4-devel
BuildRequires:	gtkglext-devel
BuildRequires:	pkgconfig
BuildRequires:	doxygen
BuildRequires:	recode
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Library and data files for the gtkglextmm package.

%package -n	%{libname}
Summary:	Dynamic libraries from gtkglextmmO
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}

%description -n	%{libname}
Dynamic libraries from gtkglextmm.

%package -n	%{develname}
Summary:	Header files and static libraries from gtkglextmm
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gtkglextmm-devel = %{version}-%{release} 
Obsoletes:	gtkglextmm-devel < %{version}-%{release}

%description -n	%{develname}
Libraries and includes files for developing programs based on gtkglextmm.


%prep
%setup -q
recode l1..u8 AUTHORS README

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

#rpmlint reports an empty file
rm -f %{buildroot}%{_libdir}/gtkglextmm-1.2/proc/m4/convert_gtkglext.m4

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%doc %{_docdir}/gtkglextmm-1.2
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_libdir}/gtkglextmm-1.2

