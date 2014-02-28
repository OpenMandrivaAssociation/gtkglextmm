%define	major	0
%define	api	1.2
%define	gdkname	%mklibname gdkglextmm-x11_ %{api} %{major}
%define	gtkname	%mklibname gtkglextmm-x11_ %{api} %{major}
%define	devname	%mklibname gtkglextmm-x11_ %{api} -d

Summary:	Libraries for the gtkglextmm package
Name:		gtkglextmm
Version:	1.2.0
Release:	5
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.k-3d.org/gtkglext/Main_Page
Source0:	http://downloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
Patch0:		gtkglextmm-1.2.0-aclocal.patch
Patch1:		gtkglextmm-1.2.0-gtk2.20.patch
Patch2:		gtkglextmm-1.2.0-gtk2.36.patch
Patch3:		gtkglextmm-1.2.0-gtk2.37.patch
BuildRequires:	doxygen
BuildRequires:	recode
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(gtkglext-1.0)

%description
Library and data files for the gtkglextmm package.

#----------------------------------------------------------------------------

%package -n	%{gdkname}
Summary:	Dynamic libraries from gtkglextmmO
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
Conflicts:	%{_lib}gtkglextmm0 < 1.2.0-5

%description -n	%{gdkname}
Dynamic libraries from gtkglextmm.

%files -n %{gdkname}
%{_libdir}/libgdkglextmm-x11-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{gtkname}
Summary:	Dynamic libraries from gtkglextmmO
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
Conflicts:	%{_lib}gtkglextmm0 < 1.2.0-5
Obsoletes:	%{_lib}gtkglextmm0 < 1.2.0-5

%description -n	%{gtkname}
Dynamic libraries from gtkglextmm.

%files -n %{gtkname}
%{_libdir}/libgtkglextmm-x11-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Header files and static libraries from gtkglextmm
Group:		Development/C
Requires:	%{gtkname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{_lib}gtkglextmm-devel < 1.2.0-5
Obsoletes:	%{_lib}gtkglextmm-devel < 1.2.0-5

%description -n	%{devname}
Libraries and includes files for developing programs based on gtkglextmm.

%files -n %{devname}
%doc AUTHORS ChangeLog README
%doc %{_docdir}/gtkglextmm-1.2
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/libgdkglextmm-x11-%{api}.so
%{_libdir}/libgtkglextmm-x11-%{api}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/gtkglextmm-1.2

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
recode l1..u8 AUTHORS README

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

#rpmlint reports an empty file
rm -f %{buildroot}%{_libdir}/gtkglextmm-1.2/proc/m4/convert_gtkglext.m4

