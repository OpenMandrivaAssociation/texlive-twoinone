Name:		texlive-twoinone
Version:	17024
Release:	2
Summary:	Print two pages on a single page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/twoinone
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
