{
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            (pkgs.python3.withPackages (pythonPackages: [
              pythonPackages.hatchling
              pythonPackages.twine
              pythonPackages.build
            ]))
          ];
        };

        packages.default = pkgs.python3.pkgs.callPackage ./default.nix { };
      }
    );
}
