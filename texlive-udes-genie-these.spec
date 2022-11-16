Name:		texlive-udes-genie-these
Version:	64509
Release:	1
Summary:	A thesis class file for the Faculte de genie at the Universite de Sherbrooke
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/udes-genie-these
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/udes-genie-these.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/udes-genie-these.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/udes-genie-these.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The udes-genie-these class can be used for Ph.D. theses,
master's theses and project definitions at the Faculte de genie
of the Universite de Sherbrooke (Quebec, Canada). The class
file is coherent with the latest version of the Protocole de
redaction aux etudes superieures which is available on the
faculte's intranet. The class file documentation is in French,
the language of the typical user at the Universite de
Sherbrooke. An example of use is also distributed with the
documentation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/udes-genie-these
%{_texmfdistdir}/tex/latex/udes-genie-these
%doc %{_texmfdistdir}/doc/latex/udes-genie-these

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
