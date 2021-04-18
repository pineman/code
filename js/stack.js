// https://www.youtube.com/watch?v=eEBOvqMfPoI

// Passing blocks around!

const newStack = () => {
	const items = []
	return {
		depth: () => items.length,
		top: () => items[0],
		pop: () => { items.shift() },
		push: newTop => { items.unshift(newTop) },
	}
}

const stackable = base => {
	const items = []
	return Object.assign(base, {
		depth: () => items.length,
		top: () => items[0],
		pop: () => { items.shift() },
		push: newTop => { items.unshift(newTop) },
	})
}

const clearable = base => {
	return Object.assign(base, {
		clear: () => {
			while (base.depth())
				base.pop()
		},
	})
}

const newStack =
	() => clearable(stackable({}))

const newStack =
	() => compose(clearable, stackable)({})

const compose = (...funcs) =>
	arg => funcs.reduceRight(
		(composed, func) => func(composed), arg)
