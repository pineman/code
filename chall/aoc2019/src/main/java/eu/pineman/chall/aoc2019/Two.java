package eu.pineman.chall.aoc2019;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public abstract class Two {
    final static List<Path> TWO_INPUT = Stream.of(
            "input/2/input.txt"
//            "input/2/bigboyinput.txt"
    ).map(Paths::get).collect(Collectors.toList());

    public static void main(String[] args) throws IOException {
        for (Path path : TWO_INPUT) {
            System.out.println(partOne(path));
        }
    }

    static int partOne(Path path) throws IOException {
//        String[] stringCode = Files.asCharSource(path.toFile(), Charsets.UTF_8).readFirstLine().split(","); // Guava
        String[] stringCode = Files.lines(path).map(s -> s.split(",")).findFirst().orElseThrow();

        int[] code = Arrays.stream(stringCode).mapToInt(Integer::parseInt).toArray();

        code[1] = 12;
        code[2] = 2;

        runIntcode(code);

        System.out.println(Arrays.toString(code));

        return code[0];
    }

    static void runIntcode(int[] code) {
        loop:
        for (int ip = 0; ip < code.length; ip += 4) {
            switch (code[ip]) {
                case 1:
                    code[code[ip + 3]] = code[code[ip + 1]] + code[code[ip + 2]];
                    break;
                case 2:
                    code[code[ip + 3]] = code[code[ip + 1]] * code[code[ip + 2]];
                    break;
                case 99:
                    break loop;
                default:
                    break;
            }
        }
    }

    static int partTwo(Path path) {
//        Some ways to solve part two:
//         1. brute force O(n^2)
//         2. saddleback search
//        "notice that the function (program) is strictly increasing (i.e f(n,m) < f(n+1,m) and f(n,m) < f(n, m+1)) since
//        it is a composition of addition and multiplication of positive integers.
//        now consider the possible values as a 100 x 100 matrix where the entries are f(i,j)
//        since the matrix is sorted columnwise (M[i,j] < M[i, j+1]) and row-wise (M[i,j] < M[i+1,j]) we can use a saddleback search
//        this is where we start at the bottom left corner of the matrix. if the value there is less than what we're
//        looking for, move right (since it can't be in that column). if it's less, move up (since it can't be in that row)
//        repeat
//        this is O(n+m) and takes roughly 56 (iirc) calls to f(n,m) rather than 2255"
//         3. gradient descent https://pastebin.com/gri8k4Tf
//        "for what it's worth, gradient descent is overkill here, because the function he gave us,
//        f(x, y) = program(noun, verb) = output is not complex at all, it's actually just a linear 2d plane. it's not "bumpy"."
//         4. symbolic arithmetic: 'reverse-engineer' the program symbolically and solve it since its just a function of x and y.
//        what about potential halts tho? some solutions may write a halt instruction somewhere terminating the program
//        early before the desired value is in the 0 position
        return 0;
    }
}
