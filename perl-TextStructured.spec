%include	/usr/lib/rpm/macros.perl
Summary:	TextStructured perl module
Summary(pl):	Modu³ perla TextStructured
Name:		perl-TextStructured
Version:	0.02
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/TextStructured-%{version}.tar.gz
# Source0-md5:	dd7937a44d09b0206f942e6dc4b57e20
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README template
%{perl_vendorlib}/Text/Structured.pm
%{perl_vendorlib}/Text/StructuredBase.pm
%{_mandir}/man3/*
