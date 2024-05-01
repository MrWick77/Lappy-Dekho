document.getElementById('price-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var form = new FormData(this);

    fetch('/predict', {
        method: 'POST',
        body: form
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Predicted Price: ₹' + data.predicted_price.toFixed(2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
