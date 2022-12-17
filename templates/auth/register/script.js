main.register = {
    data: {
        currentTab: 0,
        tabContainer: document.querySelectorAll(".tab"),
        btnNext: document.getElementById('nextBtn'),
        btnPrev: document.getElementById('prevBtn'),
        emailField: document.getElementById('useremail'),
        nicknameField: document.getElementById('nickname'),
        passwordField: document.getElementById('password'),
        passRepeatField: document.getElementById('passRepeat'),
        fileField: document.getElementById('avatar')
    },
    handler: {
        nextPrev: (n) => {
            // Эта функция определит, какую вкладку отображать
            let tabs = main.register.data.tabContainer;
            // Выйдите из функции, если какое-либо поле на текущей вкладке является недопустимым:
            if (n == 1 && !main.register.handler.validateForm()) return false;
            // Скрыть текущую вкладку:
            tabs[main.register.data.currentTab].style.display = "none";
            // Увеличьте или уменьшите текущую вкладку на 1:
            main.register.data.currentTab = main.register.data.currentTab + n;
            // если вы дошли до конца формы... :
            if (main.register.data.currentTab >= tabs.length) {
                // ...форма будет отправлена:
                document.getElementById("regForm").submit();
                return false;
            }
            // В противном случае отобразите правильную вкладку:
            main.register.methods.showTab(main.register.data.currentTab);
        },
        validateForm: () => {
            // Эта функция занимается проверкой полей формы
            var x, y, i, valid = true;
            x = document.getElementsByClassName("tab");
            y = x[main.register.data.currentTab].getElementsByTagName("input");
            // Цикл, который проверяет каждое поле ввода на текущей вкладке:
            for (i = 0; i < y.length; i++) {
                // Если поле пустое...
                if (y[i].value == "") {
                    // добавьте "invalid" класс в поле:
                    y[i].className += " invalid";
                    // и установите текущий допустимый статус на false:
                    valid = false;
                }
            }
            // If the valid status is true, mark the step as finished and valid:
            if (valid) {
                document.getElementsByClassName("step")[main.register.data.currentTab].className += " finish";
            }
            return valid; // верните действительный статус
        },
        fixStepIndicator: (n) => {
            // Эта функция удаляет "активный" класс всех шагов...
            var i, x = document.getElementsByClassName("step");
            for (i = 0; i < x.length; i++) {
              x[i].className = x[i].className.replace(" active", "");
            }
            // ... и добавляет "активный" класс к текущему шагу:
            x[n].className += " active";
        }
    },
    methods: {
        showTab: (n) => {
            // Эта функция отобразит указанную вкладку формы ...
            var x = document.getElementsByClassName("tab");
            x[n].style.display = "flex";
            // ... и исправьте кнопки "Предыдущий"/"Следующий":
            if (n == 0) {
                document.getElementById("prevBtn").style.display = "none";
            } else {
                document.getElementById("prevBtn").style.display = "inline";
            }
            if (n == (x.length - 1)) {
                document.getElementById('nextBtn').style.display = 'none';
                document.querySelector('input[type=submit]').style.display = 'inline';
            } else {
                document.getElementById('nextBtn').style.display = 'inline';
                document.querySelector('input[type=submit]').style.display = 'none';
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
    /* вызов функции шагов формы */
    main.register.methods.showTab(main.register.data.currentTab);
    main.register.data.btnNext.addEventListener('click', () => {
        main.register.handler.nextPrev(1)
    });
    main.register.data.btnPrev.addEventListener('click', () => {
        main.register.handler.nextPrev(-1)
    });

    /* Валидация форм */
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

    main.register.data.passRepeatField.addEventListener('input', () => {
        if (main.register.data.passwordField.value === main.register.data.passRepeatField.value) {
            document.getElementById('repeat-password-check').innerText = 'ok';
            main.register.data.btnNext.disabled = false;
        } else {
            document.getElementById('repeat-password-check').innerText = 'bad';
            main.register.data.btnNext.disabled = true;
        }
    })

    /* Загрузка файла */
    //
}());