function check(){
  
    var luu=document.getElementById('lurl').value
    if(luu==''){
       document.getElementById("err").innerHTML="\"nothing entered\""
       return false
    }
    var x=/^(http|https):\/\//
    var z=/^http:\/\/((178\.79\.157\.230)|(bit\.ly)|(goo\.gl)|(ow\.ly))/
    var y=/^http:\/\/((localhost)|(127\.0\.0\.1))/
    if (y.test(luu)){
      document.getElementById("err").innerHTML="\"oops localhost\""
      return false
    }
    if(x.test(luu)){
      if(z.test(luu)){
       document.getElementById("err").innerHTML="\"already shortened\""
      return false
       }
      return true
    }
   else{
      document.getElementById("err").innerHTML="\"wrong url\""
      return false
   }
      
}
