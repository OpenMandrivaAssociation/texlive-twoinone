# revision 17024
# category Package
# catalog-ctan /macros/latex/contrib/twoinone
# catalog-date 2010-02-26 11:17:49 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-twoinone
Version:	20100226
Release:	1
Summary:	Print two pages on a single page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/twoinone
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is for printing two pages on a single (landscape)
A4 page. Page numbers appear on the included pages, and not on
the landscape 'container' page.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/twoinone/2in1.sty
%doc %{_texmfdistdir}/doc/latex/twoinone/twoinone.pdf
%doc %{_texmfdistdir}/doc/latex/twoinone/twoinone.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
