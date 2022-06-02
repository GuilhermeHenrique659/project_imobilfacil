

const cidades = document.querySelector('#cidades')
cidades.addEventListener('change',()=>{
  console.log(cidades.value)
  if(cidades.value!=''){
    document.querySelector('#search_barr').removeAttribute('disabled')
  }else{
    document.querySelector('#search_barr').setAttribute('disabled','')
  }
})
const bairro_select = document.querySelector("#bairros")
const search = document.querySelector('#search_barr')

async function search_bairro(){
    let cidade = cidades.value
    let bairro = search.value
    const response = await fetch("/procura_bairro",{
      method: "POST",
      body: JSON.stringify({
        "cid_id": cidade,
        "bairro_nome": bairro
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    let bairro_reposense = await response.json()
    return bairro_reposense
}

function make_bairro_select(bairro_list){
      
      bairro_list.forEach(bairro => {
          bairro_select.innerHTML += `<option value="${bairro._id_bairro}">${bairro._bairro_nome}</option>`
      });
}

function remove_selectOptionBairro(list) {
  for (item of list) {
    item.remove()
  }
}

search.addEventListener('keyup', async ()=>{
  ENTER_KEY_ID = 13
  if (event.keyCode == ENTER_KEY_ID){
    let option_to_remove = bairro_select.children
    console.log(bairro_select.children)
    await remove_selectOptionBairro(option_to_remove)
    let bairro_list = await search_bairro()
    if (bairro_list.length > 0)
        make_bairro_select(bairro_list)
  }
})

document.getElementById('porcentagem').addEventListener('keyup', (event) => {
  valorimovel = document.getElementById('valor').value.replace('.', '')
  taxa = document.getElementById('porcentagem').value.replace('%', '')
  valorvenda = parseInt(valorimovel) + (parseInt(valorimovel) * parseFloat(taxa / 100))
  repasse = (parseInt(valorimovel) * parseFloat(taxa / 100))

  document.getElementById('valorvenda').value = valorvenda
  document.getElementById('repasse').value = repasse
})
document.getElementById('valor').addEventListener('keyup', ()=>{

  valorimovel = document.getElementById('valor').value.replace('.', '')
  taxa = document.getElementById('porcentagem').value.replace('%', '')
  valorvenda = parseInt(valorimovel) + (parseInt(valorimovel) * parseFloat(taxa / 100))
  repasse = (parseInt(valorimovel) * parseFloat(taxa / 100))

  document.getElementById('valorvenda').value = valorvenda
  document.getElementById('repasse').value = repasse
})