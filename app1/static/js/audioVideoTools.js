function sendCustomerData() {
    // Collect all input field data
    let formData = {};

    // Select all input, textarea, and select elements
    const inputs = document.querySelectorAll('input[name], textarea[name], select[name]');

    // Iterate over inputs and add their values to formData
    inputs.forEach(input => {
        formData[input.name] = input.value;
    });
    let checkedOption = document.querySelector('input[name="gstoption"]:checked');

    if (!checkedOption) {
        alert("Please choose a GST option.");
    } else {
        formData['gstoption'] = checkedOption.value;
    }

    // Send the data using jQuery AJAX
    $.ajax({
        url: '/sentcustomerdata/', // Replace with your Django URL
        method: 'POST',
        data: JSON.stringify(formData), // Convert formData to a JSON string
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': getCSRFToken('csrf_token') // Include CSRF token for Django
        },
        success: function (response) {
            if (response.status === "success") {

                showOverlay('Data submitted successfully! ' + response.message);
                inputs.forEach(input => {
                    input.value = '';
                });
            }

            else if (response.status === "duplicate_entry") {
                UpdateMessage('' + response.message);
            }

            else if (response.status === "error") {
                showOverlay('yeh garbError hai baba' + response.message);
            }
        },
        error: function (xhr, status, error) {
            showOverlay('Koi Error hai: ' + errorMessage);
            console.error(xhr.responseText);
        }
    });
}