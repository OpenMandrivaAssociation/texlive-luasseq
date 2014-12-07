# revision 20467
# category Package
# catalog-ctan /macros/luatex/latex/luasseq
# catalog-date 2010-11-14 10:49:57 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-luasseq
Version:	2.1
Release:	9
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

%description
The package is an update of the author's sseq package, for use
with LuaLaTeX. This version uses less memory, and operates
faster than the original; it also offers several enhancements.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/luasseq/luasseq.lua
%{_texmfdistdir}/tex/lualatex/luasseq/luasseq.sty
%doc %{_texmfdistdir}/doc/lualatex/luasseq/luasseq.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/luasseq/luasseq.dtx
%doc %{_texmfdistdir}/source/lualatex/luasseq/luasseq.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 753590
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 718929
- texlive-luasseq
- texlive-luasseq
- texlive-luasseq
- texlive-luasseq

