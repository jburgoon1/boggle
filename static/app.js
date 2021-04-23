$(function(){
const inputGuess = $("#guess").val();
const $button = $('#submit');
const $form = $('#guess-form');
const base_url = 'http://127.0.0.1:5000/';
const $score = $('#score')
$form.on('submit', async function (e){
  e.preventDefault();
  
  await axios ({
    url: base_url + 'answer',
    method: 'POST',
    
   data:{
     guess: inputGuess
   }
  });
});
})
let timer = 60
setInterval(function(){
  timer -= 1
  console.log(time)
},1000)
$('#time').append('<p>timer</p>')
