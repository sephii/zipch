{
  buildPythonPackage,
  fetchFromGitHub,
  hatchling,
}:
buildPythonPackage rec {
  pname = "zipch";
  version = "2.1.0";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "sephii";
    repo = "zipch";
    rev = version;
    hash = "sha256-nsp4XotizPaXY3p7CrUvHt4JVRwkMdaEVa8TqaVRfHU=";
  };

  build-system = [ hatchling ];

  pythonImportsCheck = [ "zipch" ];
}
