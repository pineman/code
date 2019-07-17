-module(problem9).
-compile(export_all).
main() ->
 run(true).
run(true) ->
A = trunc(1000*rand:uniform()), B = trunc(1000*rand:uniform()),
case Y=math:pow((1000 - A - B), 2) - math:pow(A, 2) - math:pow(B, 2) of
    Y when (A == 0) or (B == 0) -> run(true);
    Y when (Y /= 0) -> run(true);
    Y when (Y == 0) -> [A,B,(1000-A-B)]
end.
