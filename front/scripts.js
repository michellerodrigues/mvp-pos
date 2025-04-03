document.addEventListener("DOMContentLoaded", function() {
    console.log("O documento está pronto!");
});

/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  // Mock de API
  --------------------------------------------------------------------------------------
*/


const mockAPI = {
    fetchData: () => Promise.resolve({
        data: 
            [ 
                {
                    categoria: "Tarefas da Cozinha", 
                    tarefas: 
                    [
                        { id: 1, nome: "Maçã", v: true },
                        { id: 2, nome: "Banana", v: false },
                        { id: 3, nome: "Laranja", v: true },
                        { id: 4, nome: "Uva", v: false },
                        { id: 5, nome: "Pera", v: true }
                    ]
                }
            ]
    }),
    
    updateItem: (id, newStatus) => {
        console.log(`PUT /items/${id}`, { v: newStatus });
        return Promise.resolve({ success: true });
    }
};

// Função para renderizar a tabela
function renderTable(data) {
    const thead = document.getElementById('categoria-tarefa');
    
    thead.innerHTML = data.map(item => `
        <tr>
            <th>${item.categoria}</th>
            <th></th>
        </tr>
    `).join('');
           
    const tbody = document.getElementById('tabelaItens');

    tbody.innerHTML = data[0].tarefas.map(tarefa =>
       ` <tr>
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
    `).join('');
}
        

// Função para alternar status
async function toggleStatus(id, newStatus) {
    try {
        await mockAPI.updateItem(id, newStatus);
        
        // Atualizar dados locais (simulando resposta da API)
        const updatedData = mockData.data.map(item => 
            item.id === id ? { ...item, v: newStatus } : item
        );
        
        renderTable(updatedData);
    } catch (error) {
        console.error('Erro ao atualizar:', error);
        alert('Erro ao atualizar status!');
    }
}

// Carregar dados iniciais
let mockData;
mockAPI.fetchData()
    .then(response => {
        mockData = response;
        renderTable(mockData.data);
    })
    .catch(error => console.error('Erro ao carregar dados:', error));

// Exemplo: Adicionar novo item após 3 segundos
setTimeout(() => {
    const newItem = { id: 6, nome: "Morango", v: false };
    mockData.data.push(newItem);
    renderTable(mockData.data);
}, 3000);