#
%define		_name		projectM-libvisual
#
Summary:	ProjectM plugin for libvisual
Summary(pl.UTF-8):	Wtyczka ProjectM dla libvisual
Name:		libvisual-projectM
Version:	1.2.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/projectm/%{_name}-%{version}.tar.bz2
# Source0-md5:	41a90c5b8931a2cfcdd406eca89e83f9
URL:		http://projectm.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	cmake
BuildRequires:	libprojectM-devel >= 1:%{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libvisual-devel = 0.4.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
projectM is a reimplementation of Milkdrop under OpenGL. This is a
plugin for libvisual visualization library.

%description -l pl.UTF-8
projectM jest reimplementacją projektu Milkdrop na OpenGL. Ten pakiet
zawiera wtyczkę dla biblioteki wizualizacji libvisual.

%prep
%setup -q -n %{_name}-%{version}

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
