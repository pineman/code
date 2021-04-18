class wrap {
public static void main(String[] args) {

class Parent {
	private int a = 50;
	public Parent(int a) {
		System.out.println("Parent's constructor");
		System.out.println(this.a);
	}
}

class Child extends Parent {
	public int a = 40;
	public Child(int a) {
		super(a);
		System.out.println("Child's constructor");
		System.out.println(a);
	}
}

Child c = new Child(30);
System.out.println(c.a);

}
}
