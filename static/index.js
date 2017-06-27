$(function(){
    $("#submit").on('click', function(){
        url = '/upload';
        var file = $('[type="file"]')[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        $.ajax({
            url: "/upload",
            type: 'POST',
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                $('#result').attr("src", data.src);
                $('#message').html(data.status);
            }
        });
        return false;
    });
});