Name:		texlive-luasseq
Version:	20180303
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
%{_texmfdistdir}/scripts/luasseq
%{_texmfdistdir}/tex/lualatex/luasseq
%doc %{_texmfdistdir}/doc/lualatex/luasseq
#- source
%doc %{_texmfdistdir}/source/lualatex/luasseq

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
