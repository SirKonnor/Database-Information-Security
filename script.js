function searchCars() {
    let carClass = document.getElementById('car-class').value;
    let carBrand = document.getElementById('car-brand').value;
    let carModel = document.getElementById('car-model').value;
}

function bookCar() {
    let bookingDate = new Date();
    let returnDate = new Date();
}

function redirectToAnotherPage() {
    window.location = "booking.html";
}

function redirectToAnotherPage2() {
    window.location = "booking.html";
}

function redirectToAnotherPage3() {
    window.location = "booking.html";
}

document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    var data = {};
    for (var [key, value] of formData.entries()) {
      data[key] = value;
    }
    console.log(data);
  });

  document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var phone = document.getElementById('phone').value;
    var password = document.getElementById('password').value;
    console.log("Phone: " + phone + ", Password: " + password);
  });
  


