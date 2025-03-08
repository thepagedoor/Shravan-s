function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.classList.toggle("active");
}

// Hide the menu after clicking a menu item on mobile
document.querySelectorAll('#menu a').forEach(item => {
    item.addEventListener('click', () => {
        const menu = document.getElementById("menu");
        if (menu.classList.contains("active")) {
            menu.classList.remove("active");
        }
    });
});

const images = document.querySelectorAll(".cover-image img");
let currentIndex = 0;

function switchImages() {
    // Hide current image
    images[currentIndex].style.opacity = "0";
    images[currentIndex].style.transform = "translateX(100%)";

    // Move to next image
    currentIndex = (currentIndex + 1) % images.length;

    // Show next image
    images[currentIndex].style.opacity = "1";
    images[currentIndex].style.transform = "translateX(0)";
}

// Run every 2.5 seconds
setInterval(switchImages, 2500);

let slideIndex = 0;
const totalSlides = 5; // Since we have 6 reviews (3 per slide)
const slider = document.querySelector(".testimonial-slider");
const dots = document.querySelectorAll(".dot");

function updateDots() {
    dots.forEach((dot, index) => {
        dot.classList.toggle("active", index === slideIndex);
    });
}

function moveSlide(direction) {
    slideIndex += direction;

    if (slideIndex < 0) {
        slideIndex = totalSlides - 1;
    } else if (slideIndex >= totalSlides) {
        slideIndex = 0;
    }

    slider.style.transform = `translateX(${-slideIndex * 100}%)`;
    updateDots();
}

function goToSlide(index) {
    slideIndex = index;
    slider.style.transform = `translateX(${-slideIndex * 100}%)`;
    updateDots();
}

// Auto-scroll every 4 seconds
setInterval(() => {
    moveSlide(1);
}, 4000);

function sendWhatsApp() {
    let name = document.getElementById("name").value;
    let gender = document.getElementById("gender");
    let service = document.getElementById("service").value;
    let appointmentDate = document.getElementById("appointmentDate").value;
    let appointmentTime = document.getElementById("appointmentTime").value;

    if (!name || !gender || !service || !appointmentDate || !appointmentTime) {
        alert("Please fill all the details!");
        return;
    }

    let genderValue = gender.value;
    let message = `Name: ${name}%0aGender: ${genderValue}%0aService: ${service}%0aAppointment Date: ${appointmentDate}%0aAppointment Time: ${appointmentTime}`;

    let phoneNumber = "+916302941811"; // Replace with your WhatsApp number
    let whatsappURL = `https://wa.me/${phoneNumber}?text=${message}`;

    window.open(whatsappURL, "_blank");
}