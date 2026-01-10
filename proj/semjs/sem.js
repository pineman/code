class Sem {
  #q;

  constructor(num) {
    this.#q = Array(num);
    for (let i = 0; i < num; i++) {
      this.#q[i] = new Promise((resolve) => {
        return resolve(i);
      });
    }
  }

  async run(f) {
    await Promise.race(this.#q).then(async (i) => {
      this.#q[i] = new Promise(async (resolve, reject) => {
        await f();
        resolve(i);
      });
    });
  }
}

function sleep(s) {
  return new Promise((resolve) => setTimeout(resolve, s * 1000));
}
const start = performance.now();
const log = (i) => {
  const second = Math.round((performance.now() - start) / 1000);
  console.log(
    `${second}s - completed promise that sleeps for ${i + 1} seconds`,
  );
};

const func = (i) => {
  return async () => {
    await sleep(i + 1);
    log(i);
    return i;
  };
};

const s = new Sem(4);

for (let i = 0; i < 10; i++) {
  await s.run(func(i));
}
