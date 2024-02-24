document.addEventListener("domContentLoaded",main())


function main(){
  const demoQs = {
    "questions": [
      {
        "question": "What is the sum of the geometric series with |r| < 1?",
        "options": ["1/(1 + r)", "1/(1 - r)", "(1 - r)/r", "(1 + r)/r"],
        "answer": "1/(1 - r)"
      },
      {
        "question": "What does .a1a2a3 ... represent?",
        "options": ["An integer", "A rational number", "An irrational number", "A complex number"],
        "answer": "A rational number"
      },
      {
        "question": "How is the sum of the series Pan/10n obtained?",
        "options": ["Through Integration", "Using the Comparison Test", "Using Differentiation", "Using the Ratio Test"],
        "answer": "Using the Comparison Test"
      },
      {
        "question": "What does a terminating decimal represent?",
        "options": ["A rational number", "An irrational number", "An integer", "A prime number"],
        "answer": "A rational number"
      },
      {
        "question": "What is the repeating decimal 0.5910˙ 2 expressed as a quotient of two integers?",
        "options": ["59043/99900", "59102/99999", "59100/100000", "591/999"],
        "answer": "59043/99900"
      },
      {
        "question": "How are irrational numbers represented in decimal expansions?",
        "options": ["As repeating decimals", "As terminating decimals", "As non-repeating decimals", "As integers"],
        "answer": "As non-repeating decimals"
      },
      {
        "question": "How can the decimal expansion of an arbitrary real number be computed?",
        "options": ["Using the division algorithm", "Using long division", "Through integration", "By differentiation"],
        "answer": "Using the division algorithm"
      },
      {
        "question": "What type of numbers do terminating and repeating decimal expansions represent?",
        "options": ["Rational numbers", "Irrational numbers", "Real numbers", "Complex numbers"],
        "answer": "Rational numbers"
      },
      {
        "question": "What does the division algorithm help in computing for rational numbers?",
        "options": ["Quotient and Remainder", "Exponentiation", "Factorial", "Square root"],
        "answer": "Quotient and Remainder"
      },
      {
        "question": "What is the decimal expansion of 5/14?",
        "options": ["0.714285˙", "0.357142˙", "0.142857˙", "0.285714˙"],
        "answer": "0.357142˙"
      }
    ]
  }
  let correctAnswers=0;
  let qsAnswered=0;
  let qIndex=0;
  let q_text = document.getElementById("q-text");
  let a1_text = document.getElementById("a1-text")
  let a2_text = document.getElementById("a2-text")
  let a3_text = document.getElementById("a3-text")
  let a4_text = document.getElementById("a4-text")
  let score_text = document.getElementById("score-text")
  let currentq;
  function update(){
    q_text.innerHTML = demoQs.questions[qIndex].question
    a1_text.innerHTML = demoQs.questions[qIndex].options[0]
    a2_text.innerHTML = demoQs.questions[qIndex].options[1]
    a3_text.innerHTML = demoQs.questions[qIndex].options[2]
    a4_text.innerHTML = demoQs.questions[qIndex].options[3]
    score_text.innerHTML=`${correctAnswers} / ${qsAnswered}`
    currentq = demoQs.questions[qIndex]
  }
  update();
  let a1_box = document.getElementById("a1-box")
  let a2_box = document.getElementById("a2-box")
  let a3_box = document.getElementById("a3-box")
  let a4_box = document.getElementById("a4-box")

  a1_box.addEventListener("click", function() {
    answerClicked(currentq.answer == currentq.options[0]);
  });
  a2_box.addEventListener("click", function() {
answerClicked(currentq.answer == currentq.options[1]);  });
  a3_box.addEventListener("click", function() {
    answerClicked(currentq.answer == currentq.options[2]);
  });
  a4_box.addEventListener("click", function() {
    answerClicked(currentq.answer == currentq.options[3]);
  });
  
  function answerClicked(isCorrect){
    qsAnswered++;
    if(isCorrect){
      correctAnswers++;
    }
    qIndex= (qIndex+1)%demoQs.questions.length;
    update();
  }
}

