$(document).ready(function () {
    // Jquery datepicker
    $('#inlineFormInputGroupCheckOut, #inlineFormInputGroupCheckIn').datepicker({
        format: 'dd/mm/yyyy'
    });

    // Change form with radio buttons
    document.getElementById('residential-radio').addEventListener('click', function () {
        document.getElementById('radio-form-residential').classList.remove('display-none');
        document.getElementById('radio-form-commercial').classList.add('display-none');
    });

    // Change form with radio buttons
    document.getElementById("commercial-radio").addEventListener('click', function () {
        document.getElementById('radio-form-residential').classList.add('display-none');
        document.getElementById('radio-form-commercial').classList.remove('display-none');
    });
});
