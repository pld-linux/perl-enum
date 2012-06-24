%include	/usr/lib/rpm/macros.perl
%define		pdir	enum
%define		pnam	enum
Summary:	enum Perl module
Summary(cs):	Modul enum pro Perl
Summary(da):	Perlmodul enum
Summary(de):	enum Perl Modul
Summary(es):	M�dulo de Perl enum
Summary(fr):	Module Perl enum
Summary(it):	Modulo di Perl enum
Summary(ja):	enum Perl �⥸�塼��
Summary(ko):	enum �� ����
Summary(no):	Perlmodul enum
Summary(pl):	Modu� perla enum
Summary(pt_BR):	M�dulo Perl enum
Summary(pt):	M�dulo de Perl enum
Summary(ru):	������ ��� Perl enum
Summary(sv):	enum Perlmodul
Summary(uk):	������ ��� Perl enum
Summary(zh_CN):	enum Perl ģ��
Name:		perl-enum
Version:	1.016
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
enum defines a set of symbolic constants with ordered numeric values
ala C enum types.

%description -l pl
enum definiuje zestaw sta�ych symbolicznych o uporz�dkowanych
warto�ciach numerycznych, podobnie do typ�w enum w C.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/enum.pm
%{_mandir}/man3/*
