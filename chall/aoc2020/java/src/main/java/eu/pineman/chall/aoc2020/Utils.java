package eu.pineman.chall.aoc2020;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

public class Utils {
    public static Stream<String> getInput(int day) throws IOException {
        return Files.lines(Path.of("../input/" + day + "/input"));
    }

    public static Stream<String> getBigBoy(int day) throws IOException {
        return Files.lines(Path.of("../input/" + day + "/bigboy"));
    }
}
