function quiz(){
  var header = document.querySelector(".dropdown");
  header.innerHTML = 'Subjects:<br><select id ="drop" name="subjects"><option value="dbms_quiz">DBMS</option><option value="os_quiz">OS</option><option value="ca_quiz">Computer Architecture</option><option value="vb_quiz">Visual Basic</option><option value="eng_quiz">ENGLISH</option></select><div class="button2"><button type="button" onclick="select()">select</button></div>';

}

function select(){
  selected = document.getElementById('drop').value;
  anchor = document.getElementById("anchor");
  anchor.textContent = 'Go to '+selected;
  anchor.setAttribute("href","/quiz/staff_categories/"+selected+"/");
  console.log(selected)
  return selected
}
