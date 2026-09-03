function add_carro(){
    console.log("adicionando carro");
     formalario = document.getElementById("form-carro");

     html = `
        <br> 
        <div class='row'>
            <div class='col-md'>
                <input type='text' class='form-control' placeholder='Carro' name = 'carro'>
            </div>
            <div class='col-md'>
                <input type='text' class='form-control' placeholder='Placa do carro' name = 'placa'>
            </div>
            <div class='col-md'>
                <input type='number' class='form-control' placeholder='Ano do carro' name = 'ano'>
            </div>

        </div>
     `

     formalario.innerHTML += html;
}

function exibir_form(tipo) {
    add_cliente = document.getElementById("adicionar-cliente");
    att_cliente = document.getElementById("att_cliente");

    if(tipo == '1'){
        att_cliente.style.display = "none";
        add_cliente.style.display = "block";
    }
    else if(tipo == '2'){
        add_cliente.style.display = "none";
        att_cliente.style.display = "block";
    }
}

function dados_cliente(){
    cliente = document.getElementById("cliente-select");
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
   
    id_cliente = cliente.value;

    data = new FormData();
    data.append('id_cliente', id_cliente);
    

    fetch("/clientes/atualizar_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },

        body: data

    }).then(function(result){
        return result.json();
    }).then(function(data){
        document.getElementById("form-att-cliente").style.display = "block";

        nome = document.getElementById("nome");
        nome.value = data.nome;

        sobrenome = document.getElementById("sobrenome");
        sobrenome.value = data.sobrenome;

        email = document.getElementById("email");
        email.value = data.email;

        cpf = document.getElementById("cpf");
        cpf.value = data.cpf;
        
    })
}