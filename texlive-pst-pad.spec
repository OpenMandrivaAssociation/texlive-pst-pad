%global tl_name pst-pad
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3b
Release:	%{tl_revision}.1
Summary:	Draw simple attachment systems with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-pad
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pad.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pad.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pad.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package collects a set of graphical elements based on PStricks that
can be used to facilitate display of attachment systems such as two
differently shaped surfaces with or without a fluid wedged in between.
These macros ease the display of wet adhesion models and common friction
systems such as boundary lubrication, elastohydrodynamic lubrication and
hydrodynamic lubrication.

