navigator.usb.requestDevice({ filters: [] })
	.then(d => {
		for (let c of d.configurations) {
			for (let k of c.interfaces) {
				for (let x of k.alternates) {
					console.log(`found interfaceClass = ${x.interfaceClass}`)
				}
			}
		}
	})
