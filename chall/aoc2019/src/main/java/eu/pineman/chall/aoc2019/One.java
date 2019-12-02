package eu.pineman.chall.aoc2019;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public abstract class One {
    final static List<Path> ONE_INPUT = Stream.of(
            "input/1/input.txt"
//            "input/1/bigboyinput.txt"
    ).map(Paths::get).collect(Collectors.toList());

    public static void main(String[] args) throws IOException {
        for (Path path : ONE_INPUT) {
            System.out.println(partOne(path));
            System.out.println(partTwo(path));
        }
    }

    static long partOne(Path input) throws IOException {
        return Files.lines(input).mapToLong(One::calcFuel).sum();
    }

    static long partTwo(Path input) throws IOException {
        partTwoIterative(input);
        return partTwoRecursive(input);
    }

    private static long partTwoIterative(Path input) throws IOException {
        return Files.lines(input).mapToLong(One::calcFuelTotal).sum();
    }

    private static long partTwoRecursive(Path input) throws IOException {
//        try (Stream<String> lines = Files.lines(input)) {
//            return lines.mapToLong(line -> calcFuelTotalRecursive(Long.parseLong(line))).sum();
//        }
//        catch (IOException e) {
//            e.printStackTrace();
//            System.exit(1);
//        }
//        return 0;

        return Files.lines(input).mapToLong(line -> calcFuelTotalRecursive(Long.parseLong(line))).sum();
    }

    private static long calcFuelTotalRecursive(long mass) {
        long step = calcFuel(mass);
        if (step <= 0) { return 0; }
        return step + calcFuelTotalRecursive(step);
    }

    private static long calcFuel(long mass) {
        return mass / 3 - 2;
    }

    private static long calcFuel(String mass) {
        return calcFuel(Long.parseLong(mass));
    }

    private static long calcFuelTotal(String line) {
        long moduleMass = calcFuel(line);
        long totalModuleMass = 0;
        while (moduleMass > 0) {
            totalModuleMass += moduleMass;
            moduleMass = calcFuel(moduleMass);
        }
        return totalModuleMass;
    }
}
