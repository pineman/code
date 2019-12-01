package eu.pineman.chall.aoc2019;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public abstract class One {
    static List<Path> ONE_INPUT = Arrays.asList(
        "input/1/input.txt"
    ).stream().map(Paths::get).collect(Collectors.toList());

    public static void main(String[] args) throws IOException {
        for (Path path : ONE_INPUT) {
            System.out.println(partOne(path));
            System.out.println(partTwo(path));
        }
    }

    static long partOne(Path input) throws IOException {
        return Files.lines(input).mapToLong(line -> Long.parseLong(line) / 3 - 2).sum();
    }

    static long partTwo(Path input) throws IOException {
        return Files.lines(input).mapToLong(line -> {
            long moduleMass = Long.parseLong(line) / 3 - 2;
            long totalModuleMass = 0;
            while (moduleMass > 0) {
                totalModuleMass += moduleMass;
                moduleMass = moduleMass / 3 - 2;
            }
            return totalModuleMass;
        }).sum();
    }
}
