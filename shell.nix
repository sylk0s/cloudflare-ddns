{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell rec {
    buildInputs = with pkgs; [

    ];
    TOKEN = (builtins.readFile ./token);
    ZONE = "sylkos.xyz";
    DOMAIN = "sylkos.xyz";
    FREQ = "1";
    TYPE = "A";
  }
