const form = document.querySelector('#corr_form')

function store_input_values (){
    let form_values = JSON.stringify({
        'nome': form.nome_corr.value,
        'email': form.email_corr.value,
        'usuario': form.usuario_corr.value,
        'creci': form.creci_corr.value,
        'celular': form.celular_corr.value,
        'cpf': form.cpf_corr.value,
        'endereco': form.endereco_corr.value,
        'cidade': form.cidades.value,
        'bairro': form.bairros.value
      })
    sessionStorage.setItem('form_values', form_values)
}

form.addEventListener('submit', () => {
  store_input_values()
})

document.querySelector('#form_bairro').addEventListener('submit', ()=>{
    store_input_values()
})
document.querySelector('#cidade_form').addEventListener('submit',()=>{
    store_input_values()
})


window.addEventListener('load', () => {
  let inputs_values = JSON.parse(sessionStorage.getItem('form_values'))
  form.nome_corr.value = inputs_values.nome
  form.email_corr.value = inputs_values.email
  form.usuario_corr.value = inputs_values.usuario
  form.creci_corr.value = inputs_values.creci
  form.celular_corr.value = inputs_values.celular
  form.cpf_corr.value = inputs_values.cpf
  form.endereco_corr.value = inputs_values.endereco
  form.cidades.value = inputs_values.cidade
  form.bairros.value = inputs_values.bairro
})