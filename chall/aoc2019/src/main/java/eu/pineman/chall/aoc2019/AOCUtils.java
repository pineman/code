package eu.pineman.chall.aoc2019;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public final class AOCUtils {
    private AOCUtils() {
        throw new UnsupportedOperationException();
    }

    static Stream<String> fileLinesStream(Path path) {
        try (Stream<String> stringStream = Files.lines(path)) {
            return stringStream; // TODO: try-with-resources will close the stream before returning!! hence the error
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1); // TODO: not worth catching exceptions if you're not doing anything with them!
        }
        return null;
    }
    static List<String> fileLinesList(Path path) {
       return fileLinesStream(path).collect(Collectors.toList());
    }
}
