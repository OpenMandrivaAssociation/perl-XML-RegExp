%define modname	XML-RegExp
Summary:	XML::RegExp - regular expressions for XML tokens
Name:		perl-%{modname}
Version:	0.04
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/XML-RegExp-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
This package contains regular expressions for the following XML
tokens:	BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar,
NameChar, EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

%prep
%setup -qn %{modname}-%{version}

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


