// Main JavaScript for Voting System

document.addEventListener('DOMContentLoaded', function() {
    console.log('Voting System loaded');
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = 'none';
        }, 5000);
    });

    // Candidate card selection
    const candidateCards = document.querySelectorAll('.candidate-card');
    candidateCards.forEach(card => {
        card.addEventListener('click', function() {
            const radio = this.querySelector('input[type="radio"]');
            radio.checked = true;
        });
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = this.querySelectorAll('input[required], textarea[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#e74c3c';
                } else {
                    input.style.borderColor = '#ddd';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });
    // Handle edit candidate functionality
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const candidateId = this.getAttribute('data-id');
            const row = document.querySelector(`tr[data-candidate-id="${candidateId}"]`);
            const nameDisplay = row.querySelector('.candidate-name-display');
            const descDisplay = row.querySelector('.candidate-desc-display');
            const editForm = row.querySelector('.edit-form');

            // Hide display elements and show form
            nameDisplay.style.display = 'none';
            descDisplay.style.display = 'none';
            editForm.style.display = 'inline';

            // Hide edit button
            this.style.display = 'none';
        });
    });

    // Handle cancel edit functionality
    const cancelButtons = document.querySelectorAll('.cancel-btn');
    cancelButtons.forEach(button => {
        button.addEventListener('click', function() {
            const row = this.closest('tr');
            const nameDisplay = row.querySelector('.candidate-name-display');
            const descDisplay = row.querySelector('.candidate-desc-display');
            const editForm = row.querySelector('.edit-form');
            const editBtn = row.querySelector('.edit-btn');

            // Show display elements and hide form
            nameDisplay.style.display = '';
            descDisplay.style.display = '';
            editForm.style.display = 'none';

            // Show edit button
            editBtn.style.display = '';
        });
    });
});

// Fetch and display live results
function fetchResults() {
    fetch('/api/candidates')
        .then(response => response.json())
        .then(data => {
            console.log('Results:', data);
        })
        .catch(error => console.error('Error fetching results:', error));
}

// Refresh results every 10 seconds
setInterval(fetchResults, 10000);

