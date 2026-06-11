let createBtn = document.getElementById("btn-create");
let editBtn = document.getElementById("btn-edit");
let deleteBtn = document.getElementById("btn-delete");
let selectAllCheckbox = document.getElementById("select-all-checkbox");

let fieldsCount = document.getElementsByClassName("field-checkbox").length;

let selectedFields = [];


function updateButtons() {
	if (selectedFields.length > 0) {
		deleteBtn.classList.remove("disabled");
		editBtn.classList.add("disabled");
	}
	else {
		deleteBtn.classList.add("disabled");
		editBtn.classList.add("disabled");
	}

	if (selectedFields.length == 1)
		editBtn.classList.remove("disabled");
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
		if (e.target.checked)
			selectedFields.push(parseInt(e.target.dataset.id));
	});

	if (!e.target.checked)
		selectedFields = [];

	updateButtons();
}

document.querySelectorAll(".field-checkbox").forEach(checkbox => {
	checkbox.addEventListener("change", onCheckboxChange)
});

selectAllCheckbox.addEventListener("change", selectAll);