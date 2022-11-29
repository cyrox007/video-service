main.register = {
    data: {
        currentTab: 0,
        btnNext: document.getElementById('nextBtn'),
        btnPrev: document.getElementById('prevBtn'),
        emailField: document.getElementById('email'),
        nicknameField: document.getElementById('nickname'),
        passwordField: document.getElementById('password'),
        passRepeatField: document.getElementById('repeat-password'),
        fileField: document.getElementById('file-input')
    },
    handler: {
        nextPrev: (n) => {
            // This function will figure out which tab to display
            var x = document.getElementsByClassName("tab");
            // Exit the function if any field in the current tab is invalid:
            if (n == 1 && !main.register.handler.validateForm()) return false;
            // Hide the current tab:
            x[main.register.data.currentTab].style.display = "none";
            // Increase or decrease the current tab by 1:
            main.register.data.currentTab = main.register.data.currentTab + n;
            // if you have reached the end of the form... :
            if (main.register.data.currentTab >= x.length) {
                //...the form gets submitted:
                document.getElementById("regForm").submit();
                return false;
            }
            // Otherwise, display the correct tab:
            main.register.methods.showTab(main.register.data.currentTab);
        },
        validateForm: () => {
            // This function deals with validation of the form fields
            var x, y, i, valid = true;
            x = document.getElementsByClassName("tab");
            y = x[main.register.data.currentTab].getElementsByTagName("input");
            // A loop that checks every input field in the current tab:
            for (i = 0; i < y.length; i++) {
                // If a field is empty...
                if (y[i].value == "") {
                    // add an "invalid" class to the field:
                    y[i].className += " invalid";
                    // and set the current valid status to false:
                    valid = false;
                }
            }
            // If the valid status is true, mark the step as finished and valid:
            if (valid) {
                document.getElementsByClassName("step")[main.register.data.currentTab].className += " finish";
            }
            return valid; // return the valid status
        },
        fixStepIndicator: (n) => {
            // This function removes the "active" class of all steps...
            var i, x = document.getElementsByClassName("step");
            for (i = 0; i < x.length; i++) {
              x[i].className = x[i].className.replace(" active", "");
            }
            //... and adds the "active" class to the current step:
            x[n].className += " active";
        }
    },
    methods: {
        showTab: (n) => {
            // This function will display the specified tab of the form ...
            var x = document.getElementsByClassName("tab");
            x[n].style.display = "flex";
            // ... and fix the Previous/Next buttons:
            if (n == 0) {
                document.getElementById("prevBtn").style.display = "none";
            } else {
                document.getElementById("prevBtn").style.display = "inline";
            }
            if (n == (x.length - 1)) {
                document.getElementById("nextBtn").innerHTML = "Submit";
            } else {
                document.getElementById("nextBtn").innerHTML = "Next";
            }
            // ... and run a function that displays the correct step indicator:
            main.register.handler.fixStepIndicator(n)
        },
        validateEmail: async (data) => {
            if (data.length >= 6 && data.includes('@') && data.includes('.')) {
                let response = await fetch("{{ url_for('valid-email') }}", {
                    method: 'POST',
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(data)
                });
                let result = await response.json();
                if (result['ok'] == true) {
                    return true
                }
            }
            return false;
        },
        validateNickname: async (data) => {
            if (data != '') {
                let response = await fetch("{{ url_for('valid-nickname') }}", {
                    method: 'POST',
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(data)
                });
                let result = await response.json();

                if (result['ok'] == true) {
                    return true;
                }
            }
            return false;
        }
    }
};
(function () {
    main.register.methods.showTab(main.register.data.currentTab);
    main.register.data.btnNext.addEventListener('click', () => {
        main.register.handler.nextPrev(1)
    });
    main.register.data.btnPrev.addEventListener('click', () => {
        main.register.handler.nextPrev(-1)
    });

    
    main.register.data.emailField.addEventListener('change', () => {
        let check = main.register.methods.validateEmail(main.register.data.emailField.value);
        check.then(result => {
            if (result) {
                document.getElementById('email-check').innerText = 'ok';
                main.register.data.btnNext.disabled = false;
            } else {
                document.getElementById('email-check').innerText = 'bad';
                main.register.data.btnNext.disabled = true;
            }
        });
    });

    main.register.data.nicknameField.addEventListener('change', () => {
        let check = main.register.methods.validateNickname(main.register.data.nicknameField.value);
        check.then(result => {
            if (result) {
                document.getElementById('nickname-check').innerText = 'ok';
                main.register.data.btnNext.disabled = false;
            } else {
                document.getElementById('nickname-check').innerText = 'bad';
                main.register.data.btnNext.disabled = true;
            }
        });
    });

    main.register.data.passwordField.addEventListener('change', () => {
        if (main.register.data.passwordField.value.length >= 8) {
            document.getElementById('password-check').innerText = 'ok';
            main.register.data.btnNext.disabled = false;
        } else {
            document.getElementById('password-check').innerText = 'bad';
            main.register.data.btnNext.disabled = true;
        }
    });

    main.register.data.passRepeatField.addEventListener('change', () => {
        if (main.register.data.passwordField.value === main.register.data.passRepeatField.value) {
            document.getElementById('repeat-password-check').innerText = 'ok';
            main.register.data.btnNext.disabled = false;
        } else {
            document.getElementById('repeat-password-check').innerText = 'bad';
            main.register.data.btnNext.disabled = true;
        }
    })

    let uploadContainer = document.getElementById('uploadContainer');

    uploadContainer.addEventListener('dragenter', (e) => {
        e.preventDefault();
        uploadContainer.classList.add('dragover');
    });

    uploadContainer.addEventListener('dragenter', (e) => {
        e.preventDefault();
        uploadContainer.classList.add('dragover');
    });

    uploadContainer.addEventListener('dragleave', (e) => {
        e.preventDefault();
        uploadContainer.classList.remove('dragover');
    });

    uploadContainer.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadContainer.classList.remove('dragover');
        let files = e.dataTransfer.files;
    });
    
    main.register.data.fileField.addEventListener('change', () => {
        let files = this.files;
    });
}());