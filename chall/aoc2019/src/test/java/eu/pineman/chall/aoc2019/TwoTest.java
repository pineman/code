package eu.pineman.chall.aoc2019;

import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import static eu.pineman.chall.aoc2019.Two.runIntcode;

public class TwoTest {

    @DataProvider(name = "partOnePrograms")
    public Object[][] testRunIntcodePrograms() {
        int[] code1 = {1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50};
        int[] result1 = {3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50};
        int[] code2 = {1, 0, 0, 0, 99};
        int[] result2 = {2, 0, 0, 0, 99};
        int[] code3 = {2, 3, 0, 3, 99};
        int[] result3 = {2, 3, 0, 6, 99};
        int[] code4 = {2, 4, 4, 5, 99, 0};
        int[] result4 = {2, 4, 4, 5, 99, 9801};
        int[] code5 = {1, 1, 1, 4, 99, 5, 6, 0, 99};
        int[] result5 = {30, 1, 1, 4, 2, 5, 6, 0, 99};
        return new Object[][]{
                {code1, result1},
                {code2, result2},
                {code3, result3},
                {code4, result4},
                {code5, result5},
        };
    }

    @Test(dataProvider = "partOnePrograms")
    public void testRunIntcode(int[] code, int[] result) {
        runIntcode(code);
        Assert.assertEquals(code, result);
    }
}