const emailCheck = () => {
  const inputEmail = document.querySelector('#email-input').value;
  const mailFormat = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  const format_validation = mailFormat.test(inputEmail.toLowerCase())
  const dup_validation = AjaxCall('../email-check/', {'email': inputEmail});
  if(dup_validation && format_validation) {
    document.querySelector('#email-result-success').style.display = 'block';
    document.querySelector('#email-result-duplication').style.display = 'none';
    document.querySelector('#email-result-format').style.display = 'none';
    return true
  } else if (dup_validation) {
    document.querySelector('#email-result-success').style.display = 'none';
    document.querySelector('#email-result-duplication').style.display = 'none';
    document.querySelector('#email-result-format').style.display = 'block';
  } else {
    document.querySelector('#email-result-success').style.display = 'none';
    document.querySelector('#email-result-duplication').style.display = 'block';
    document.querySelector('#email-result-format').style.display = 'none';
  }
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
  document.querySelector('#email-input').addEventListener('keyup', checkSubmitAllow, false);
}