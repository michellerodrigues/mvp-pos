document.addEventListener("DOMContentLoaded", function() {
    console.log("O documento está pronto! scripts");
});

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
                        <td>${tarefa.descricao}</td>
                        <td>
                            <div class="custom-control custom-switch">
                                <input 
                                    type="checkbox" 
                                    class="custom-control-input" 
                                    id="customSwitch${tarefa.id}"
                                    onclick="salvarExecucao(${tarefa.id}, this.checked)"
                                    checked
                                >
                                <label class="custom-control-label" for="customSwitch${tarefa.id}"></label>
                            </div>
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

export async function carregarTarefasUsuario()
{
    try {
        const response = await fetch('http://127.0.0.1:8002/api/categorias/', {
            mode: 'cors', // Padrão, pode omitir
            headers: {
              'Content-Type': 'application/json',
            }
          });

        if (!response.ok) {
            throw new Error('Erro na requisição');
        }
        const tarefas_usuario = await response.json();

        tarefas_usuario.forEach((categoria, index) => {
                // Posicionar tabelas em locais diferentes
                console.log('lista tarefas recebidas', categoria);
                console.log('lista tarefas index', index);
                const posX = 50 + (index * 320);
                const posY = 50 + (index * 50);
                criarComponenteTarefas(categoria.nome, categoria.tarefas, posX, posY);
            });

    } catch (error) {
        console.error('Erro ao buscar dados:', error);
        return [];
    }

}