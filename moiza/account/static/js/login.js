const loginAction = () => {
  const userId = document.querySelector('#input_id').value;
  const userPw = document.querySelector('#input_pw').value;
  result = AjaxCall('../login-action/', 'GET', false, {"id": userId, "pw": userPw});
  
  if(result) {
    location.href = "../success/";
  }
  modal_on('login-fail');
}
