%define upstream_name    XML-RegExp
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	XML::RegExp - regular expressions for XML tokens
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This package contains regular expressions for the following XML
tokens: BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar,
NameChar, EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/RegExp.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-4mdv2012.0
+ Revision: 765849
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-3
+ Revision: 764373
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-2
+ Revision: 667454
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 401854
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.03-8mdv2009.1
+ Revision: 351672
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.03-7mdv2009.0
+ Revision: 224639
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.03-6mdv2008.1
+ Revision: 180658
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03-5mdv2008.0
+ Revision: 25467
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.03-4mdv2008.0
+ Revision: 23246
- rebuild


* Mon Apr 03 2006 Buchan Milne <bgmilne@mandriva.org> 0.03-3mdk
- Rebuild
- use mkrel

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-2mdk
- fix deps

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package

