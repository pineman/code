#include <iostream>
#include <typeinfo>

using namespace std;

auto test(auto x, auto y)
{
	cout << typeid(x).name() << endl;
	cout << typeid(y).name() << endl;
	cout << typeid(x + y).name() << endl;
	return x + y;
}

int main(int argc, char *argv[])
{
	int a = 2;
	auto b = 3;
	cout << test(a, b) << endl;

	auto c = 4.5;
	cout << test(a, c) << endl;

	auto d = "string!";
	cout << test(a, d) << endl;
}
