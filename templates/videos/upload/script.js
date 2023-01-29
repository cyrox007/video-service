main.videoloader = {
    data: {
        uploadForm: document.getElementById('upload-form'),
        inputVideo: document.getElementById('input-file'),
        videoTypes: [
            'mp4',
            'avi'
        ],
        progressBarContainer: document.getElementById('progress-bar'),
        progressBar: () => {
            return main.videoloader.data.progressBarContainer.querySelector('span');
        },
        formFields: document.querySelectorAll('.videos-upload__form--field')
    },
    handler: {
        checkVideo: () => {
            let file = main.videoloader.data.inputVideo.files[0];
            main.videoloader.data.videoTypes.every(el => {
                let typ = 'video/' + el;
                if (file.type == typ) {
                    main.videoloader.methods.videoUploader(file);
                } else {
                    alert(file.type);
                }
            });
        },
        percentMath: (x, y) => {
            let math = Math.round((100 - (x / y)) * 100) / 100;
            let result = math + '%';
            return result;
        },
        prefilling_out_form: (file) => {
            let name = document.getElementById('video_name');
            name.value = file.name;
        }
    },
    methods: {
        videoUploader: (file) => {
            let formData = new FormData();
            formData.append("myfile", file);
            main.videoloader.handler.prefilling_out_form(file);
            let xhr = new XMLHttpRequest();

            // отслеживаем процесс отправки
            xhr.upload.onprogress = function (event) {
                main.videoloader.data.uploadForm.classList.add('hidden');
                main.videoloader.data.progressBarContainer.classList.add('active');
                let bar = main.videoloader.data.progressBarContainer.querySelector('span');
                bar.classList.add('loaded');
                bar.style.width = main.videoloader.handler.percentMath(event.total, event.loaded);
                bar.textContent = 'Загрузка ' + main.videoloader.handler.percentMath(event.total, event.loaded);
            };

            // Ждём завершения: неважно, успешного или нет
            xhr.onloadend = function () {
                if (xhr.status == 200) {
                    console.log("Успех");
                } else {
                    console.log("Ошибка " + this.status);
                    main.videoloader.data.progressBar().classList.remove('loaded');
                    main.videoloader.data.progressBar().classList.add('error');
                    main.videoloader.data.progressBar().textContent = "Ошибка " + this.status;
                }
            };

            xhr.open("POST", "{{ url_for('video-upload') }}");

            xhr.send(formData);

            xhr.onload = () => {
                let response = JSON.parse(xhr.response);
                if (response.ok == 'ok') {
                    console.log("Загрузка завершена");
                    main.videoloader.data.progressBar().classList.remove('loaded');
                    main.videoloader.data.progressBar().classList.add('success');
                    main.videoloader.data.progressBar().style.width = '100%';
                    main.videoloader.data.progressBar().textContent = "Загрузка завершена";
                    let wrng = document.getElementById('warning');
                    wrng.innerText = "Видео загружено, и начата его обработка, теперь форму можно закрыть. Не забудьте сохранить изменения";
                    wrng.classList.remove('grey');
                    wrng.classList.add('green');
                }
            };
        }
    }
};
(function () {
    main.videoloader.data.inputVideo.addEventListener('change', () => {
        main.videoloader.handler.checkVideo();
    });
    main.videoloader.data.formFields.forEach(el => {
        let input = el.querySelector('input[type=text]');
        if (input != null) {
            input.addEventListener('focus', (e) => {
                el.classList.toggle('focus');
                console.log(e);
            })
        }
    });
}());