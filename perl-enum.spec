#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	enum
%define		pnam	enum
Summary:	enum - C style enumerated types and bitmask flags in Perl
Summary(pl):	enum - typy wyliczeniowe w stylu C i znaczniki bitowe dla Perla
Name:		perl-enum
Version:	1.016
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	aace7ee8648e5d20c0e81f5a51cb6604
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
enum defines a set of symbolic constants with ordered numeric values
ala C enum types.

%description -l pl
enum definiuje zestaw stałych symbolicznych o uporządkowanych
wartościach numerycznych, podobnie do typów enum w C.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/enum.pm
%{_mandir}/man3/*
