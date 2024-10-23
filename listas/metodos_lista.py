pedidos = []

# O cliente faz um pedido
pedidos.append("hamburguer")
pedidos.append("batata")
print("Pedidos:", pedidos)

# O cliente adiciona mais itens
pedidos.insert(1, "refrigerante")
print("Pedidos atualizados:", pedidos)

# O cliente decide remover algo
pedidos.remove("hamburguer")
print("Após remover hambúrguer:", pedidos)

# Conta quantas batatas foram pedidas
print("Quantidade de batatas pedidas:", pedidos.count("batata"))

# Reverte a ordem dos pedidos
pedidos.reverse()
print("Pedidos após reversão:", pedidos)

# Remove o último pedido
ultimo_pedido = pedidos.pop()
print("Último pedido removido:", ultimo_pedido)
print("Pedidos finais:", pedidos)

# Limpa todos os pedidos
pedidos.clear()
print("Todos os pedidos foram removidos:", pedidos)
