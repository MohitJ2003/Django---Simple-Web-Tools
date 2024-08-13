function filterLinks() {
        // Get input value and convert it to lowercase for case-insensitive search
        var searchText = document.getElementById('searchInput').value.toLowerCase();

        // Get the list of links
        var links = document.getElementById('linkList').getElementsByTagName('a');

        // Loop through the links and show/hide based on the search
        for (var i = 0; i < links.length; i++) {
                var linkText = links[i].innerText.toLowerCase();
                var listItem = links[i].parentNode; // Get the parent li element

                if (linkText.includes(searchText)) {
                        listItem.style.display = 'list-item'; // Show the list item
                } else {
                        listItem.style.display = 'none'; // Hide the list item
                }
        }
}
/*
    function toggleDiv() {
    var div = document.getElementById('charactersblock_id');
    var button = document.getElementById('characters_btnid');

    if (div.style.display === 'none') {
      // If the div is currently hidden, show it
      div.style.display = 'block';
      button.innerText = 'Hide Characters';
    } else {
      // If the div is currently visible, hide it
      div.style.display = 'none';
      button.innerText = 'Show Characters';
    }
  }
  */

// Function to open file explorer
function openFileExplorer_tochoosenew_chrimg(imgid_2) {
        document.getElementById(imgid_2).click();
}

// Function to preview image and remember choice
function chrimgprvw(input, imgid) {
        var mainImage = document.getElementById(imgid);
        var file = input.files[0];

        if (file) {
                var reader = new FileReader();

                reader.onload = function (e) {
                        // Update the source of the main image
                        mainImage.src = e.target.result;
                        mainImage.alt = "New Image";

                        // Save the selected image URL to local storage
                        localStorage.setItem('selectedImage', e.target.result);
                };

                reader.readAsDataURL(file);
        }
}

// Function to retrieve the selected image URL on page load
window.onload = function () {
        var selectedImage = localStorage.getItem('selectedImage');
        if (selectedImage) {
                // Update the source of the main image
                document.getElementById('imageInput1').src = selectedImage;
        }
};

//Now  [27/Dec/2023 10:46:55]
function toggleDiv() {
        var myDiv = document.getElementById('charactersblock_id');
        var button = document.getElementById('characters_btnid');

        // Toggle the hidden class on the div
        myDiv.classList.toggle('hidden');

        // Toggle the button text
        button.textContent = myDiv.classList.contains('hidden') ? 'Hide Characters' : 'Show Characters';
}

function openPasswordOverlay() {
        // Display the password overlay
        document.getElementById('passwordOverlay').style.display = 'flex';
}

function checkPassword() {
        // Get the entered password
        var enteredPassword = document.getElementById('password').value;

        // Replace the following line with your actual password validation logic
        var correctPassword = "passme45";

        // Check if the entered password is correct
        if (enteredPassword === correctPassword) {
                // Hide the password overlay
                document.getElementById('passwordOverlay').style.display = 'none';
                document.getElementById('myDiv').style.display = 'block';
                document.getElementById('closebtn').style.display = 'block';

                // Add code to show the protected content or perform other actions
        } else {
                // Display an error message or take appropriate action
                alert("Incorrect password. Please try again.");
        }
}

function closediv() {
        document.getElementById('closebtn').style.display = 'none';
        document.getElementById('myDiv').style.display = 'none';
}


