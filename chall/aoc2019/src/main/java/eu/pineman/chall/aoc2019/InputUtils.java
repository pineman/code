package eu.pineman.chall.aoc2019;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public final class InputUtils {
    private InputUtils() {
        throw new UnsupportedOperationException();
    }

    static Stream<String> fileLinesStream(Path path) {
        try (Stream<String> stringStream = Files.lines(path)) {
            return stringStream;
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
        return null;
    }
    static List<String> fileLinesList(Path path) {
       return fileLinesStream(path).collect(Collectors.toList());
    }
}
