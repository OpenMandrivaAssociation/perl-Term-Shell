%define upstream_name    Term-Shell
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Write command-line shells in Perl

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/shlomif/Term-Shell
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Term-Shell-%{upstream_version}.tar.gz

BuildRequires:	make
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



