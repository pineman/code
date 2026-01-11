function fib(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;
  return fib(n-1) + fib(n-2);
}

// what is printed?
console.log(fib(42));
setTimeout(() => console.log('timeout'), 1000);
new Promise((resolve) => { console.log(3); resolve(3) })
new Promise((resolve) => resolve(3)).then((x) => console.log(x));
console.log(fib(42));
// 267914296, 3, 267914296, 3, timeout
// Promises (and therefore async functions which are Promises too) are yielded to the 'microtask' queue, while the callback in setTimeout is queued to the 'callback' queue. the microtask queue has priority over the callback queue.

// the first 3 is printed synchronously because that code is equivalent to:
async function a() {
  console.log(3);
  return 3;
}
console.log(fib(42));
a(); // without await, since we didn't specify a .then()
new Promise((resolve) => resolve(3)).then((x) => console.log(x));
console.log(fib(42));

// which is equivalent to:
async function b() {
  return 3;
}
async function c() {
  const x = await b();
  console.log(x);
}
console.log(fib(42));
new Promise((resolve) => { console.log(3); resolve(3) })
c(); // without await because console.log(fib(42)) is not inside a .then! in other words, its sync code.
console.log(fib(42));

