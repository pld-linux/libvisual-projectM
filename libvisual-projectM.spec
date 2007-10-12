#
%define		package		projectM-libvisual
#
Summary:	ProjectM plugin for libvisual
Summary(pl.UTF-8):	Wtyczka ProjectM dla libvisual
Name:		libvisual-projectM
Version:	1.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/projectm/%{package}-%{version}.tar.bz2
# Source0-md5:	0812241e443c8b9e35bbe44a7bbade3d
URL:		http://projectm.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	libprojectM-devel = %{version}
BuildRequires:	libvisual-devel = 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
projectM is a reimplementation of Milkdrop under OpenGL. This
is a plugin for libvisual visualization library.

%description -l pl.UTF-8
projectM jest reimplementacją projektu Milkdrop na OpenGL. To
jest plugin dla biblioteki wizualizacji libvisual.

%prep
%setup -q -n %{package}-%{version}

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
        .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/libvisual-0.4/actor/libprojectM_libvisual.so
