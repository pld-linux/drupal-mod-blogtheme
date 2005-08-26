%define		modname blogtheme
Summary:	Drupal Blog Theme Module
Summary(pl):	Modu³ Drupal Blog Theme
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	a527f9efc6ec532748104e7e2904927d
URL:		http://drupal.org/node/19248
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_moddir		%{_datadir}/drupal/modules

%description
Blog theme allows users to have persistent themes for their blogs
based on the theme they choose for their account. When others view
their main blog page, or any node created by them, the reader will see
the author's theme instead of their own. 

The module works by using the hook_init function and setting the
$custom_theme global variable to the node/blog owner's theme.

%description -l pl
Blog theme pozwala u¿ytkownikom mieæ trwa³e motywy dla swoich blogów w
oparciu o motyw wybrany dla w³asnego konta. Kiedy inni ogl±daj± ich
g³ówn± stronê bloga lub dowolny utworzony wêze³, czytelnik zobaczy
motyw autora zamiast w³asnego.

Modu³ dzia³a poprzez u¿ycie funkcji hook_init i ustawienie zmiennej
globalnej $custom_theme na motyw w³a¶ciciela wêz³a/bloga.

%prep
%setup -q -n %{modname}

rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
