package eu.pineman.chall.aoc2020;

import org.javatuples.Pair;
import org.javatuples.Triplet;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OneTest {
    @Test
    void partOne() throws IOException {
        assertEquals(691771, One.partOne(One.getInput(), 2020));
    }

    @Test
    void partTwo() throws IOException {
        assertEquals(232508760, One.partTwo(One.getInput(), 2020));
    }

    @Test
    void partOneBigBoy() throws IOException {
        assertEquals(1939883877222459L, One.partOne(One.getBigBoy(), 99920044L));
    }

    // Not working due to not using BigInts
//    @Test
//    void partTwoBigBoy() throws IOException {
//        assertEquals(32625808479480099854130L, One.partTwo(One.getBigBoy(), 99920044L));
//    }

    public static Object[][] twoSum() {
        return new Object[][]{
                {Pair.with(50L, 50L), new long[]{50L, 50L}, 100L},
                {Pair.with(50L, 50L), new long[]{50L, 50L, 1L}, 100L},
                {Pair.with(-1L, -1L), new long[]{50L, 50L, 1L}, 110L},
        };
    }

    public static Object[][] threeSum() {
        return new Object[][]{
                {Triplet.with(30L, 30L, 30L), new long[]{30L, 30L, 30L}, 90L},
                {Triplet.with(30L, 30L, 30L), new long[]{30L, 30L, 1L, 30L}, 90L},
                {Triplet.with(0L, -1L, -1L), new long[]{30L, 30L, 1L, 30L}, 100L},
        };
    }

    @ParameterizedTest
    @MethodSource("twoSum")
    void twoSum(Pair<Long, Long> expected, long[] input, long target) {
        assertEquals(expected, One.twoSum(input, target));
    }

    @ParameterizedTest
    @MethodSource("threeSum")
    void threeSum(Triplet<Long, Long, Long> expected, long[] input, long target) {
        assertEquals(expected, One.threeSum(input, target));
    }
}