%include	/usr/lib/rpm/macros.perl
Summary:	TextStructured perl module
Summary(pl):	Modu³ perla TextStructured
Name:		perl-TextStructured
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/TextStructured-%{version}.tar.gz
Patch:		perl-TextStructured-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TextStructured perl module. 

%description -l pl
Modu³ perla TextStructured.

%prep
%setup -q -n TextStructured-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Structured
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz template

%{perl_sitelib}/Text/Structured.pm
%{perl_sitelib}/Text/StructuredBase.pm
%{perl_sitearch}/auto/Text/Structured

%{_mandir}/man3/*
