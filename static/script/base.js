    /* This validates the add_post form */
    const post_form = document.getElementById('add_post_form')
    const messageBlock = document.getElementById('form_validation_message');

    function errorMessage(message) {
        e.preventDefault();
        const messageText = document.createTextNode(message);
        messageBlock.appendChild(messageText);
    }

    post_form.addEventListener('submit', (e) => {
        if (document.getElementById("featured_image").value === '') {
            e.preventDefault();
            alert('Please provide an image.');
            errorMessage('Please provide an image.');
        }

    });