function check(){
var luu=document.getElementById('lurl').value
if(luu==''){
document.getElementById("err").innerHTML="\"nothing entered\""
    return false
    }

var x=/^(http|https):\/\//
if(x.test(luu)){
      return true
                  }
else{
    document.getElementById("err").innerHTML="\"wrong url\""
    return false
   }
   
   
}
