using Pkg

# there's also a Pkg REPL inside the julia REPL, acessible by typing ']'
Pkg.add("PackageCompiler")

println(PROGRAM_FILE)
for x in ARGS
	println(x)
end
