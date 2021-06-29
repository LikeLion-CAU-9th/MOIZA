const logOut = () => {
  const action = confirm("정말로 로그아웃 하시겠어요?");
  if(action) {
    const result = AjaxCall('../logout-action/', {})
    if(result){
      location.href = "../login/";
    }
  }
}