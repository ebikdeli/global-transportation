 // JavaScript form validation and AJAX submission
document.querySelector('.shipping-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the default form submission behavior

    // Validate form
    let valid = true;

    if (!document.getElementById('product').value) {
        document.getElementById('productError').textContent = 'Please enter a product name.';
        valid = false;
    } else {
        document.getElementById('productError').textContent = '';
    }

    if (!document.getElementById('weight').value) {
        document.getElementById('weightError').textContent = 'Please enter a weight.';
        valid = false;
    } else {
        document.getElementById('weightError').textContent = '';
    }

    if (!document.getElementById('quantity').value) {
        document.getElementById('quantityError').textContent = 'Please enter a quantity.';
        valid = false;
    } else {
        document.getElementById('quantityError').textContent = '';
    }

    if (!document.getElementById('source').value) {
        document.getElementById('sourceError').textContent = 'Please enter a source.';
        valid = false;
    } else {
        document.getElementById('sourceError').textContent = '';
    }

    if (!document.getElementById('destination').value) {
        document.getElementById('destinationError').textContent = 'Please enter a destination.';
        valid = false;
    } else {
        document.getElementById('destinationError').textContent = '';
    }

    // if (!valid) {
    //     return; // Stop if validation fails
    // }
    if (valid){
        // Create form data object to send with
        let jsonData = new FormData();
        let data = {
            company: document.getElementById('company').value,
            product: document.getElementById('product').value,
            weight: document.getElementById('weight').value,
            quantity: document.getElementById('quantity').value,
            source: document.getElementById('source').value,
            destination: document.getElementById('destination').value,
            describe: document.getElementById('describe').value
        };
        jsonData.append('data', JSON.stringify(data))
        
        // Send data via AJAX
        let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let url = `${location.protocol}//${location.host}/shipping/order/`;
        fetch(url, { // Replace with your server URL
            method: 'POST',
            headers: {
                // 'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: jsonData,
            credentials: 'include',
            mode: 'cors',
        })
        .then(response => response.json())
        .then(data => {
            if (data) {
                // Show success message
                // document.getElementById('successMessage').textContent = 'Form submitted successfully!';
                // console.log(data);
                let shipping_code = data['data']['shipping_code'];
                window.location.replace(`${location.protocol}//${location.host}/shipping/view/${shipping_code}/`)
            } else {
                // document.getElementById('successMessage').textContent = 'Error submitting form.';
                alert('Error submitting form.');
            }
        })
        .catch(error => {
            // document.getElementById('successMessage').textContent = 'Error submitting form.';
            alert('Error submitting form.')
            console.log('Error:', error);
        });
    }
});