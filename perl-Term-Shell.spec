%define upstream_name    Term-Shell
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Write command-line shells in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Term/Term-Shell-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Term::Shell makes it joyfully easy to write command-line interfaces in Perl.
All the boring details like command-line parsing and terminal handling are
done for you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Term/Shell*
%{_mandir}/*/*


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 664913
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 405543
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 241963
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-1mdv2008.0
+ Revision: 22102
- 0.02


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdk
- initial Mandriva package



