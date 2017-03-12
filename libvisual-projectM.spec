
Obsolete packaga,e all projectM plugins are build now from libprojectM

Summary:	ProjectM plugin for libvisual
Summary(pl.UTF-8):	Wtyczka ProjectM dla libvisual
Name:		libvisual-projectM
Version:	2.0.1
Release:	1.1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/project/projectm/%{version}/projectM_libvisual-%{version}-Source.tar.gz
# Source0-md5:	35e09b09210d48b437e3574bd00b15a8
URL:		http://projectm.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	cmake >= 2.4.0
BuildRequires:	libprojectM-devel >= 1:1.2.0
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
%setup -q -n projectM_libvisual-%{version}-Source

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/libvisual-0.4/actor/libprojectM_libvisual.so
