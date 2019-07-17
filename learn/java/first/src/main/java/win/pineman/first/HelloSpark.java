package win.pineman.first;

import static spark.Spark.*;

public class HelloSpark {
	public static void main(String[] args) {
        get("/", (req, res) -> "Hello!");
	}
}
