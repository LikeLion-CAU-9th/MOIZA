const createGroup = () => {
  let groupName = document.querySelector('.groupName').value;
  let url = document.querySelector('.url').innerText;
  if(groupName.trim() < 1) {
    alert("그룹명을 입력하세요.");
    return false;
  }
  const result = AjaxCall('../create-group/', {'name': groupName, 'url': url});
  if(result){
    alert("성공적으로 그룹을 생성하였습니다.");
    window.location.href = "../mainpage/";
  } else{
    alert("그룹 생성에 실패하였습니다.");
  }
}

const get_hashed_url = () => {
  const url = AjaxCall('../generate-url/', {});
  document.querySelector('.url').innerHTML = url;
}