%include	/usr/lib/rpm/macros.perl
Summary:	TextStructured perl module
Summary(pl):	Modu³ perla TextStructured
Name:		perl-TextStructured
Version:	0.02
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Text/TextStructured-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README template
%{perl_sitelib}/Text/Structured.pm
%{perl_sitelib}/Text/StructuredBase.pm
%{_mandir}/man3/*
