package eu.pineman.chall.aoc2019;

import org.testng.annotations.Test;

import java.io.IOException;

import static org.testng.Assert.assertEquals;

public class OneTest {

    @Test
    public void testPartOne() throws IOException {
        assertEquals(One.partOne(One.ONE_INPUT.get(0)), 3231195);
    }

    @Test
    public void testPartTwo() throws IOException {
        assertEquals(One.partTwo(One.ONE_INPUT.get(0)), 4843929);
    }
}