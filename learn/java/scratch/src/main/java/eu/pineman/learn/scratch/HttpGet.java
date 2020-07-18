package eu.pineman.learn.scratch;

import java.io.IOException;
import java.net.URL;

class HttpGet {
    public static void main(String[] args) throws IOException {
        // TODO: chamar C
        System.out.println(new String(new URL("https://www.pineman.eu").openConnection().getInputStream().readAllBytes()));
    }
}
