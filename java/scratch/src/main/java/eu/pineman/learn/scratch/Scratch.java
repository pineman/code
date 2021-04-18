package eu.pineman.learn.scratch;

public class Scratch {
    public static void main(String[] args) {
        short i = 1, j = 0; // short is 16 bits
        while (i != 0) {
            i >>>= 1; // >>> doesn't do sign extension
            j++;
        }
        System.out.println(j);
    }
}
