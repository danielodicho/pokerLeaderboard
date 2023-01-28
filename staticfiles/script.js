const removeButtons = document.querySelectorAll('.remove-button');
  removeButtons.forEach(button => {
    button.addEventListener('click', event => {
      const playerId = event.target.getAttribute('data-id');
      fetch(`/leaderboard/api/players/${playerId}/`, {
        method: 'DELETE',
       headers: {
        'Content-Type': 'application/json',
      },
      }).then(() => {
      showAlert("Player removed successfully!");

      });
    });
  });

  function showAlert(message) {
    // Get the alert container element

    const alertContainer = document.getElementById("alert");

    // Create a new element for the alert message
    const alertMessage = document.createElement("div");
    alertMessage.classList.add("notification", "is-success");
    alertMessage.innerHTML = message;

    // Add the alert message to the container
    alertContainer.appendChild(alertMessage);

    // disappear the message

    setTimeout(() => {
    window.location.reload();
    alertMessage.remove();
    }, 1000);

  }
  const addForm = document.getElementById('add-form');
  addForm.addEventListener('submit', event => {
    event.preventDefault();
    const nameInput = document.getElementById('name-input');
    const name = nameInput.value;
    fetch('/leaderboard/api/players/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: name,
        current_amount: 0,
        peak_amount: 0,
      }),
    }).then(() => {
      window.location.reload();
    });
  });