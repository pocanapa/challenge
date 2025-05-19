// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.querySelector('.nav-links');

mobileMenuBtn.addEventListener('click', () => {
    mobileMenuBtn.textContent = mobileMenuBtn.textContent === '☰' ? '✕' : '☰';
    navLinks.classList.toggle('active');
    document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
});

// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
const currentTheme = localStorage.getItem('theme');

if (currentTheme === 'dark' || (!currentTheme && prefersDarkScheme.matches)) {
    document.documentElement.setAttribute('data-theme', 'dark');
    themeToggle.textContent = '☀️';
}

themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    if (currentTheme === 'dark') {
        document.documentElement.removeAttribute('data-theme');
        themeToggle.textContent = '🌓';
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        themeToggle.textContent = '☀️';
        localStorage.setItem('theme', 'dark');
    }
});

// FAQ Accordion
const faqQuestions = document.querySelectorAll('.faq-question');

faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        question.classList.toggle('active');
        const answer = question.nextElementSibling;

        if (question.classList.contains('active')) {
            answer.style.maxHeight = answer.scrollHeight + 'px';
        } else {
            answer.style.maxHeight = '0';
        }

        // Close other open FAQs
        faqQuestions.forEach(q => {
            if (q !== question && q.classList.contains('active')) {
                q.classList.remove('active');
                q.nextElementSibling.style.maxHeight = '0';
            }
        });
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });

            // Close mobile menu if open
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileMenuBtn.textContent = '☰';
                document.body.style.overflow = '';
            }
        }
    });
});

// Animation on scroll
const fadeElements = document.querySelectorAll('.fade-in');

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });

fadeElements.forEach(el => {
    el.style.opacity = 0;
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    fadeObserver.observe(el);
});

// Form validation and submission
const contactForm = document.getElementById('contactForm');
const formFeedback = document.getElementById('formFeedback');

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

function validatePhone(phone) {
    const re = /^(\+\d{1,3})?\s?\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$/;
    return re.test(phone) || phone === '';
}

function showError(inputId, message) {
    const errorElement = document.getElementById(`${inputId}Error`);
    errorElement.textContent = message;
    errorElement.style.display = 'block';
    document.getElementById(inputId).classList.add('error');
}

function hideError(inputId) {
    const errorElement = document.getElementById(`${inputId}Error`);
    errorElement.style.display = 'none';
    document.getElementById(inputId).classList.remove('error');
}

function handleSubmit(event) {
    event.preventDefault();

    // Reset feedback
    formFeedback.style.display = 'none';
    formFeedback.className = 'form-feedback';

    // Validate inputs
    let isValid = true;

    // Name validation
    const name = document.getElementById('name').value.trim();
    if (name === '' || name.length < 3) {
        showError('name', 'Por favor, insira seu nome completo');
        isValid = false;
    } else {
        hideError('name');
    }

    // Email validation
    const email = document.getElementById('email').value.trim();
    if (email === '' || !validateEmail(email)) {
        showError('email', 'Por favor, insira um email válido');
        isValid = false;
    } else {
        hideError('email');
    }

    // Phone validation
    const phone = document.getElementById('phone').value.trim();
    if (phone !== '' && !validatePhone(phone)) {
        showError('phone', 'Por favor, insira um telefone válido');
        isValid = false;
    } else {
        hideError('phone');
    }

    // Message validation
    const message = document.getElementById('message').value.trim();
    if (message === '' || message.length < 10) {
        showError('message', 'Por favor, insira uma mensagem com pelo menos 10 caracteres');
        isValid = false;
    } else {
        hideError('message');
    }

    if (isValid) {
        // Simulate form submission (in a real scenario, you would use AJAX or fetch)
        formFeedback.textContent = 'Obrigado pelo seu interesse! Nossa equipe entrará em contato em até 24 horas.';
        formFeedback.classList.add('success');
        formFeedback.style.display = 'block';

        // Reset form
        contactForm.reset();

        // Scroll to feedback
        formFeedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } else {
        formFeedback.textContent = 'Por favor, corrija os erros no formulário.';
        formFeedback.classList.add('error');
        formFeedback.style.display = 'block';
    }
}

// Add event listeners for real-time validation
document.getElementById('name').addEventListener('input', function () {
    if (this.value.trim().length >= 3) {
        hideError('name');
    }
});

document.getElementById('email').addEventListener('input', function () {
    if (validateEmail(this.value.trim())) {
        hideError('email');
    }
});

document.getElementById('phone').addEventListener('input', function () {
    if (this.value.trim() === '' || validatePhone(this.value.trim())) {
        hideError('phone');
    }
});

document.getElementById('message').addEventListener('input', function () {
    if (this.value.trim().length >= 10) {
        hideError('message');
    }
});

// Form submission
contactForm.addEventListener('submit', handleSubmit);

// Add floating animation to some elements
const floatElements = document.querySelectorAll('.solution-card, .feature-card, .team-member');
floatElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
        el.classList.add('float');
    });
    el.addEventListener('mouseleave', () => {
        el.classList.remove('float');
    });
});