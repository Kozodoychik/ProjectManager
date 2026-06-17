function workspaceRedirect(e) {
	window.location = e.target.parentNode.dataset.slug;
}

document.querySelectorAll(".workspace-card-header").forEach((card) => {
	card.addEventListener("click", workspaceRedirect);
});