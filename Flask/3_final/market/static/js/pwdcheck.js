function pwdCheck(){
    let p1=document.getElementById('pwd');
    let p2=document.getElementById('pwdcheck');
    let confirm_msg=document.getElementById('confirm_msg')
    let correct_color="#443e75";
    let wrong_color="#cd1d1d";

    console.log(p1.value)
    console.log(p2.value)

    if(p1.value== p2.value) { //비밀번호 일치
        confirm_msg.style.color=correct_color;
        confirm_msg.innerHTML="비밀번호 일치"
    }else{
        confirm_msg.style.color=wrong_color;
        confirm_msg.innerHTML="비밀번호 불일치"
    }
}
