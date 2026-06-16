let createBtn = document.getElementById("btn-create");
let deleteBtn = document.getElementById("btn-delete");
let editBtn = document.getElementById("btn-edit");

let toolbarBtns = document.querySelectorAll(".toolbar-btn");
let oneFieldActivatedBtns = document.querySelectorAll(".toolbar-btn-one");

let selectAllCheckbox = document.getElementById("select-all-checkbox");

let fieldsCount = document.getElementsByClassName("field-checkbox").length;

let csrfToken = document.querySelector("meta[name='csrf-token']").content;

let selectedFields = [];


function updateButtons() {
	if (selectedFields.length > 0) {
		toolbarBtns.forEach((btn) => {
			btn.classList.remove("disabled");
		});
		oneFieldActivatedBtns.forEach((btn) => {
			btn.classList.add("disabled");
		});
	}
	else {
		toolbarBtns.forEach((btn) => {
			btn.classList.add("disabled");
		});
	}

	if (selectedFields.length == 1)
		oneFieldActivatedBtns.forEach((btn) => {
			btn.classList.remove("disabled");
		});
}

function onCheckboxChange(e) {
	let id = parseInt(e.target.dataset.id);

	if (e.target.checked)
		selectedFields.push(id)
	else
		selectedFields = selectedFields.filter(i => i !== id);

	if (selectedFields.length == fieldsCount) {
		selectAllCheckbox.checked = true;
		selectAllCheckbox.indeterminate = false;
	}
	else if (selectedFields.length > 0) {
		selectAllCheckbox.checked = false;
		selectAllCheckbox.indeterminate = true;
	}
	else {
		selectAllCheckbox.checked = false;
		selectAllCheckbox.indeterminate = false;
	}

	updateButtons();
}

function selectAll(e) {
	document.querySelectorAll(".field-checkbox").forEach(checkbox => {
		checkbox.checked = e.target.checked;
		if (e.target.checked) {
			selectedFields.push(parseInt(checkbox.dataset.id));
		}
	});

	if (!e.target.checked)
		selectedFields = [];

	updateButtons();
}

document.querySelectorAll(".field-checkbox").forEach(checkbox => {
	checkbox.addEventListener("change", onCheckboxChange)
});

deleteBtn.addEventListener("click", (e) => {
	if (selectedFields.length > 1) {
		let f = document.createElement("form");
		f.action = "bulk-delete/";
		f.method = "POST";

		let i = document.createElement("input");
		i.type = "hidden";
		i.name = "ids";
		i.value = JSON.stringify(selectedFields);

		let csrf = document.createElement("input");
		csrf.type = "hidden";
		csrf.name = "csrfmiddlewaretoken";
		csrf.value = csrfToken;

		f.appendChild(csrf);
		f.appendChild(i);

		document.body.appendChild(f);
		f.submit();
	}
	else if (selectedFields.length == 1) {
		window.location = `${selectedFields[0]}/delete`;
	}
});

editBtn.addEventListener("click", (e) => {
	if (selectedFields.length != 1) return;

	window.location = `${selectedFields[0]}/edit`;
});

selectAllCheckbox.addEventListener("change", selectAll);