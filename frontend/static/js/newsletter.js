const newsletterLink = document.getElementById('subscribe-link')
const newsletterForm = document.getElementById('newsletter-popup');
const closeNewsletter = document.getElementById('close-newsletter');
const successMessage = document.getElementById("success-message");
const closeMessages = document.querySelectorAll('.close-message-button');
const continueButton = document.getElementById('continue-button');

document.addEventListener("DOMContentLoaded", () => {
    const firstNameInput = document.getElementById('first-name');
    const lastNameInput = document.getElementById('last-name');
    const emailInput = document.getElementById('email');
    const confirmEmailInput = document.getElementById('confirm-email');
    const choiceField = document.getElementById('choice-field');
    const submitButton = document.querySelector('.submit-button');

    function hideNewsletterForm() {
        newsletterForm.style.display = 'none';
    };

    function showSpinner() {
        document.getElementById('overlay').style.display = 'block';
        document.getElementById('centered-spinner-container').style.display = 'block';
        document.body.classList.add('overlay-visible'); // Disable scrolling
    }
    
    function hideSpinner() {
        document.getElementById('overlay').style.display = 'none';
        document.getElementById('centered-spinner-container').style.display = 'none';
        document.body.classList.remove('overlay-visible'); // Enable scrolling
    }

    function clearNewsletterFormErrors() {
        //errors
        document.getElementById('first-name-char').style.display = 'none';
        document.getElementById('last-name-char').style.display = 'none';
        document.getElementById('invalid-email').style.display = 'none';
        document.getElementById('unmatching-email').style.display = 'none';
        document.getElementById('existing-email').style.display = 'none';
        //fields required
        document.getElementById('first-name-required').style.display = 'none';
        document.getElementById('last-name-required').style.display = 'none';
        document.getElementById('email-field-required').style.display = 'none';
        document.getElementById('confirm-email-field-required').style.display = 'none';
        firstNameInput.classList.remove('newsletter-field-error');
        lastNameInput.classList.remove('newsletter-field-error');
        emailInput.classList.remove('newsletter-field-error');
        confirmEmailInput.classList.remove('newsletter-field-error');    
    }

    function reinitialiseNewsletterForm() {
        firstNameInput.value = "";
        lastNameInput.value = "";
        emailInput.value = "";
        confirmEmailInput.value = "";
        choiceField.value = choiceField.options[0].value;
    }
    
    newsletterLink.addEventListener('click', (event) => {
        event.preventDefault(); 
        newsletterForm.style.display = 'block';
        newsletterLink.classList.add('hovered');
    });
    
    document.addEventListener('click', (event) => {
        if (!newsletterForm.contains(event.target) && event.target !== newsletterLink) {
            reinitialiseNewsletterForm();
            clearNewsletterFormErrors();
            hideNewsletterForm();
            newsletterLink.classList.remove('hovered');
        }
    });

    continueButton.addEventListener('click', () => {
        successMessage.style.display = 'none';
    })
    
    closeNewsletter.addEventListener('click', () => {
        reinitialiseNewsletterForm();
        clearNewsletterFormErrors();
        hideNewsletterForm();
        newsletterLink.classList.remove('hovered');
    });
    
    closeMessages.forEach(closeMessage => {
        closeMessage.addEventListener('click', () => {
            switch (closeMessage.getAttribute('close')) {
                case 'success-close':
                    successMessage.style.display = 'none';
                    break;
            }
        })
    })

    let SubmitNewsletter = async (first_name, last_name, email, confirm_email, choice) => {
        let fieldsFilledOut = true;
        if (first_name.trim() === '') {
            document.getElementById('first-name-required').style.display = 'block';
            firstNameInput.classList.add('newsletter-field-error');
            fieldsFilledOut = false;
        } 
        if (last_name.trim() === '') {
            document.getElementById('last-name-required').style.display = 'block';
            lastNameInput.classList.add('newsletter-field-error');
            fieldsFilledOut = false;
        }
        if (email.trim() === '') {
            document.getElementById('email-field-required').style.display = 'block';
            emailInput.classList.add('newsletter-field-error');
            fieldsFilledOut = false;
        } 
        if (confirm_email.trim() === '') {
            document.getElementById('confirm-email-field-required').style.display = 'block';
            confirmEmailInput.classList.add('newsletter-field-error');
            fieldsFilledOut = false;
        }
        
        if (fieldsFilledOut) {
            console.log(last_name)
            let response = await fetch(`/products/newsletter/?first_name=${first_name}&last_name=${last_name}&email=${email}&confirm_email=${confirm_email}&choice=${choice}`); 
            let data = await response.json();
            return data.response;                
        }
    }        

    submitButton.addEventListener('click', async (event) => {
        event.preventDefault(); 

        const firstNameValue = firstNameInput.value;
        const lastNameValue = lastNameInput.value;
        const emailValue = emailInput.value;
        const confirmEmailValue = confirmEmailInput.value;
        const choiceValue = choiceField.value;
                
        clearNewsletterFormErrors();

        showSpinner();
        const response = await SubmitNewsletter(firstNameValue, lastNameValue, emailValue, confirmEmailValue, choiceValue)
        hideSpinner();

        switch (response) {
            case 'success':
                hideNewsletterForm();
                newsletterLink.classList.remove('hovered');
                successMessage.style.display = "block";
                reinitialiseNewsletterForm();
                break;
            case 'failure':
                document.getElementById('existing-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                confirmEmailInput.value = "";
                choiceField.value = choiceField.options[0].value;
                break;
            case 'invalid-email':
                document.getElementById('invalid-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                break;
            case 'unmatching-email':
                document.getElementById('unmatching-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                confirmEmailInput.classList.add('newsletter-field-error');
                break;
            case 'existing-email':
                document.getElementById('existing-email').style.display = 'block';
                emailInput.classList.add('newsletter-field-error');
                confirmEmailInput.value = "";
                choiceField.value = choiceField.options[0].value;
                break;
            case 'invalid-first-name':
                document.getElementById('first-name-char').style.display = 'block';
                firstNameInput.classList.add('newsletter-field-error');
                break;
            case 'invalid-last-name':
                lastNameInput.classList.add('newsletter-field-error');
                document.getElementById('last-name-char').style.display = 'block';
                break;
        }
    });
});
