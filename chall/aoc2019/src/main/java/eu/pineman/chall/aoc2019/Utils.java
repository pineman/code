package eu.pineman.chall.aoc2019;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Utils {
    static Stream<String> readFileLines(String path) {
        try (Stream<String> stringStream = Files.lines(Paths.get(path))) {
            return stringStream;
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
        return null;
    }
    static List<String> readFileLinesList(String path) {
       return readFileLines(path).collect(Collectors.toList());
    }
}
