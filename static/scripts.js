document.getElementById("showButtonsBtn").addEventListener("click", function() {
    var additionalButtons = document.getElementById("additionalButtons");
    additionalButtons.classList.toggle("hidden");
  });
  
  function captureImage() {
    fetch('/capture')
        .then(response => {
            if (response.ok) {
                return response.text();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            alert(data); // Display the message in a popup
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function captureVideo() {
            fetch('/video_record')
                .then(response => {
                    if (response.ok) {
                        return response.text();
                    }
                    throw new Error('Network response was not ok.');
                })
                .then(data => {
                    alert(data); // Display the message in a popup
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
function stopVideo() {
            fetch('/stop_record')
                .then(response => {
                    if (response.ok) {
                        return response.text();
                    }
                    throw new Error('Network response was not ok.');
                })
                .then(data => {
                    alert(data); // Display the message in a popup
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }

