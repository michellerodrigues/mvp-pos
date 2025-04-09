import { carregarTarefasUsuario } from './scripts.js';

document.addEventListener("DOMContentLoaded", function() {
    console.log("O documento está pronto!");
    carregarTarefasUsuario(); 

    document.getElementById('logoutBtn').addEventListener('click', function() {
        
        //TODO: Remover dados de sessão (implementar chamada no banco de dados)

      //  localStorage.removeItem('usuarioLogado');
      //  sessionStorage.removeItem('token');
        
        window.location.href = '.././index.html';
        
        // TODO: quando estiver usando jwt, limpar os cookies de domínio
        // document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    });

});