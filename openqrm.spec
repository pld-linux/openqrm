%define	_date	20060208
Summary:	Data Center Management Platform
Summary(pl.UTF-8):	Platforma do zarządzania centrum informacji
Name:		openqrm
Version:	2.1
Release:	0.1
License:	Qlusters Public License
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/openqrm/%{name}-%{version}_DATE%{_date}.src.tgz
# Source0-md5:	49716889ec80c9be9a764d2d91ce6160
URL:		http://www.openqrm.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
openQRM is an open source systems management platform which integrates
with existing components in enterprise data centers. openQRM is
derived from a proven commercial product and distributed under a
modified Mozilla Public License.

%description -l pl.UTF-8
openQRM to mająca otwarte źródła platforma zarządzania systemami
integrująca się z istniejącymi komponentami w centrach informacji
klasy enterprise. openQRM wywodzi się ze sprawdzonego komercyjnego
produktu i jest rozprowadzane na zmodyfikowanej licencji Mozilla
Public License.

%prep
%setup -q -n %{name}-%{version}_DATE%{_date}-123420

%build
cd src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/LICENSE
