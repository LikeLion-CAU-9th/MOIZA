const emailCheck = () => {
  const inputEmail = document.querySelector('#email-input').value;
  const validation = AjaxCall('../email-check/', {'email': inputEmail});
  if(validation) {
    document.querySelector('#email-result-success').style.display = 'block';
    document.querySelector('#email-result-fail').style.display = 'none';
    return true;
  }
  document.querySelector('#email-result-success').style.display = 'none';
  document.querySelector('#email-result-fail').style.display = 'block';
  return false;
}

const passwordCheck = () => {
  const pw1 = document.querySelector('#pw1').value;
  const pw2 = document.querySelector('#pw2').value;
  if(pw1 === pw2) {
    pwCorrect();
    return true;
  }
  pwNotCorrect();
  return false
}

const pwCorrect = () => {
  const pwcheckSpace = document.querySelector('#space-for-pwcheck');
  const failMessage = document.querySelector('#pw-result-fail');
  const singupBtn = document.querySelector('#signup-action-btn');
  pwcheckSpace.style.display = 'inline-block';
  failMessage.style.display = 'none';
  if(emailCheck()) {
    singupBtn.style.background = 'linear-gradient(105deg, #BD6ADF, #8D85DF)';
    singupBtn.style.pointerEvents = '';
  }
}

const pwNotCorrect = () => {
  const pwcheckSpace = document.querySelector('#space-for-pwcheck');
  const failMessage = document.querySelector('#pw-result-fail');
  const singupBtn = document.querySelector('#signup-action-btn');
  pwcheckSpace.style.display = 'none';
  failMessage.style.display = 'block';
  singupBtn.style.background = '#DDDDDD';
  singupBtn.style.pointerEvents = "none";
}

const checkSubmitAllow = () => {
  const singupBtn = document.querySelector('#signup-action-btn');
  if(emailCheck() && passwordCheck()){
    console.log("CORRECT!")
    singupBtn.style.background = 'linear-gradient(105deg, #BD6ADF, #8D85DF)';
    singupBtn.style.pointerEvents = '';
    return true
  }
    singupBtn.style.background = '#DDDDDD';
    singupBtn.style.pointerEvents = 'none';
  return false;
}

window.onload = () => {
  const singupBtn = document.querySelector('#signup-action-btn');
  singupBtn.style.pointerEvents = "none";
  document.querySelector('#pw2').addEventListener('keyup', passwordCheck, false);
  document.querySelector('#email-input').addEventListener('focusout', checkSubmitAllow, false);
}