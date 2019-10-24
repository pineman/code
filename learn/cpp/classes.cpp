#include <iostream>

using namespace std;

class Foo {
public:
	explicit Foo(int arg = 42)
		: a(arg)
	{
		cout << "Foo's constructor, a = " << a << endl;
	};

private:
	int a;
};

class Parent {
public:
	explicit Parent(int arg = 0)
		: a(arg)
	{
		cout << "Parent's constructor" << endl;
	}

	//void hello() { cout << "This is parent." << endl; };
	virtual void hello() { cout << "This is parent." << endl; };

	int a = 0;
};

class Child : public Parent {
public:
	explicit Child(int arg = 0)
		//: Parent(arg)
		: a(initFoo)
	{
		cout << "Child's constructor" << endl;
	};

	void hello() { cout << "This is child." << endl; };
	//virtual hello() { cout << "This is parent." << endl; };

	const int initFoo = 420;
	Foo a;
};

int main()
{
	Parent *p;
	Child c(3);
	p = &c;

	c.hello();
	p->hello();
}
