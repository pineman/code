#include <iostream>
#include <stdexcept>

// C++11 constexpr functions use recursion rather than iteration
// (C++14 constexpr functions may use local variables and loops)
constexpr int factorial(int n)
{
	return n <= 1 ? 1 : (n * factorial(n - 1));
}

// C++11 constexpr functions had to put everything in a single return statement
// (C++14 doesn't have that requirement)
constexpr std::size_t countlower(std::string_view s)
{
	return s.size();
}

int main()
{
	int k = 8; // disallow optimization using volatile
	std::cout << k << "! = " << factorial(k) << '\n'; // computed at run time

	std::cout << "Hello, world! is " << countlower("Hello, world!") << std::endl; // implicitly converted to conststr
}