$(document).ready(function () {
    // Jquery datepicker
    $('#inlineFormInputGroupCheckOut, #inlineFormInputGroupCheckIn').datepicker({
        format: 'dd/mm/yyyy'
    });

    // Change form with radio buttons
    document.getElementById('residential-radio').addEventListener('click', function () {
        document.getElementById('radio-forms').innerHTML = `<h1>Residential form</h1>`;
    });

     // Change form with radio buttons
    document.getElementById("commercial-radio").addEventListener('click', function () {
        document.getElementById('radio-forms').innerHTML = `<h1>Comercial form</h1>`;
    });
});

