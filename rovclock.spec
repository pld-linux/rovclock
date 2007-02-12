Summary:	Radeon overclocking utility
Summary(pl.UTF-8):   Narzędzie do zmiany częstotliwości pracy chipsetów Radeon
Name:		rovclock
Version:	0.6e
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://www.hasw.net/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	bebd45ee75fd95c5e52bdad17076988d
URL:		http://www.hasw.net/linux/
ExclusiveArch:	%{ix86} %{x8664} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Radeon overclocking utility.

%description -l pl.UTF-8
Narzędzie do zmiany częstotliwości pracy chipsetów Radeon.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
