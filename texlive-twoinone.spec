%global tl_name twoinone
%global tl_revision 17024

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Print two pages on a single page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/twoinone
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/twoinone.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is for printing two pages on a single (landscape) A4 page.
Page numbers appear on the included pages, and not on the landscape
'container' page.

