$(document).ready(function(){

    count = $('.multiField').length
    
    for (i = 0; i < count; i++) {
        if ($('#div_id_form-'+ i +'-image').find("a").length) {
            conversion_id = $('#conversion_id').val()
            image_index = $('#id_form-'+ i +'-id').val()
            str = "/conversions/delete_image/" + conversion_id + "/" + image_index + "/" 
            $('#div_id_form-'+ i +'-image').append('<a href="' + str + '" class="btn-light-green mt-3 text-white btn">DELETE</a><br><hr class="border-top-dark">')
        }
    }
});