document.addEventListener('DOMContentLoaded', (event) => {
    let currentQuestionIndex = 0;
    const questions = document.querySelectorAll('.quiz');
    const nextButtons = document.querySelectorAll('.next-btn');
    const prevButtons = document.querySelectorAll('.before-btn');
    const submit = document.querySelectorAll(".submit-btn");
    
    // ランダムにシャッフルする関数
    function shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }
    
    window.onload = function() {
        // すべてのクイズの選択肢を取得
        const boxes = document.querySelectorAll('.box');
    
        // 各クイズの選択肢をシャッフル
        boxes.forEach(box => {
            const options = Array.from(box.querySelectorAll('.option-label'));
            const shuffledOptions = shuffle(options);
            shuffledOptions.forEach(option => box.appendChild(option));
        });
    };
    //シャッフルここまで

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
