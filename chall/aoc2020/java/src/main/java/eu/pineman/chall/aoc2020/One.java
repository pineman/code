package eu.pineman.chall.aoc2020;

import org.javatuples.Pair;
import org.javatuples.Triplet;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class One {
    // https://phauer.com/2019/modern-best-practices-testing-java/#dont-use-static-access-never-ever
    public static long[] getInput() throws IOException {
        return Utils.getInput(1).mapToLong(Long::parseLong).toArray();
    }

    public static long[] getBigBoy() throws IOException {
        return Utils.getBigBoy(1).mapToLong(Long::parseLong).toArray();
    }

    public static Pair<Long, Long> twoSum(long[] input, long target) {
        Arrays.sort(input);
        int l = 0, r = input.length - 1;
        while (r != l) {
            long sum = input[l] + input[r];
            if (sum == target) return Pair.with(input[r], input[l]);
            else if (sum < target) l++;
            else r--;
        }
        return Pair.with(-1L, -1L);
    }

    public static Triplet<Long, Long, Long> threeSum(long[] input, long target) {
        Arrays.sort(input);
        int i = 0;
        for (long a : input) {
            List<Long> slice = Arrays.stream(input).boxed().collect(Collectors.toList());
            slice.remove(i);
            Pair<Long, Long> ts = twoSum(slice.stream().mapToLong(s -> s).toArray(), target - a);
            if (a + ts.getValue0() + ts.getValue1() == target) {
                return Triplet.with(a, ts.getValue0(), ts.getValue1());
            }
            i++;
        }
        return Triplet.with(-1L, -1L, -1L);
    }

    public static long partOne(long[] input, long target) {
        Pair<Long, Long> sol = twoSum(input, target);
        return sol.getValue0() * sol.getValue1();
    }

    public static long partTwo(long[] input, long target) {
        Triplet<Long, Long, Long> sol = threeSum(input, target);
        return sol.getValue0() * sol.getValue1() * sol.getValue2();
    }

    public static void main(String[] args) throws IOException {
        long[] input = getInput();
        System.out.println(partOne(input, 2020));
        System.out.println(partTwo(input, 2020));

        long[] bigBoy = getBigBoy();
        System.out.println(partOne(bigBoy, 99920044));
        System.out.println(partTwo(bigBoy, 99920044));
    }
}
