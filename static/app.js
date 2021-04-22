const $input = $('#guess').val()
const $button = $('#submit')
const $form = $('#guess-form')
const base_url = 'http://127.0.0.1:5000/'

function post_word(e){
  e.stopImmediatePropagation();
  $.ajax({
    url: 'app.py',
    type: 'POST',
   data:{
     words: JSON.stringify($input)
   }
  })
}

$form.on('submit', post_word)