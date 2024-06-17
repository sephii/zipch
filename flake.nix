{
  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells."x86_64-linux".default = pkgs.mkShell {
        packages = [
          (pkgs.python3.withPackages (pythonPackages: [
            pythonPackages.hatchling
            pythonPackages.twine
            pythonPackages.build
          ]))
        ];
      };
    };
}
