// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
});

// Mobile menu toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
            mobileMenu.classList.remove('active');
        }
    });
}

// Auto-hide messages after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideIn 0.3s reverse';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
});

// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href && href !== '#') {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Card animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.6s ease-out';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.card').forEach(card => {
    observer.observe(card);
});

// Form validation
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        const requiredFields = form.querySelectorAll('[required]');
        let isValid = true;
        
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                field.style.borderColor = '#ff6b6b';
            } else {
                field.style.borderColor = '#dee2e6';
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            alert('Please fill in all required fields');
        }
    });
});

// Image preview for file inputs
document.querySelectorAll('input[type="file"]').forEach(input => {
    input.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function(event) {
                let preview = document.querySelector('.photo-preview');
                if (!preview) {
                    preview = document.createElement('img');
                    preview.className = 'photo-preview';
                    input.parentElement.insertBefore(preview, input);
                }
                preview.src = event.target.result;
            }
            reader.readAsDataURL(file);
        }
    });
});

// Price filter validation
const priceInput = document.querySelector('input[name="max_price"]');
if (priceInput) {
    priceInput.addEventListener('input', function() {
        if (this.value < 0) {
            this.value = 0;
        }
    });
}

// Date validation - prevent past dates
const dateInputs = document.querySelectorAll('input[type="date"]');
dateInputs.forEach(input => {
    const today = new Date().toISOString().split('T')[0];
    input.setAttribute('min', today);
});

// Animate stats on admin dashboard
const statNumbers = document.querySelectorAll('.stat-info h3');
if (statNumbers.length > 0) {
    statNumbers.forEach(stat => {
        const text = stat.textContent;
        const finalValue = parseInt(text.replace(/[^0-9]/g, ''));
        
        if (!isNaN(finalValue)) {
            let currentValue = 0;
            const increment = finalValue / 50;
            
            const updateCounter = () => {
                if (currentValue < finalValue) {
                    currentValue += increment;
                    stat.textContent = Math.ceil(currentValue);
                    requestAnimationFrame(updateCounter);
                } else {
                    stat.textContent = finalValue;
                }
            };
            
            const statObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        updateCounter();
                        statObserver.unobserve(entry.target);
                    }
                });
            });
            
            statObserver.observe(stat);
        }
    });
}

// Autocomplete for destination and airline inputs
function setupAutocomplete(inputElement, apiUrl) {
    let timeout = null;
    const resultsDiv = document.createElement('div');
    resultsDiv.className = 'autocomplete-results';
    inputElement.parentElement.style.position = 'relative';
    inputElement.parentElement.appendChild(resultsDiv);
    
    inputElement.addEventListener('input', function() {
        clearTimeout(timeout);
        const query = this.value.trim();
        
        if (query.length < 2) {
            resultsDiv.innerHTML = '';
            resultsDiv.style.display = 'none';
            return;
        }
        
        timeout = setTimeout(() => {
            fetch(`${apiUrl}?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    resultsDiv.innerHTML = '';
                    
                    if (data.length > 0) {
                        data.forEach(item => {
                            const div = document.createElement('div');
                            div.className = 'autocomplete-item';
                            div.textContent = item;
                            div.addEventListener('click', () => {
                                inputElement.value = item;
                                resultsDiv.innerHTML = '';
                                resultsDiv.style.display = 'none';
                            });
                            resultsDiv.appendChild(div);
                        });
                        resultsDiv.style.display = 'block';
                    } else {
                        resultsDiv.style.display = 'none';
                    }
                })
                .catch(error => {
                    console.error('Autocomplete error:', error);
                });
        }, 300);
    });
    
    // Close autocomplete when clicking outside
    document.addEventListener('click', (e) => {
        if (!inputElement.contains(e.target) && !resultsDiv.contains(e.target)) {
            resultsDiv.style.display = 'none';
        }
    });
}

// Initialize autocomplete on flights page
document.addEventListener('DOMContentLoaded', () => {
    const destinationInput = document.querySelector('input[name="destination"]');
    const airlineInput = document.querySelector('input[name="airline"]');
    
    if (destinationInput) {
        setupAutocomplete(destinationInput, '/api/autocomplete/destinations/');
    }
    
    if (airlineInput) {
        setupAutocomplete(airlineInput, '/api/autocomplete/airlines/');
    }
    
    // Scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                scrollObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.card, .section-title').forEach(el => {
        el.classList.add('scroll-animate');
        scrollObserver.observe(el);
    });
    
    // Add floating animation to icons
    document.querySelectorAll('.flight-arrow, .deal-badge').forEach(el => {
        el.classList.add('float');
    });
    
    // Smooth number counting for stats
    const countUp = (element, target, duration = 2000) => {
        let start = 0;
        const increment = target / (duration / 16);
        const timer = setInterval(() => {
            start += increment;
            if (start >= target) {
                element.textContent = Math.ceil(target);
                clearInterval(timer);
            } else {
                element.textContent = Math.ceil(start);
            }
        }, 16);
    };
    
    // Apply to stat numbers
    document.querySelectorAll('.stat-info h3').forEach(stat => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const text = stat.textContent.replace(/[^0-9]/g, '');
                    const num = parseInt(text);
                    if (!isNaN(num)) {
                        stat.textContent = '0';
                        countUp(stat, num);
                    }
                    observer.unobserve(stat);
                }
            });
        });
        observer.observe(stat);
    });
});
