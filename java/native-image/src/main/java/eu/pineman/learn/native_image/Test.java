package eu.pineman.learn.native_image;

import java.io.IOException;
import java.net.URL;
import java.nio.charset.StandardCharsets;

final class Test {
    private Test () { }

    public static void main(String[] args) throws IOException {
        System.out.println("Hello!");
        System.out.println(new String(new URL("https://www.pineman.eu").openConnection().getInputStream().readAllBytes(), StandardCharsets.UTF_8));
        System.out.println("Goodbye!");
    }
}
