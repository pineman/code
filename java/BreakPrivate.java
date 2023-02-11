import java.lang.reflect.*;
import java.util.Arrays;

class A {
	private Integer a = 42;
	public Integer b() {
		return a;
	}
}

public class BreakPrivate {
	static Object p(Object o) {
		System.out.println(o[0]);
		return o;
	}
	public static void main(String[] args) throws IllegalAccessException {
		A a = new A();
		Field f = A.class.getDeclaredFields()[0];
		f.setAccessible(true);
		f.set(a, 69);
		p(a.b());
	}
}

