%global packname  ergm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.4_3
Release:          1
Summary:          Fit, Simulate and Diagnose Exponential-Family Models for Networks
Group:            Sciences/Mathematics
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.4-3.tar.gz
Requires:         R-network R-nlme R-trust R-coda R-KernSmooth R-sna R-Rglpk
Requires:         R-robustbase R-Matrix 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-network
BuildRequires:    R-nlme R-trust R-coda R-KernSmooth R-sna R-Rglpk
BuildRequires:    R-robustbase R-Matrix 

%description
An integrated set of tools to analyze and simulate networks based on
exponential-family random graph models (ERGM). "ergm" is a part of the
"statnet" suite of packages for network analysis.  For a list of functions
type: help(package='ergm')

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/inst
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/help
