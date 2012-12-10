%define	major		0
%define	api_version	1.2
%define	libname		%mklibname gtkglextmm %{major}
%define	develname	%mklibname gtkglextmm -d

Name:		gtkglextmm
Version:	1.2.0
Release:	4
Summary:	Libraries for the gtkglextmm package
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.k-3d.org/gtkglext/Main_Page
Source0:	http://downloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
Patch0:		gtkglextmm-1.2.0-aclocal.patch
Patch1:		gtkglextmm-1.2.0-gtk2.20.patch
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	doxygen
BuildRequires:	recode

%description
Library and data files for the gtkglextmm package.

%package -n	%{libname}
Summary:	Dynamic libraries from gtkglextmmO
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Dynamic libraries from gtkglextmm.

%package -n	%{develname}
Summary:	Header files and static libraries from gtkglextmm
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gtkglextmm-devel = %{version}-%{release} 

%description -n	%{develname}
Libraries and includes files for developing programs based on gtkglextmm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
recode l1..u8 AUTHORS README

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

#rpmlint reports an empty file
rm -f %{buildroot}%{_libdir}/gtkglextmm-1.2/proc/m4/convert_gtkglext.m4

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README
%doc %{_docdir}/gtkglextmm-1.2
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/gtkglextmm-1.2

%changelog
* Fri Sep 11 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2.0-3mdv2010.0
+ Revision: 437828
- rebuild

* Wed Mar 25 2009 Götz Waschk <waschk@mandriva.org> 1.2.0-2mdv2009.1
+ Revision: 361011
- rebuild

* Tue Oct 21 2008 Guillaume Bedot <littletux@mandriva.org> 1.2.0-1mdv2009.1
+ Revision: 296257
- import gtkglextmm


* Thu Sep 18 2008 Guillaume Bedot <littletux@mandriva.org> 1.2.0-1mdv2009.0
- First package of gtkglextmm for Mandriva
