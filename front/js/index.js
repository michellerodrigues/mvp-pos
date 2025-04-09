document.addEventListener("DOMContentLoaded", function() {
    console.log("O documento está pronto! scripts index");

    const loginForm = document.getElementById("loginForm");

    if(loginForm)
    {
        loginForm.addEventListener("submit", async function(event) {
            event.preventDefault(); //TODO: verificar a necessidade de real de usar o preventDefault
        
            const email = document.getElementById("email").value;
            const senha = document.getElementById("senha").value;
        
            if (!email || !senha) {
                alert("Por favor, preencha todos os campos!");
                return;
            }
        
            if (!email.includes("@") || !email.includes(".")) {
                alert("Por favor, insira um e-mail válido!");
                return;
            }
        
               
            try {
                const response = await fetch('http://localhost:8002/api/usuarios/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: email,
                        senha: senha
                    })
                });
                
                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || 'Erro no login');
                }
                
                const data = await response.json();
                localStorage.setItem('emailUsuario', data.email);
                window.location.href = ".././painelUsuario.html";
            } catch (error) {
                document.getElementById('error-message').textContent = error.message;
            }
        });
    }
});