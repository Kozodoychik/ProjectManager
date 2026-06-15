function workspaceRedirect(e) {
	window.location = e.target.dataset.slug;
}

document.querySelectorAll(".workspace-card-header").forEach((card) => {
	card.addEventListener("click", workspaceRedirect);
});