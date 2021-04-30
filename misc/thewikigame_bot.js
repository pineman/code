// A http://thewikigame.com bot.
setInterval((function () {
	let s = document.querySelector("#start");
	let e = document.querySelector("#end");
	s = sb.textContent.replace(/ /g, "_");
	e = e.textContent.replace(/ /g, "_");
	sb.click();
	let i = document.querySelector("iframe");
	i.src = i.src.replace(s, e);
})(), 20000);
