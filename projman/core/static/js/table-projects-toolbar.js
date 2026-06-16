let resourcesBtn = document.getElementById("btn-resources");

resourcesBtn.addEventListener("click", (e) => {
	if (selectedFields.length != 1) return;

	window.location = `${selectedFields[0]}/resources`;
});