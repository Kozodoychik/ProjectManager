function page_back(e) {
	e.preventDefault();
	history.back();
}

document.querySelector(".btn-cancel")?.addEventListener("click", page_back);