

$(document).ready(function () {

    $('#searchInput').on('input', function () {
        var search_text = $(this).val();
        $.ajax({
            type: 'GET',
            url: 'search_files',
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

