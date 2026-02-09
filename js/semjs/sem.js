class Sem {
  #q;
  #acquiring;

  constructor(num) {
    this.#q = Array.from({ length: num }, () => Promise.resolve());
    this.#acquiring = Promise.resolve();
  }

  run(fn) {
    // Deferred to signal when slot is released
    let releaseSlot;
    const slotOccupied = new Promise((r) => (releaseSlot = r));

    // Race for a free slot
    const slotAcquired = this.#acquiring.then(() =>
      Promise.race(this.#q.map((p, i) => p.then(() => i)))
    );

    // Mark the slot as occupied BEFORE next run can race
    const slotUpdated = slotAcquired.then((slot) => {
      this.#q[slot] = slotOccupied;
      return slot;
    });

    // Next run waits until we've marked our slot
    this.#acquiring = slotUpdated;

    // Do the work and release slot when done
    const result = slotUpdated.then(async () => {
      try {
        return await fn();
      } finally {
        releaseSlot();
      }
    });

    return result;
  }
}

function sleep(s) {
  return new Promise((resolve) => setTimeout(resolve, s * 1000));
}
const start = performance.now();
const log = (i) => {
  const second = Math.round((performance.now() - start) / 1000);
  console.log(
    `${second}s - completed promise that sleeps for ${i + 1} seconds`
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

// Kick off all 10 tasks - semaphore limits to 4 concurrent
const promises = Array.from({ length: 10 }, (_, i) => s.run(func(i)));

const results = await Promise.all(promises);
results.forEach((ret, i) => {
  console.log(`${i} returns ${ret}`);
});
