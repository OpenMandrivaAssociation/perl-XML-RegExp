%define modname	XML-RegExp
%define modver 0.04

Summary:	XML::RegExp - regular expressions for XML tokens
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/XML-RegExp-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This package contains regular expressions for the following XML
tokens:	BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar,
NameChar, EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/RegExp.pm
%{_mandir}/man3/*


