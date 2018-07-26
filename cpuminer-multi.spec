%global gittag0 %{version}-multi

Name:           cpuminer-multi
Version:        1.3.5
Release:        2%{?dist}
Summary:        Multi-threaded CPU miner
License:        GPLv2 and GPLv3
URL:            https://github.com/tpruvot/%{name}

Source0:        https://github.com/tpruvot/%{name}/archive/v%{gittag0}.tar.gz#/%{name}-%{gittag0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  jansson-devel
BuildRequires:  libcurl-devel >= 7.15.2
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  mpir-devel
BuildRequires:  openssl-devel

Provides:       cpuminer = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Currently supported
    ✓ scrypt (Litecoin, Dogecoin, Feathercoin, ...)
    ✓ scrypt:N
    ✓ scrypt-jane:N
    ✓ sha256d (Bitcoin, Freicoin, Peercoin/PPCoin, Terracoin, ...)
    ✓ axiom (Axiom Shabal-256 based MemoHash)
    ✓ bastion (Joincoin [J])
    ✓ bitcore Permuted serie of 10 algos (BitCore)
    ✓ blake (Saffron [SFR] Blake-256)
    ✓ blake2s (NevaCoin Blake2-S 256)
    ✓ bmw (Midnight [MDT] BMW-256)
    ✓ cryptonight (Bytecoin [BCN], Monero [XMR])
    ✓ cryptonight-light (Aeon)
    ✓ decred (Blake256-14 [DCR])
    ✓ dmd-gr (Diamond-Groestl)
    ✓ fresh (FreshCoin)
    ✓ groestl (Groestlcoin)
    ✓ jha (JackpotCoin, SweepStake)
    ✓ lbry (LBRY Credits [LBC])
    ✓ lyra2RE (Cryptocoin)
    ✓ lyra2REv2 (VertCoin [VTC])
    ✓ myr-gr Myriad-Groestl (MyriadCoin [MYR])
    ✓ neoscrypt (Feathercoin)
    ✓ nist5 (MistCoin [MIC], TalkCoin [TAC], ...)
    ✓ pentablake (Joincoin)
    ✓ pluck (Supcoin [SUP])
    ✓ quark (Quarkcoin)
    ✓ qubit (GeoCoin)
    ✓ skein (Skeincoin, Myriadcoin, Xedoscoin, ...)
    ✓ skein2 (Woodcoin)
    ✓ s3 (OneCoin)
    ✓ sia (Reversed Blake2B for SIA [SC])
    ✓ sib X11 + gost streebog (SibCoin)
    ✓ timetravel Permuted serie of 8 algos (MachineCoin [MAC])
    ✓ tribus 3 of the top NIST5 algos (Denarius [DNR])
    ✓ vanilla (Blake-256 8-rounds - double sha256 [VNL])
    ✓ veltor (Veltor [VLT])
    ✓ xevan x17 x 2 on bigger header (BitSend [BSD])
    ✓ x11evo (Revolver [XRE])
    ✓ x11 (Darkcoin [DRK], Hirocoin, Limecoin, ...)
    ✓ x12 (GalaxyCash [GCH])
    ✓ x13 (Sherlockcoin, [ACE], [B2B], [GRC], [XHC], ...)
    ✓ x14 (X14, Webcoin [WEB])
    ✓ x15 (RadianceCoin [RCE])
    ✓ x16r (Ravencoin [RVN])
    ✓ x16s (Pigeoncoin [PGN])
    ✓ x17 (Verge [XVG])
    ✓ yescrypt (GlobalBoostY [BSTY], Unitus [UIS], MyriadCoin [MYR])
    ✓ zr5 (Ziftrcoin [ZRC])
Implemented, but untested
    ? hefty1 (Heavycoin)
    ? keccak (Maxcoin HelixCoin, CryptoMeth, Galleon, 365coin, Slothcoin, BitcointalkCoin)
    ? keccakc (Creativecoin)
    ? luffa (Joincoin, Doomcoin)
    ? shavite3 (INKcoin)

%prep
%autosetup -p1 -n %{name}-%{gittag0}

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
autoreconf -vif
%configure --with-crypto --with-curl

%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%{_bindir}/cpuminer
%{_mandir}/man1/cpuminer.1*

%changelog
* Thu Jul 26 2018 Simone Caronni <negativo17@gmail.com> - 1.3.5-2
- Update to final 1.3.5 release.

* Wed Jul 18 2018 Simone Caronni <negativo17@gmail.com> - 1.3.5-1.20180714git41da2b4
- Update to 1.3.5 snapshot.

* Fri Jun 16 2017 Simone Caronni <negativo17@gmail.com> - 1.3.1-2
- Provide cpuminer.

* Wed Jun 14 2017 Simone Caronni <negativo17@gmail.com> - 1.3.1-1
- First build.
