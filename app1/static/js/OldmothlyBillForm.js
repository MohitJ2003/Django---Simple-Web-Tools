
function formatDate(input) {
    var date = new Date(input.value);
    if (!isNaN(date.getTime())) {
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();

        if (day < 10) {
            day = '0' + day;
        }
        if (month < 10) {
            month = '0' + month;
        }

        input.value = day + '-' + month + '-' + year;
    }
}




// Get form and input elementss
const myForm = document.getElementById('createfileform');
const price_var = document.getElementById('billprice2');
const custname_var = document.getElementById('customname');
const createfilebtnvar = document.getElementById('createfilebtn');
const errorMessage = document.getElementById('errorMessage');

const year = document.getElementById('year');
const billmonth = document.getElementById('month');

var file = document.getElementById('file');
var commnm = document.getElementById('commnm');
var comdprice = document.getElementById('comdprice');
var dateofpymnt = document.getElementById('dateofpymnt');

var plcoftranopt = document.getElementById('plcoftranopt');
var category = document.getElementById('category');
var message_2 = document.getElementById('message_2');
var tabledata = document.getElementById('tabledata');


// Function to check form validity
function checkFormValidity() {
    if (price_var.value && custname_var.value) {
        // Both fields are filled
        createfilebtnvar.disabled = true;
        createfilebtnvar.style.backgroundColor = "rgb(212, 190, 174)";
        errorMessage.textContent = 'Both fields cannot be filled';
    } else if (!price_var.value && !custname_var.value) {
        // Neither field is filled
        createfilebtnvar.disabled = true;
        createfilebtnvar.style.backgroundColor = "rgb(212, 190, 174)";
        errorMessage.textContent = 'One of the fields needs to be filled';
    } else {
        // Form is valid
        createfilebtnvar.style.backgroundColor = "rgb(84, 60, 0)";
        createfilebtnvar.disabled = false;
        errorMessage.textContent = '';
    }
}

// Add event listeners to input fields
price_var.addEventListener('input', checkFormValidity);
custname_var.addEventListener('input', checkFormValidity);


// Prevent form submission if the button is disabled
document.getElementById('createfilebtn').addEventListener('click', function (event) {
    if (createfilebtnvar.disabled) {
        event.preventDefault();
    }
});
/*
$('.btn34').click(function () {
    alert("My Message");
})
*/


$(document).ready(function () {
    $('#createfilebtn').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: 'GET',
            url: '{% url "my_function" %}',
            data: {
                'totbillprice2': price_var.value,
                'custname_var': custname_var.value,
                'year2': year.value,
                'billmonth2': billmonth.value,
            },
            success: function (response) {
                $('#message').text(response.result);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });


    $('#addrecord').click(function (e) {
        e.preventDefault();
        $.post({
            type: 'GET',
            url: '{% url "get_commodity_details" %}',
            data: {
                'file': file.value,
                'commnm': commnm.value,
                'comdprice': comdprice.value,
                'dateofpymnt': dateofpymnt.value,
                'plcoftranopt': plcoftranopt.value,
                'category': category.value,
            },
            success: function (response) {
                message_2.textContent = response.result_1;

                commnm.value = "";
                comdprice.value = "";
                dateofpymnt.value = "";
                plcoftranopt.value = "";
                category.value = "";


                var data = response.filedata2;

                var tableBody = $('#excelDataTable tbody');
                tableBody.empty();
                var row = $('<tr>'); // for adding table heading's tr
                row.append($('<th>').text('S no.'));
                for (var j = 0; j < data[0].length; j++) {
                    if (j == 5) { row.append($('<th class = "hidden-column">')); }
                    else { row.append($('<th>').text(data[0][j])); }
                }
                row.append($('<th>').text('Actions'));
                tableBody.append(row);

                var sum_of_price = 0;
                for (var i = 1; i < data.length; i++) {
                    var row = $('<tr class = "trtbl2" id="row' + i + '">');
                    row.append($('<td>').text(i));
                    // alert(data[i][1]);
                    sum_of_price += Number(data[i][1]);
                    for (var j = 0; j < data[i].length; j++) {
                        if (j == 2) { row.append($('<td class = "date-cell">').text(data[i][j])) }
                        else if (j == 5) { row.append($('<td class = "hidden-column">').text(data[i][j])) }

                        else { row.append($('<td>').text(data[i][j])); }
                    }
                    row.append($('<td>'
                        + '<button onclick="editRow(this)" class="edit-btn" ><img class = "editbutton" src = "{% static "\images\editbtnlogo.png" %}" ></button>'
                        + '<button class="save-btn hidden"><img src = "{% static "\images\savelogobtn.png" %}" ></button>'
                        + '<button class = "cancel-btn hidden"><img src = "{% static "\images\Button_cancel.png" %}" ></button>'
                        + '<button class = "delete-btn"><img src = "{% static "\images\Delete-button.png" %}" ></button>'
                    ))

                    tableBody.append(row);
                }

                var row = $('<tr>'); // for adding total values tr row
                for (var j = 0; j < data[0].length; j++) {
                    if (j == 1) { row.append($('<th>').text('Total')); }
                    if (j == 1) { row.append($('<td>').text(sum_of_price)); }
                    if (j == 5) { row.append($('<td class = "hidden-column">').text('')); }
                    else (row.append($('<td>').text('')));
                }
                // row.append($('<td>').text(''));
                tableBody.append(row);


                const tableRows2 = document.querySelectorAll("#excelDataTable .trtbl2");
                // alert("341")
                tableRows2.forEach(row => {
                    // alert("342");
                    const editBtn = row.querySelector(".edit-btn");
                    const saveBtn = row.querySelector(".save-btn");
                    const cancelBtn = row.querySelector(".cancel-btn");
                    const deleteBtn = row.querySelector(".delete-btn");

                    editBtn.addEventListener("click", () => {
                        editBtn.classList.add("hidden");
                        deleteBtn.classList.add("hidden");

                        saveBtn.classList.remove("hidden");
                        cancelBtn.classList.remove("hidden");
                    });

                    cancelBtn.addEventListener("click", () => {
                        saveBtn.classList.add("hidden");
                        cancelBtn.classList.add("hidden");
                        editBtn.classList.remove("hidden");
                        deleteBtn.classList.remove("hidden");
                    });

                    saveBtn.addEventListener("click", () => {
                        saveBtn.classList.add("hidden");
                        cancelBtn.classList.add("hidden");
                        editBtn.classList.remove("hidden");
                        deleteBtn.classList.remove("hidden");
                    });

                });


                $('.delete-btn').click(function () {
                    confirmationModal.style.display = 'block';
                    confirmDelete(this);
                });

                function confirmDelete(button) {

                    var row = button.parentElement.parentElement;
                    confirmationModal.setAttribute('data-row', row.id);
                    var choice = document.getElementById("choice").innerText;
                    var hiddenData = button.parentElement.parentElement.querySelector(".hidden-column").innerText;
                    var hidden_btn = button.parentElement.parentElement.querySelector(".delete-btn");



                    if (confirm("Do you really want to Delete")) {
                        alert("You pressed OK! Continuing execution...");
                    } else {
                        alert("You pressed Cancel! Stopping execution.");
                    }
                    alert("Record Deleted Succesfully !! ");

                    $.ajax({
                        type: 'GET',
                        url: 'delete_record',
                        data: {
                            "hiddenData": hiddenData,
                            "filename": file.value,
                            'csrfmiddlewaretoken': '{{ csrf_token }}'
                        },
                        success: function (response) {
                            alert(response.result3);
                        },
                        error: function (xhr, status, error) {
                            alert('Error sending data!');
                        }
                    });


                }

                $('.save-btn').click(function () {
                    save_edited_record(this);
                });

                function save_edited_record(btn) {
                    var row = btn.parentNode.parentNode;
                    var rowData = [];
                    var values = "";
                    index = 0;
                    var inputs = row.querySelectorAll('input');

                    inputs.forEach(function (input) {
                        var value = input.value;
                        rowData[index] = value;
                        values += value + ",";
                        index += 1;
                    });

                    var uniqueID = btn.parentElement.parentElement.querySelector(".hidden-column").innerText;
                    $.ajax({
                        type: 'GET',
                        url: 'save_edited_record',
                        data: {
                            "uniqueId": uniqueID,
                            "filenamefor_ser": file.value,
                            "editedvalues": values,
                            'csrfmiddlewaretoken': '{{ csrf_token }}'
                        },
                        success: function (response) {
                            alert(response.result4);
                        },
                        error: function (xhr, status, error,) {
                            alert('Error sending data!');
                        }
                    });
                }
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });

    $('#searchInput').on('input', function () {
        var search_text = $(this).val();
        $.ajax({
            type: 'GET',
            url: '{% url "search_files" %}',
            data: { 'search_text': search_text },
            success: function (response) {
                $('#file').empty();
                response.files.forEach(function (file) {
                    $('#file').append('<option>' + file + '</option>');
                });
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
                $('#file').append('<li>Error occurred, please try again.</li>');
            }
        });
    });

});

$(document).ready(function () {
    $(".datepickerBtn").click(function () {
        $(this).prev('.datepicker').datepicker("show"); // Show the datepicker associated with the input before this button
    });

    $(".datepicker").datepicker({ dateFormat: 'dd-mm-yy' }); // Initialize the datepicker with the desired date format
});

$(document).ready(function () {
    $.datepicker.setDefaults({
        dateFormat: 'dd-mm-yy'
    });
});

function editRow(btn) {

    var min_width = 15;
    var row = btn.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");
    var arr = [];


    for (var i = 1; i < cells.length - 2; i++) {
        var input = document.createElement("input");
        input.type = "text";
        input.value = cells[i].innerText;
        input.style.width = cells[i].offsetWidth - min_width + "px";
        input.style.padding = "5px 5px 5px 5px";
        arr[i] = input.value; // for cancel values change to orginals

        cells[i].innerText = '';
        cells[i].appendChild(input);
        min_width += 7;
    }


    /*
    // commodity name
    var input_2 = document.createElement("input");
    input_2.type = "text";
    input_2.value = cells[1].innerText;
    arr[1] = input_2.value;
    cells[1].innerText = '';
    cells[1].appendChild(input_2);
    input_2.style.width = cells[1].offsetWidth - cut7 + "px";

    // price input
    var input = document.createElement("input");
    input.type = "text";
    input.value = cells[2].innerText;
    arr[2] = input.value;
    cells[2].innerText = '';
    cells[2].appendChild(input);

    // date input 
    const dateCell = row.querySelector('.date-cell');
    const originalDate = dateCell.innerText;
    const input2 = document.createElement('input');
    input2.type = 'text';
    input2.value = originalDate;
    input2.style.width = '100px';
    $(input2).datepicker();
    dateCell.style.width = dateCell.offsetWidth - cut7 + "px";
    const setDateButton = document.createElement('button');
    setDateButton.innerText = 'Set Date';
    setDateButton.type = 'button';
    setDateButton.onclick = () => $(input2).datepicker('show');
    dateCell.setAttribute('data-original-date', originalDate);
    dateCell.innerHTML = '';
    dateCell.appendChild(input2);
    dateCell.appendChild(setDateButton);

    // Place input
    var place_input = document.createElement("input");
    place_input.type = "text";
    place_input.value = cells[3].innerText;
    arr[3] = place_input.value;
    cells[4].innerText = '';
    cells[4].appendChild(place_input);
    

    // Category input
    var select = document.createElement("select");
    var option = document.createElement("option");
    option.text = cells[5].innerText;
    select.appendChild(option);
    var option1 = document.createElement("option");
    option1.text = "Devlopment";
    select.appendChild(option1);
    var option2 = document.createElement("option");
    option2.text = "HR";
    select.appendChild(option2);
    var option3 = document.createElement("option");
    option3.text = "Testing";
    select.appendChild(option3);
    var currentValue = cells[4].innerText;
    arr[4] = cells[5].innerText;
    cells[5].innerText = '';
    cells[5].appendChild(select);
    */

    const saveBtn = row.querySelector(".save-btn");
    saveBtn.onclick = function () { saveRow(this); };
    // btn.parentNode.replaceChild(saveBtn, btn);

    const cnclbtn = row.querySelector(".cancel-btn");
    cnclbtn.onclick = function () { cancelbtn(this, arr); };
    currentRow = row;
}


function saveRow(btn) {
    var row = btn.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");


    for (var i = 1; i < cells.length - 2; i++) {
        cells[i].innerText = cells[i].getElementsByTagName("input")[0].value;
    }
    /*
    cells[5].innerText = cells[1].getElementsByTagName("select")[0].value;

    const dateCell = row.querySelector('.date-cell');
    const input = dateCell.querySelector('input[type="text"]');
    const newDate = input.value;

    // Set the new date in dd-mm-yyyy format
    dateCell.innerHTML = newDate;
    */

    currentRow = null;

}

function cancelbtn(btn, arr) {
    var row = btn.parentNode.parentNode;
    var cells = row.getElementsByTagName("td");

    var datebutton = row.querySelectorAll(".date-container");

    for (var i = 1; i < cells.length - 2; i++) {
        cells[i].innerText = cells[i].getElementsByTagName("input")[0].value;
        cells[i].innerText = arr[i];
    }



    entRow = null;
}

function hide_deletedrow(button) {
    var row = button.parentNode.parentNode;
    row.style.display = 'none';
}


// Get the modal elements
var confirmationModal = document.getElementById('confirmationModal');
var successModal = document.getElementById('successModal');


// Open confirmation modal

// Close modal
function closeModal() {
    document.getElementById("choice").innerText = "Yes";
    confirmationModal.style.display = 'none';
    successModal.style.display = 'none';
}

function deleteRow() {
    document.getElementById("choice").innerText = "No";
    var rowId = confirmationModal.getAttribute('data-row');
    var row = document.getElementById(rowId);
    deleteRow
    row.remove();
    closeModal();
    successModal.style.display = 'block';

    confirmDelete(this);
}

// Close modals when clicking on close buttons
var closeButtons = document.getElementsByClassName('close');
for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].onclick = function () {
        closeModal();
    }
}


