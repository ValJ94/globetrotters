let csrfToken = document.cookie.split('=')[1];

function createThread() {
    $(document).ready(function() {
        $.ajax({
            type: "GET",
            url: "{% url 'globe_app: create_message_thread' user %}",
            headers: { 'X-CSRFToken': csrfToken },
            success: function (response) {
                console.log(response);
                receiver = User.objects.get(username=username);
                if(MessageThread.objects.filter(user=request.user, receiver=receiver).exists()) {
                    messageThread = MessageThread.objects.filter(user=request.user, receiver=receiver)[0];
                    return redirect('globe_app:thread', pk=messageThread.pk)
                } else if(MessageThread.objects.filter(user=receiver, receiver=request.user).exists()) {
                    messageThread = MessageThread.objects.filter(user=receiver, receiver=request.user)[0];
                    return redirect('globe_app:thread', pk=messageThread.pk)
                };

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