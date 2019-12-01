# Package

version       = "0.1.0"
author        = "João Pinheiro"
description   = "A new awesome nimble package"
license       = "MIT"
srcDir        = "src"
bin           = @["one_nim"]

backend       = "cpp"

# Dependencies

requires "nim >= 1.0.2"
requires "bignum >= 1.0.4"
