const loginAction = () => {
  const userId = document.querySelector('#input_id').value;
  const userPw = document.querySelector('#input_pw').value;
  result = AjaxCall('../login-action/', {"id": userId, "pw": userPw}, 'GET', false);
  
  if(result) {
    location.href = "../success/";
  }
  modal_on('login-fail');
}
