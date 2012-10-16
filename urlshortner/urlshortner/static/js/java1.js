function check(){
  
    var luu=document.getElementById('lurl').value
    if(luu==''){
       document.getElementById("err").innerHTML="\"nothing entered\""
       return false
    }
    var x=/^(http|https):\/\//
    var z=/^http:\/\/178\.79\.157\.230/
     
    if (luu.length<=20||z.test(luu)){
       document.getElementById("err").innerHTML="\"already shortened\""
      return false
    }
    if(x.test(luu)){
      return true
      
    
    }
   else{
      document.getElementById("err").innerHTML="\"wrong url\""
      return false
   }
      
}
