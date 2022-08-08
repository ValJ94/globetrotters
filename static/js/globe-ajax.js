let csrfToken = document.cookie.split('=')[1];

function createThread() {
    $(document).ready(function() {
        $('#save_history')({
            type: "POST",
            url: "{% url 'globe_app:save_history' %}",
            headers: { 'X-CSRFToken': csrfToken },
            data: {
                'latitude': latitude,
                'longitude': longitude,
                'locationFullName': locationFullName,
                'owner': owner,
                'travelPics': travelPics,
                'travelNotes': travelNotes,
                'noteContent': content,

            },
            // success and error are callbacks. They notify when the request is done.
            success: function (response) {
                console.log(response);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log('failed');
                console.log(jqXHR);
                console.log(textStatus);
                console.log(errorThrown);
            }
        });
    })

}