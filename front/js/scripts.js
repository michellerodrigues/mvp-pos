document.addEventListener("DOMContentLoaded", function() {
    console.log("O documento está pronto! scripts");
});

/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  // Mock de API
  --------------------------------------------------------------------------------------
*/


function criarComponenteTarefas(categoria, tarefas, posX = 0, posY = 0) {
    // Criar container
    const container = document.createElement('div');
    container.className = 'floating-table';
    container.style.left = `${posX}px`;
    container.style.top = `${posY}px`;

    // Cabeçalho
    const header = document.createElement('div');
    header.className = 'table-header';
    
    // Título
    const title = document.createElement('span');
    title.textContent = categoria;

    // Botão de minimizar
    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'toggle-visibility';
    toggleBtn.textContent = '−';
    toggleBtn.onclick = () => {
        content.style.display = content.style.display === 'none' ? 'block' : 'none';
    };

    // Conteúdo
    const content = document.createElement('div');
    content.className = 'table-content';

    // Montar estrutura
    header.appendChild(title);
    header.appendChild(toggleBtn);
    container.appendChild(header);
    container.appendChild(content);
    document.body.appendChild(container);

    // Adicionar tabela
    content.innerHTML = `
        <table>
            <thead>
                <tr>
                    <th>Tarefa</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                ${tarefas.map(tarefa => `
                    <tr>
                        <td>${tarefa.nome}</td>
                        <td>
                            <button 
                                class="toggle-btn ${tarefa.v ? 'on' : 'off'}"
                                onclick="toggleStatus(${tarefa.id}, ${!tarefa.v})"
                            >
                                ${tarefa.v ? 'ON' : 'OFF'}
                            </button>
                        </td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;

    // Tornar arrastável
    let isDragging = false;
    let currentX = 0;
    let currentY = 0;

    header.addEventListener('mousedown', startDragging);
    document.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', stopDragging);

    function startDragging(e) {
        isDragging = true;
        currentX = e.clientX;
        currentY = e.clientY;
        container.style.zIndex = 1001;
    }

    function drag(e) {
        if (isDragging) {
            const deltaX = e.clientX - currentX;
            const deltaY = e.clientY - currentY;
            
            container.style.left = `${container.offsetLeft + deltaX}px`;
            container.style.top = `${container.offsetTop + deltaY}px`;
            
            currentX = e.clientX;
            currentY = e.clientY;
        }
    }

    function stopDragging() {
        isDragging = false;
        container.style.zIndex = 1000;
    }
}


// Carregar Tarefas Usuario

export function carregarTarefasUsuario() {
    
    const mockAPI = {
        fetchData: () => Promise.resolve({
            data: 
                [ 
                    {
                        categoria: "Tarefas da Cozinha",
                        tarefas: [
                            { id: 1, nome: "Lavar louça", v: true },
                            { id: 2, nome: "Comprar frutas", v: false }
                        ]
                    },
                    {
                        categoria: "Tarefas do Escritório",
                        tarefas: [
                            { id: 3, nome: "Relatório mensal", v: true },
                            { id: 4, nome: "Reunião com equipe", v: false }
                        ]
                    }
                ]
        }),
        
        updateItem: (id, newStatus) => {
            console.log(`PUT /items/${id}`, { v: newStatus });
            return Promise.resolve({ success: true });
        }
    };
    
    mockAPI.fetchData().then(response => {
        response.data.forEach((categoria, index) => {
            // Posicionar tabelas em locais diferentes
            const posX = 50 + (index * 320);
            const posY = 50 + (index * 50);
            criarComponenteTarefas(categoria.categoria, categoria.tarefas, posX, posY);
        });
    });
}