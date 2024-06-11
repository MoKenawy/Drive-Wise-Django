document.addEventListener('DOMContentLoaded', function() {
    const ratingStars = document.querySelectorAll('#rating-stars');
    ratingStars.forEach(star => {
        // const rating = parseFloat(star.getAttribute('data-rating')); // Get rating value as float
        const rating = parseFloat(star.getAttribute('data-rating')); 
        star.innerHTML = ''; // Clear any existing content inside the rating-stars element

        // Calculate full stars and half star
        const fullStars = Math.floor(rating); // Full stars
        const decimalPart = rating - fullStars; // Decimal part to determine half star

        for (let i = 0; i < 5; i++) {
            const starElem = document.createElement('i');
            starElem.classList.add('fa', 'fa-star');

            // Add solid (filled) star class for full stars
            if (i < fullStars) {
                starElem.classList.add('fas');
                starElem.style.color = '#ffc107'; // Filled star color
            }
            // Add half star class for half star if decimal part is >= 0.5
            else if (i === fullStars && decimalPart >= 0.5) {
                starElem.classList.add('fas', 'half');
                starElem.style.color = '#ffc107'; // Filled star color
            }
            // Add outline star class for empty stars
            else {
                starElem.classList.add('far');
                starElem.style.color = '#ddd'; // Outline star color
            }

            star.appendChild(starElem); // Append the star icon to the rating-stars element
        }
    });
});
