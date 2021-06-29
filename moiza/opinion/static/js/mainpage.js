const createGroup = () => {
  let groupName = document.querySelector('.groupName').value;
  if(groupName.trim() < 1) {
    alert("그룹명을 입력하세요.");
    return false;
  }
  const result = AjaxCall('../create-group/', {'name': groupName});
  if(result){
    alert("성공적으로 그룹을 생성하였습니다.");
    window.location.href = "../group-page";
  } else{
    alert("그룹 생성에 실패하였습니다.");
  }
}