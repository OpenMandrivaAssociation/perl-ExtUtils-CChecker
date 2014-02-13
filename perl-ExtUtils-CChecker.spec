%define upstream_name    ExtUtils-CChecker
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Configure-time utilities for using C headers,
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/ExtUtils-CChecker-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildArch: noarch

%description
Often Perl modules are written to wrap functionallity found in existing C
headers, libraries, or to use OS-specific features. It is useful in the
_Build.PL_ or _Makefile.PL_ file to check for the existance of these
requirements before attempting to actually build the module.

Objects in this class provide an extension around the ExtUtils::CBuilder
manpage to simplify the creation of a _.c_ file, compiling, linking and
running it, to test if a certain feature is present.

It may also be necessary to search for the correct library to link against,
or for the right include directories to find header files in. This class
also provides assistance here.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Mar 26 2012 Götz Waschk <waschk@mandriva.org> 0.80.0-1mdv2012.0
+ Revision: 786887
- update build deps
- new version

* Sat Apr 16 2011 Götz Waschk <waschk@mandriva.org> 0.70.0-1
+ Revision: 653366
- update build deps
- update to new version 0.07

* Fri Jan 14 2011 Götz Waschk <waschk@mandriva.org> 0.60.0-1
+ Revision: 631034
- update to new version 0.06

* Wed Nov 10 2010 Götz Waschk <waschk@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 595566
- update to new version 0.05

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 550295
- update to new version 0.04

* Tue Mar 02 2010 Götz Waschk <waschk@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 513328
- new version
- fix source URL

* Sat Jan 30 2010 Götz Waschk <waschk@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 498473
- import perl-ExtUtils-CChecker


* Sat Jan 30 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

