package eu.pineman.chall.aoc2019;

import java.util.stream.Stream;

public class One {
    public static void main(String[] args) {
        Stream<String> input = Utils.readFileLines("input/1/input.txt");
        System.out.println(partOne(input));
        System.out.println(partTwo(input));
    }

    private static long calcFuel(Stream<String> modules) {
//        lines.forEach(line -> {
//            res += Long.parseLong(line) / 3 - 2;
//        });
        return modules.mapToLong(One::calcModuleFuel).sum();
    }

    private static long calcModuleFuel(long moduleMass) {
        return moduleMass / 3 - 2;
    }

    private static long calcModuleFuel(String moduleMass) {
        return calcModuleFuel(Long.parseLong(moduleMass));
    }

    private static long partOne(Stream<String> lines) {
        return calcFuel(lines);
    }

    private static long partTwo(Stream<String> lines) {
        long fuelModuleMass = calcFuel(lines);
        long totalFuel = fuelModuleMass;
        while (fuelModuleMass > 0) {
            fuelModuleMass = calcModuleFuel(fuelModuleMass);
            totalFuel += fuelModuleMass;
        }
        return totalFuel;
    }
}
