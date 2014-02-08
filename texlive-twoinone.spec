# revision 17024
# category Package
# catalog-ctan /macros/latex/contrib/twoinone
# catalog-date 2010-02-26 11:17:49 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-twoinone
Version:	20100226
Release:	3
Summary:	Print two pages on a single page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/twoinone
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is for printing two pages on a single (landscape)
A4 page. Page numbers appear on the included pages, and not on
the landscape 'container' page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/twoinone/2in1.sty
%doc %{_texmfdistdir}/doc/latex/twoinone/twoinone.pdf
%doc %{_texmfdistdir}/doc/latex/twoinone/twoinone.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100226-2
+ Revision: 757160
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100226-1
+ Revision: 719819
- texlive-twoinone
- texlive-twoinone
- texlive-twoinone

