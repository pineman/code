/*
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 0.5 seconds (c)

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

true if a and b are similar, false otherwise.
 */

// Definition for arrays:
// typedef struct arr_##name {
//   int size;
//   type *arr;
// } arr_##name;
//
// arr_##name alloc_arr_##name(int len) {
//   arr_##name a = {len, len > 0 ? malloc(sizeof(type) * len) : NULL};
//   return a;
// }

bool areSimilar(arr_integer a, arr_integer b)
{
    int c=0, l=0, r=0;
    for (int i = 0; i < a.size; i++) {
        if (a.arr[i] != b.arr[i]) {
            if (c == 2) return false; // Found a third different element => not similar
            c++;
            if (c == 1) l = i; // Save location of first different
            if (c == 2) r = i; // Save location of second different
        }
    }
    if (c == 0) return true; // Same array => similar
    if (c == 1) return false; // One different element => not similar

    // Two different elements and they're equal => similar
    if (a.arr[l] == b.arr[r] && a.arr[r] == b.arr[l]) return true;

    return false;
}

