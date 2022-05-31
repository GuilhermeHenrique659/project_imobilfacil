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