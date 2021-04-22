const $input = $('#guess').val()
const $button = $('#submit')
const $form = $('#guess-form')
const base_url = 'http://127.0.0.1:5000/'

async function post_word(e){
  e.preventDefault();
  axios ({
    url: 'boggle.py',
    method: 'POST',
   data:{
     words: JSON.stringify($input)
   }
  })
}

$form.on('submit', post_word)
const answers = JSON.parse(results)
for (let answer of answers){
  console.log(answer)
}