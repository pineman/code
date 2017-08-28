program leeter;

{$mode objfpc}
{$H+}

uses
	Classes, Sysutils;

var
	infile, outfile, stdinput: Text;
	input_sentence: string;
	i: integer;
	{ User-defined options }
	INPUTFILE, OUTPUTFILE, DISPLAY: string;
	INTERACTIVE, STDIN: boolean;

{ Program constants }
const
	version = '1.0.0';
	help = 'Usage: leeter [FILE] [-o OUTPUT]' + #13#10 +
		   'Basic text to leetspeak conversion.' + #13#10 + #13#10 +
		   '  -f, --file FILE    Read text from FILE' + #13#10 +
		   '  -o, --output FILE  Write to FILE instead of stdout' + #13#10 +
		   '  -i, --interactive  Run interactively' + #13#10 +
		   '      --help         Display this help and exit' + #13#10 +
		   '      --version      Display version and exit' + #13#10 + #13#10 +
		   'If no file is specified, reads from stdin.';


{ Function that takes a string and returns it converted to 1337speak }
function convert_text(var sentence: string) : string;
var conv, e, curr: string;
begin
	conv:=''; e:=''; curr:='';
	{write('evaluating: ' + sentence); writeln(length(sentence));}

	{ Fix for single word sentences }
	sentence:=sentence + ' ';

	for i:=1 to length(sentence) do begin
		if sentence[i] <> ' ' then begin
			curr:=curr + sentence[i];
			continue;
		end;
		case curr of
			'cool': e:=e + 'k3wl ';
			'hacker', 'hackers': e:=e + 'h4xx0rz';
			'leet': e:=e + '1337 ';
			'elite': e:=e + '31337 ';
			'the': e:=e + 't3h ';
			'owned': e:=e + '0wnd ';
			'best': e:=e + 'pwnZ ';
			'pwned', 'powned': e:=e + 'pwnt ';
			'skills': e:=e + 'skillz ';
			'you': e:=e + 'j00 ';
			'sucks','suck': e:=e + 'suxx0rz ';
			'thanks': e:=e + 'kthx ';
			'lol': e:=e + 'lulz ';
		else e:=e + curr + ' ';
		end;
		curr:='';
	end;
	{writeln('evaled: ' + e);}

	for i:=1 to length(e) do begin
		case e[i] of
			'o','O': conv:=conv + '0';
			'a', 'á', 'à', 'ã': conv:=conv + '4';
			'A', 'Á', 'À', 'Ã': conv:=conv + '@';
			'i','I': conv:=conv + '1';
			'e': conv:=conv + '3';
			'z', 'Z': conv:=conv + 'zZ';
			'w', 'W': conv:=conv + '\/\/';
		else conv:=conv + e[i];
		end;
	convert_text:=conv;
	end;
end;


{ Procedure to parse the arguments/options the user defined }
procedure argparse();
var
	count: integer;
begin
	count:=ParamCount;

	{ If the user didn't define parameters, read from stdin }
	if count = 0 then
		STDIN:=true

	else begin
		{ Parse options and arguments the user defined }
		i:=1;
		while i <= count do begin
			case ParamStr(i) of
				'-i', '--interactive':
					INTERACTIVE:=true;
				'-f', '--file': begin
					INPUTFILE:=ParamStr(i+1);
					i:=i+2;
					continue;
					end;
				'-o', '--output': begin
					OUTPUTFILE:=ParamStr(i+1);
					i:=i+2;
					continue;
					end;
				'--help':
					DISPLAY:='help';
				'--version':
					DISPLAY:='version';
				else
					DISPLAY:='error';
			end; {case}
			i := i+1;
		end; {while}
	end; {else}
end;

procedure run_from_stdin();
begin
	Assign(stdinput, '');
	reset(stdinput);
	while not eof(stdinput) do begin
		readln(stdinput, input_sentence);
		writeln(convert_text(input_sentence));
	end;
	close(stdinput);
end;


procedure run_interactive();
begin
	writeln('Convert text to leetspeak.');
	writeln('Gimme some text. Type "exit" to quit.');
	while input_sentence <> 'exit' do begin
		write('>>> ');
		readln(input_sentence);
		if input_sentence <> 'exit' then begin
			writeln(convert_text(input_sentence));
		end;
	end;
end;


procedure run_from_file();
begin
	{ Sanity checks }
	if ( (INPUTFILE = '') and (OUTPUTFILE <> '') )
		  or (INPUTFILE = '') then begin

		writeln('leeter: No input specified.' + #13#10 +
			'Try --help for more information.');
	end
	else begin
		{$I+}
		try
			AssignFile(infile, INPUTFILE);
			Reset(infile);
			if OUTPUTFILE <> '' then begin
				AssignFile(outfile, OUTPUTFILE);
				Rewrite(outfile);
				repeat
					readln(infile, input_sentence);
					WriteLn(outfile, convert_text(input_sentence));
				until Eof(infile);
				CloseFile(outfile);
				CloseFile(infile);
				writeln('Saved to file: ' + OUTPUTFILE);
			end
			else begin
				repeat
					readln(infile, input_sentence);
					writeln(convert_text(input_sentence));
				until Eof(infile);
				CloseFile(infile);
		end;
		except on E: EInOutError do
			begin
			writeln('Error: ');
			writeln(E.ClassName + ' ' + E.Message);
			end; {except}
		end; {try}
	end; {else}
end;


begin
	{ Parse args and act accordingly }
	argparse();

	{ Program is running without parameters.
	  Defaults to read from stdin. }
	if STDIN = true then
		run_from_stdin()

	else begin
	{ The user defined parameters. }
	{ Act according to them. }

	{ Display help or version if we need to and
	don't do anything else. }
		case DISPLAY of
			'help': writeln(help);
			'version': writeln('leeter ' + version);
			'error': writeln('leeter: Unknown option specified.' + #13#10 +
							 'Try ''leeter --help'' for more information.');

		{ Else, start normal execution. }
			else begin
				if INTERACTIVE=true then
					run_interactive()
				else
					run_from_file();
			end;
		end; {case}
	end; {else}
end.
