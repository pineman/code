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
        for (int i = 0; i < code.length; i += 4) {
            switch (code[i]) {
                case 1:
                    code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]];
                    break;
                case 2:
                    code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]];
                    break;
                case 99:
                    break loop;
                default:
                    break;
            }
        }
    }
}
