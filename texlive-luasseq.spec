# revision 20467
# category Package
# catalog-ctan /macros/luatex/latex/luasseq
# catalog-date 2010-11-14 10:49:57 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-luasseq
Version:	2.1
Release:	1
Summary:	Drawing spectral sequences in LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luasseq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luasseq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luasseq.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luasseq.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is an update of the author's sseq package, for use
with LuaLaTeX. This version uses less memory, and operates
faster than the original; it also offers several enhancements.

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
%{_texmfdistdir}/scripts/luasseq/luasseq.lua
%{_texmfdistdir}/tex/lualatex/luasseq/luasseq.sty
%doc %{_texmfdistdir}/doc/lualatex/luasseq/luasseq.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/luasseq/luasseq.dtx
%doc %{_texmfdistdir}/source/lualatex/luasseq/luasseq.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
