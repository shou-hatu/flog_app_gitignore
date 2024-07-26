document.addEventListener('DOMContentLoaded', (event) => {
    let currentQuestionIndex = 0;
    const questions = document.querySelectorAll('.quiz');
    const nextButtons = document.querySelectorAll('.next-btn');
    const prevButtons = document.querySelectorAll('.before-btn');
    const submit = document.querySelectorAll(".submit-btn");

    function showQuestion(index) {
        questions.forEach((question, i) => {
            question.style.display = i === index ? 'block' : 'none';
        });
    }

    nextButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentQuestionIndex++;
            if (currentQuestionIndex >= questions.length) {
                currentQuestionIndex = 0;
            }
            showQuestion(currentQuestionIndex);
        });
    });

    prevButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentQuestionIndex--;
            if (currentQuestionIndex < 0) {
                currentQuestionIndex = questions.length - 1;
            }
            showQuestion(currentQuestionIndex);
        });
    });

    // 初期表示
    showQuestion(currentQuestionIndex);

    //蛙化度計測ボタン用
    submit.style.display = 'none';
    if (currentQuestionIndex = questions.length) {
        submit.style.display = 'block';
    }


});
