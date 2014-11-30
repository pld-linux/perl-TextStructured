#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	TextStructured
%include	/usr/lib/rpm/macros.perl
Summary:	TextStructured perl module
Summary(pl.UTF-8):	Moduł Perla TextStructured
Name:		perl-TextStructured
Version:	0.02
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/TextStructured-%{version}.tar.gz
# Source0-md5:	dd7937a44d09b0206f942e6dc4b57e20
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/TextStructured/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TextStructured perl module.

%description -l pl.UTF-8
Moduł Perla TextStructured.

%prep
%setup -q -n TextStructured-%{version}
%patch0 -p0

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
%doc README template
%{perl_vendorlib}/Text/Structured.pm
%{perl_vendorlib}/Text/StructuredBase.pm
%{_mandir}/man3/*
