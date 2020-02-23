package eu.pineman.learn.scratch;

import java.io.IOException;
import java.net.URL;

class App {
    public static void main(String[] args) throws IOException {
        System.out.println("Hello!");
        System.out.println(new String(new URL("https://www.pineman.eu").openConnection().getInputStream().readAllBytes()));
        // TODO: chamar C
        System.out.println("Goodbye!");
    }
}
