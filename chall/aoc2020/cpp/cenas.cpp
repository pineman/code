#include "cenas.h"

#include "doctest.h"

std::string cenas::getCenas() {
    return "cenas";
}

TEST_CASE("Cenas") {
    CHECK(cenas::getCenas() == "not cenas");
}