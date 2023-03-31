Name:		texlive-pst-pad
Version:	15878
Release:	2
Summary:	Draw simple attachment systems with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-pad
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pad.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pad.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pad.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package collects a set of graphical elements based on
PStricks that can be used to facilitate display of attachment
systems such as two differently shaped surfaces with or without
a fluid wedged in between. These macros ease the display of wet
adhesion models and common friction systems such as boundary
lubrication, elastohydrodynamic lubrication and hydrodynamic
lubrication.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-pad/pst-pad.tex
%{_texmfdistdir}/tex/latex/pst-pad/pst-pad.sty
%doc %{_texmfdistdir}/doc/generic/pst-pad/CHANGES
%doc %{_texmfdistdir}/doc/generic/pst-pad/README
%doc %{_texmfdistdir}/doc/generic/pst-pad/pst-pad-doc-header.tex
%doc %{_texmfdistdir}/doc/generic/pst-pad/pst-pad-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-pad/pst-pad-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-pad/pst-pad-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-pad/pst-pad-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-pad/showexpl.cfg
#- source
%doc %{_texmfdistdir}/source/generic/pst-pad/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
