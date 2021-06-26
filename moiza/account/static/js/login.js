const loginAction = () => {
  const userEmail = document.querySelector('#input_email').value;
  const userPw = document.querySelector('#input_pw').value;
  result = AjaxCall('../login-action/', {"email": userEmail, "pw": userPw}, 'GET', false);
  
  if(result) {
    location.href = "../mainpage/";
  }else{
    // Else로 처리 안하면 success로 넘어갈 때 모달 나타남
    modal_on('login-fail');
  }
}
