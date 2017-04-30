#include <iostream>
#include <memory>

struct Node {
	int element;
	std::weak_ptr<Node> link;
};

int main()
{
	auto n1 = std::make_shared<Node>();
	auto n2 = std::make_shared<Node>();

	n1->link = n2;
	n2->link = n1;
}
