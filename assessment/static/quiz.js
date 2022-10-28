$(document).ready(function () {
    $("#assessmentform").submit(function (event) {
        event.preventDefault();
        $.ajax({
        data: $(this).serialize(),
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        success: function (json) {
            console.log(json);
            $("#past-result").hide();
            $("#result").html(json.result);
        },
        error: function (request, status, error) {
            console.log(request.responseText);
        }
        });
    });
})