#include <iostream>

using namespace std;

class Foo {
public:
	explicit Foo(int arg = 42) : a(arg) { cout << "Foo: " << a << endl; };

private:
	int a;
};

class Parent {
public:
	explicit Parent(int arg = 0) : a(arg) { };

	void hello() { cout << "This is parent." << endl; };

	int a = 0;
};

class Child : public Parent {
public:
	explicit Child(int arg = 0) : Parent(arg), a(initFoo) { };

	void hello() { cout << "This is child." << endl; };

	int initFoo = 420;
	Foo a;
};

int main()
{
	Child c(3);

	c.hello();
}
