
function session_storege_cpf(){
    sessionStorage.setItem('nome',document.getElementById('nome').value)
    sessionStorage.setItem('cpf',document.getElementById('cpf').value)
    sessionStorage.setItem('rg',document.getElementById('rg').value)
    sessionStorage.setItem('sexo',document.getElementById('sexo').value)
    sessionStorage.setItem('endereco',document.getElementById('endereco').value)
    sessionStorage.setItem('numero',document.getElementById('numero').value)
    sessionStorage.setItem('cep',document.getElementById('cep').value)
    sessionStorage.setItem('cidades',document.getElementById('cidades').value)
    sessionStorage.setItem('bairros',document.getElementById('bairros').value)
    sessionStorage.setItem('email',document.getElementById('email').value)
    sessionStorage.setItem('whatsapp',document.getElementById('whatsapp').value)
    sessionStorage.setItem('celular',document.getElementById('celular').value)
    sessionStorage.setItem('telefone',document.getElementById('telefone').value)
}
function session_storege_cnpj(){
    sessionStorage.setItem('nome-fantasia',document.getElementById('nome-fantasia').value)
    sessionStorage.setItem('razao',document.getElementById('razao').value)
    sessionStorage.setItem('doc_federal',document.getElementById('doc_federal').value)
    sessionStorage.setItem('doc_estadual',document.getElementById('doc_estadual').value)
    sessionStorage.setItem('atividade',document.getElementById('atividade').value)
    sessionStorage.setItem('endereco-jur',document.getElementById('endereco-jur').value)
    sessionStorage.setItem('numero-jur',document.getElementById('numero-jur').value)
    sessionStorage.setItem('cep-jur',document.getElementById('cep-jur').value)
    sessionStorage.setItem('cidades-jur',document.getElementById('cidades-jur').value)
    sessionStorage.setItem('bairros-jur',document.getElementById('bairros-jur').value)
    sessionStorage.setItem('email-jur',document.getElementById('email-jur').value)
    sessionStorage.setItem('whatsapp-jur',document.getElementById('whatsapp-jur').value)
    sessionStorage.setItem('celular-jur',document.getElementById('celular-jur').value)
    sessionStorage.setItem('telefone-jur',document.getElementById('telefone-jur').value)
    sessionStorage.setItem('capital',document.getElementById('capital').value)
    sessionStorage.setItem('patrimonio',document.getElementById('patrimonio').value)
}

document.getElementById('form-fisica').addEventListener('submit', function(event){
    session_storege_cpf()
})
document.getElementById('form-juridica').addEventListener('submit', function(event){
    session_storege_cnpj()
})

document.getElementById('cidade').addEventListener('submit', function(event){
    session_storege_cpf()
    session_storege_cnpj()
})
document.getElementById('bairro').addEventListener('submit', function(event){
    session_storege_cnpj()
    session_storege_cpf()
})


window.addEventListener('load', (event) => {
    document.getElementById('nome').value = sessionStorage.getItem('nome')
    document.getElementById('codigo').value = sessionStorage.getItem('codigo')
    document.getElementById('cpf').value = sessionStorage.getItem('cpf')
    document.getElementById('sexo').value = sessionStorage.getItem('sexo')
    document.getElementById('rg').value = sessionStorage.getItem('rg')
    document.getElementById('endereco').value = sessionStorage.getItem('endereco')
    document.getElementById('numero').value = sessionStorage.getItem('numero')
    document.getElementById('cep').value = sessionStorage.getItem('cep')
    document.getElementById('cidades').value = sessionStorage.getItem('cidades')
    document.getElementById('bairros').value = sessionStorage.getItem('bairros')
    document.getElementById('email').value = sessionStorage.getItem('email')
    document.getElementById('whatsapp').value = sessionStorage.getItem('whatsapp')
    document.getElementById('celular').value = sessionStorage.getItem('celular')
    document.getElementById('telefone').value = sessionStorage.getItem('telefone')


    document.getElementById('nome-fantasia').value = sessionStorage.getItem('nome-fantasia')
    document.getElementById('codigo-jur').value = sessionStorage.getItem('codigo-jur')
    document.getElementById('doc_federal').value = sessionStorage.getItem('doc_federal')
    document.getElementById('doc_estadual').value = sessionStorage.getItem('doc_estadual')
    document.getElementById('atividade').value = sessionStorage.getItem('atividade')
    document.getElementById('endereco-jur').value = sessionStorage.getItem('endereco-jur')
    document.getElementById('numero-jur').value = sessionStorage.getItem('numero-jur')
    document.getElementById('cep-jur').value = sessionStorage.getItem('cep-jur')
    document.getElementById('cidades-jur').value = sessionStorage.getItem('cidades-jur')
    document.getElementById('bairros-jur').value = sessionStorage.getItem('bairros-jur')
    document.getElementById('email-jur').value = sessionStorage.getItem('email-jur')
    document.getElementById('whatsapp-jur').value = sessionStorage.getItem('whatsapp-jur')
    document.getElementById('celular-jur').value = sessionStorage.getItem('celular-jur')
    document.getElementById('telefone-jur').value = sessionStorage.getItem('telefone-jur')
    document.getElementById('capital').value = sessionStorage.getItem('capital')
    document.getElementById('patrimonio').value = sessionStorage.getItem('patrimonio')

})