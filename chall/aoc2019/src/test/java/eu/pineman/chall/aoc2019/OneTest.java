package eu.pineman.chall.aoc2019;

import org.testng.annotations.Test;

import java.io.IOException;

import static org.testng.Assert.assertEquals;

public class OneTest {

    @Test
    public void testPartOne() throws IOException {
        assertEquals(One.partOne(One.ONE_INPUT.get(0)), 3231195);
//        assertEquals(One.partOne(One.ONE_INPUT.get(1)), 333215354713524402576702855198882146075237336332924);
    }

    @Test
    public void testPartTwo() throws IOException {
        assertEquals(One.partTwo(One.ONE_INPUT.get(0)), 4843929);
//        assertEquals(One.partTwo(One.ONE_INPUT.get(1)), 499823032070286603865054282798323219112855683207018);
    }
}
